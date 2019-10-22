from .base import base
from app.models.logo import logo

def init(method,params):
    l=logo()
    return l.init(method,params,logo)

class logo(base):
    def get(self,id=0,**params):
        if id==0:
            data=self.model.getAll()
        else:
            data=self.model.getById(id)
        return {'body':data}

    def post(self,id,**params):
        return {'body':{}}
        
        
    def put(self,id,**params):
        return {'body':{}}
        
    def delete(self,id,**params):
        return {'body':{}}


