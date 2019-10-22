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
        from .cache import cache
        from .functions import functions
        from .database import database

        # from datetime import datetime
        # init_time = datetime.now()

        app.environ = environ
        data_return = {}
        app.get = parse_get(app.environ["QUERY_STRING"])
        app.post = parse_post(app.environ)
        app.session = app.environ["beaker.session"]
        app.client_ip =parse_ip(app.environ)
        config = self.get_config()
        url =parse_url(environ["PATH_INFO"],config)

        app.title = config["title"]
        app.prefix_site = functions.url_amigable(app.title)

        #app.root_url = environ["SERVER_NAME"].replace("www.", "")
        app.root_url = environ["HTTP_HOST"].replace("www.", "")
        subdirectorio = config["dir"]
        https = "https://" if config["https"] else "http://"
        www = "www." if config["www"] else ""
        port = environ["SERVER_PORT"]
        if port != '80' and port not in app.root_url:
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

        file_cache = cache.get_cache()
        if file_cache != "":
            response = {
                "file": file_cache,
                "is_file": True,
                "body": "",
                "headers": [
                    ("Content-Type", "text/html charset=utf-8"),
                    ("Accept-encoding", "gzip,deflate"),
                    ("Content-Encoding", "gzip"),
                ],
            }
        else:
            controller = app.controller_dir + url[0]
            my_file = Path(app.root + controller + ".py")
            if my_file.is_file():
                current_module = importlib.import_module(controller.replace("/", "."))
                current_module = getattr(current_module, url[0])
                current_module = current_module()
                del url[0]
                # returns {'body':[],'headers':str} or {'error':int,...'redirect':str}
                response = current_module.init(url.copy())
            else:
                response = {"error": 404}

        if "headers" not in response:
            # response["headers"] = [("Content-Type", "text/html charset=utf-8")]
            response["headers"] = [("Content-Type", "application/json; charset=utf-8")]

        if "error" in response:
            response['body']=response
            
        data_return["status"] = "200 OK"

        if "is_file" in response:
            data_return["is_file"] = response["is_file"]
        if "file" in response:
            data_return["file"] = response["file"]

        # if data_return['status']=='200 OK':
        # print('antes de render', (datetime.now()-init_time).total_seconds()*1000)
        # init_time=datetime.now()

        if isinstance(response["body"], list):
            data_return["response_body"] = response["body"]
            cache.save_cache()
        else:
            data_return["response_body"] = response["body"]

        data_return["headers"] = response["headers"]
        for cookie in functions.cookies:
            data_return["headers"].append(("Set-Cookie", cookie))
        # if data_return['status']=='200 OK':
        # print('despues de render', (datetime.now()-init_time).total_seconds()*1000)
        database.close()
        return data_return



    @staticmethod
    def get_config():
        if len(app.config) == 0:
            with open(app.root + app.app_dir + "config/config.json") as f:
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

