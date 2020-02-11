import sys
import os
import json
from pathlib import Path
import importlib
from .format import *


class app:
    config = {}
    app_dir = "app/"
    controller_dir = app_dir + "controllers/"
    resource_dir = app_dir + "resources/"
    title = ""
    prefix_site = ""
    url = {}
    front = True
    path = ""
    root = "api/"
    environ = {}
    get = {}
    root_url = ""
    client_ip = ""
    idseo = 0

    def __init__(self, root):
        import locale
        try:
            locale.setlocale(locale.LC_ALL, "es_CL.UTF-8")
        except:
            pass
        app.root = root + "/"

    def init(self, environ):
        from .functions import functions
        from .database import database

        app.environ = environ
        data_return = {}
        app.method=app.environ["REQUEST_METHOD"]
        app.get = parse_get(app.environ["QUERY_STRING"])
        app.post = parse_post(app.environ)
        # app.session = app.environ["beaker.session"]
        app.client_ip = parse_ip(app.environ)
        config = self.get_config()
        url,app.idseo = parse_url(environ["PATH_INFO"], config)

        app.title = config["title"]
        app.prefix_site = functions.url_amigable(app.title)

        # app.root_url = environ["SERVER_NAME"].replace("www.", "")
        app.root_url = environ["HTTP_HOST"].replace("www.", "")
        subdirectorio = config["dir"]
        https = "https://" if config["https"] else "http://"
        www = "www." if config["www"] else ""
        port = environ["SERVER_PORT"]
        if port != "80" and port not in app.root_url:
            app.root_url += ":" + port

        app.path = https + www + app.root_url + "/"
        if subdirectorio != "":
            app.path += subdirectorio + "/"
            subdirectorio = "/" + subdirectorio + "/"
        else:
            subdirectorio = "/"

        if url[0] == config["admin"]:
            app.front = False
            del url[0]
            if len(url) == 0:
                url = ["home"]
        else:
            app.front = True

        app.url["base"] = app.path
        app.url["admin"] = app.path + config["admin"] + "/"

        app.url["base_dir"] = app.root
        app.url["admin_dir"] = app.root + config["admin"] + "/"

        app.url["base_sub"] = subdirectorio
        app.url["admin_sub"] = subdirectorio + config["admin"] + "/"

        if app.front:
            app.controller_dir = ( app.app_dir + "controllers/front/themes/" + config["theme"] + "/" )
        else:
            app.path = app.url["admin"]
            app.controller_dir = ( app.app_dir + "controllers/" + "back/themes/" + config["theme_back"] + "/" )

        resource = app.resource_dir + url[0]
        my_file = Path(app.root + resource + ".py")
        if my_file.is_file():
            current_module = importlib.import_module(resource.replace("/", "."))
            response = current_module.init(app.method,url[1:])
        else:
            response = {"error": 404}

        if "headers" not in response:
            # response["headers"] = [("Content-Type", "text/html charset=utf-8")]
            response["headers"] = [("Content-Type", "application/json; charset=utf-8")]

        if "error" in response:
            if response["error"] == 301:
                response["body"] = {
                    "error": response["error"],
                    "location": response["redirect"],
                    "status": "301 Moved Permanently",
                }
            else:
                response["body"] = {
                    "error": response["error"],
                    "status": "404 Not Found",
                }
                if config["debug"]:
                    if 'params' in response:
                        response["body"]["params"]= response["params"]
                    response["body"]["endpoint"] = str(my_file)

        data_return["status"] = "200 OK"
        data_return["response_body"] = response["body"]
        data_return["headers"] = response["headers"]
        for cookie in functions.cookies:
            data_return["headers"].append(("Set-Cookie", cookie))

        database.close()
        return data_return

    @staticmethod
    def get_config():
        if len(app.config) == 0:
            with open(app.root + "config/config.json") as f:
                app.config = json.load(f)
        return app.config

    @staticmethod
    def get_dir(front=False):
        if app.front or front:
            return app.url["base_dir"]
        else:
            return app.url["admin_dir"]

    @staticmethod
    def get_url(front=False):
        if app.front or front:
            return app.url["base"]
        else:
            return app.url["admin"]

