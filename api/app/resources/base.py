class base:
    model=None
    @classmethod
    def init(cls,method,params,model):
        cls.model=model
        if len(params)>1:
            options=set(params[1:])
        else:
            options=()
        if method=='GET':
            if len(params)>0:
                return cls.get(params[0])
            else:
                return cls.get()
        elif len(params)>0:
            if method=='POST':
                return cls.post(params[0],options)
            elif method=='PUT':
                return cls.put(params[0],options)
            elif method=='DELETE':
                return cls.delete(params[0],options)
        else:
            return {'error':404,'method':method,'params':params}

    @classmethod 
    def get(cls,id=0,**params):
        return {'body':{}}
    @classmethod
    def post(cls,id,**params):
        return {'body':{}}
        
    @classmethod
    def put(cls,id,**params):
        return {'body':{}}
    @classmethod
    def delete(cls,id,**params):
        return {'body':{}}