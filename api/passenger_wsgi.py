import sys
import os
from core.app import app
from beaker.middleware import SessionMiddleware


sys.path.insert(0, os.path.dirname(__file__))


def application2(environ, start_response):

    app_web = app(os.path.dirname(__file__))
    main_data = app_web.init(environ)
    ret = main_data["response_body"]

    if isinstance(ret, str):
        if ret != "":
            ret = bytes(ret, "utf-8")
            from gzip import compress

            ret = compress(ret)
            main_data["headers"].append(("Accept-encoding", "gzip,deflate"))
            main_data["headers"].append(("Content-Encoding", "gzip"))
        else:
            ret = b""

    start_response(main_data["status"], main_data["headers"])
    if "is_file" in main_data and main_data["is_file"]:
        f = open(main_data["file"], "rb")
        if "wsgi.file_wrapper" in environ:
            return environ["wsgi.file_wrapper"](f, 1024)
        else:
            # print('no filewrapper')
            return file_wrapper(f, 1024)
    else:
        return [ret]



session_opts = {
    "session.type": "file",
    "session.data_dir": "./session_data",
    "session.auto": True,
}

application = SessionMiddleware(application2, session_opts)

