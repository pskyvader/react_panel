def init(method,params):
    if len(params)>1:
        options=set(params[1:])
    else:
        options=()
    if method=='GET':
        if len(params)>0:
            return get(params[0],options)
        else:
            return get()
    elif len(params)>0:
        if method=='POST':
            return post(params[0],options)
        elif method=='PUT':
            return put(params[0],options)
        elif method=='DELETE':
            return delete(params[0],options)
    else:
        return {'error':404,'method':method,'params':params}
                

def get(id=0,**params):
    return {}

def post(id,**params):
    return {}
    
    
def put(id,**params):
    return {}
    
def delete(id,**params):
    return {}
    