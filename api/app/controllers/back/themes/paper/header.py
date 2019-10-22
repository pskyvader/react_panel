from core.functions import functions
from core.app import app
from core.image import image
from app.models.logo import logo as logo_model
from .base import base
import json


class header(base):
    data = {"logo": "", "url_exit": ""}
    def index(self):
        return self.get()
        
    def get(self):
        logo = logo_model.getById(3)
        portada = image.portada(logo["foto"])
        self.data["logo_max"] = image.generar_url(portada, "panel_max")
        logo = logo_model.getById(4)
        portada = image.portada(logo["foto"])
        self.data["logo_min"] = image.generar_url(portada, "panel_min")
        self.data["url_exit"] = functions.generar_url(["logout"], False)
        self.data["date"] = functions.current_time()
        return {"body":self.data}
