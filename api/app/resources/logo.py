from .base import base
from app.models.logo import logo as logo_model


def init(method, params):
    l = logo()
    return l.init(method, params, logo_model)


class logo(base):
