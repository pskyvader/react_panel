import sys
import os
from core.app import app
from beaker.middleware import SessionMiddleware
import json
from gzip import compress


sys.path.insert(0, os.path.dirname(__file__))


def application2(environ, start_response):
    # from datetime import datetime
    # init_time = datetime.now()

    app_web = app(os.path.dirname(__file__))
    main_data = app_web.init(environ)
    ret = main_data["response_body"]

    if not isinstance(ret,str):
        ret=json.dumps(ret)

    if isinstance(ret, str):
        if ret != "":
            ret = compress(bytes(ret, "utf-8"))
            main_data["headers"].append(("Accept-encoding", "gzip,deflate"))
            main_data["headers"].append(("Content-Encoding", "gzip"))
        else:
            ret = b""


    start_response(main_data["status"], main_data["headers"])
    return [ret]



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
    "session.data_dir": "./session_data",
    "session.auto": True,
}

app2 = LoggingMiddleware(application2)
application = SessionMiddleware(app2, session_opts)

