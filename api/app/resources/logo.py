from .base import base

def init(method,params):
    l=logo()
    return l.init(method,params)

class logo(base):
    def get(self,id=0,**params):
        return {'body':{'asdf'}}

    def post(self,id,**params):
        return {'body':{}}
        
        
    def put(self,id,**params):
        return {'body':{}}
        
    def delete(self,id,**params):
        return {'body':{}}


