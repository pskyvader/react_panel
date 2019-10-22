def init(self,method,params):
    if method=='GET':
        return self.get(params[0],params[1:])
    elif len(params)>0:
        if method=='POST':
            return self.post(params[0],params[1:])
        elif method=='PUT':
            return self.put(params[0],params[1:])
        elif method=='DELETE':
            return self.delete(params[0],params[1:])
    else:
        return {'error':404,'method':method,'params':params}
                

def get(self,id=0,**params):
    return {}

def post(self,id,**params):
    return {}
    
    
def put(self,id,**params):
    return {}
    
def delete(self,id,**params):
    return {}
    