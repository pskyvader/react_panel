def init(self,params):
    if len(params)==0:
        return self.get()
    else:
        if len(params)==1:
            return self.get(params[0])
        else:
            if params[1]=='get':
                return self.get(params[0],params[:2])
            elif params[1]=='post':
                return self.post(params[0],params[:2])
            elif params[1]=='put':
                return self.put(params[0],params[:2])
            elif params[1]=='delete':
                return self.delete(params[0],params[:2])
                

def get(self,id=0,**params):
    return {}

def post(self,id,**params):
    return {}
    
    
def put(self,id,**params):
    return {}
    
def delete(self,id,**params):
    return {}
    