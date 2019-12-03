import sys
import os
from core.app import app
from beaker.middleware import SessionMiddleware
import json
import pprint
from gzip import compress


sys.path.insert(0, os.path.dirname(__file__))

def application2(environ, start_response):
    app_web = app(os.path.dirname(__file__))
    main_data = app_web.init(environ)
    ret = main_data["response_body"]

    if not isinstance(ret,str):
        ret=json.dumps(ret, indent=4)

    if isinstance(ret, str):
        if ret != "":
            ret = compress(bytes(ret, "utf-8"))
            main_data["headers"].append(("Accept-encoding", "gzip,deflate"))
            main_data["headers"].append(("Content-Encoding", "gzip"))
        else:
            ret = b""

    main_data["headers"].append(("Access-Control-Allow-Origin", "*"))

    start_response(main_data["status"], main_data["headers"])
    if "is_file" in main_data and main_data["is_file"]:
        f = open(main_data["file"], "rb")
        if "wsgi.file_wrapper" in environ:
            return environ["wsgi.file_wrapper"](f, 1024)
        else:
            return file_wrapper(f, 1024)
    else:
        return [ret]


def file_wrapper(fileobj, block_size=1024):
    try:
        data = fileobj.read(block_size)
        while data:
            yield data
            data = fileobj.read(block_size)
    finally:
        fileobj.close()


class LoggingMiddleware:
    def __init__(self, application):
        self.__application = application

    def __call__(self, environ, start_response):
        errors = environ["wsgi.errors"]

        def _start_response(status, headers, *args):
            if status != "200 OK":
                # pprint.pprint(('REQUEST', environ), stream=errors)
                pprint.pprint(("REQUEST:", environ["PATH_INFO"]), stream=errors)
                # pprint.pprint(('RESPONSE', status, headers), stream=errors)
                pprint.pprint(("RESPONSE:", status), stream=errors)
            return start_response(status, headers, *args)

        return self.__application(environ, _start_response)


session_opts = {
    "session.type": "file",
    "session.data_dir": "./api/session_data",
    "session.auto": True,
}

app2 = LoggingMiddleware(application2)
application = SessionMiddleware(app2, session_opts)

