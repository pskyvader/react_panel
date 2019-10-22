from core.functions import functions
from core.app import app
from core.image import image
from app.models.logo import logo as logo_model
import json


class header:
    data = {"logo": "", "url_exit": ""}

    def init(self, var: list):
        from inspect import signature
        import inspect

        if len(var) == 0:
            var = ["index"]

        if hasattr(self, var[0]) and callable(getattr(self, var[0])):
            fun = var[0]
            del var[0]
            method = getattr(self, fun)
            sig = signature(method)
            params = sig.parameters
            if "self" in params:
                if "var" in params:
                    ret = method(self, var=var)
                else:
                    ret = method(self)
            else:
                if "var" in params:
                    ret = method(var=var)
                else:
                    ret = method()
        else:
            ret = {"error": 404}
        return ret

    def get(self):
        ret = {
            "headers": [("Content-Type", "application/json; charset=utf-8")],
            "body": "",
        }
        logo = logo_model.getById(3)
        portada = image.portada(logo["foto"])
        self.data["logo_max"] = image.generar_url(portada, "panel_max")
        logo = logo_model.getById(4)
        portada = image.portada(logo["foto"])
        self.data["logo_min"] = image.generar_url(portada, "panel_min")
        self.data["url_exit"] = functions.generar_url(["logout"], False)
        self.data["date"] = functions.current_time()
        ret["body"] = json.dumps(self.data, ensure_ascii=False)
        return ret
