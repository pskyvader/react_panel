from .base import base
from app.models.logo import logo as logo_model

def init(method,params):
    l=logo()
    return l.init(method,params,logo_model)

class logo(base):
    @classmethod
    def get(cls,id=0,*options):
        if id==0:
            data=cls.model.getAll()
        else:
            data=cls.model.getById(id)
        return {'body':data}
    @classmethod
    def post(cls,id,*options):
        return {'body':{}}
        
    @classmethod
    def put(cls,id,*options):
        return {'body':{}}
    @classmethod
    def delete(cls,id,*options):
        return {'body':{}}


