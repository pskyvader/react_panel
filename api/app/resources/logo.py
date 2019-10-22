from .base import base
from app.models.logo import logo

def init(method,params):
    l=logo()
    return l.init(method,params,logo)

class logo(base):
    def get(self,id=0,**params):

        return {'body':{'asdf':'sfd'}}

    def post(self,id,**params):
        return {'body':{}}
        
        
    def put(self,id,**params):
        return {'body':{}}
        
    def delete(self,id,**params):
        return {'body':{}}


