class base:
    model=None
    def init(self,method,params,model):
        self.model=model
        if len(params)>1:
            options=set(params[1:])
        else:
            options=()
        if method=='GET':
            if len(params)>0:
                return self.get(params[0],options)
            else:
                return self.get()
        elif len(params)>0:
            if method=='POST':
                return self.post(params[0],options)
            elif method=='PUT':
                return self.put(params[0],options)
            elif method=='DELETE':
                return self.delete(params[0],options)
        else:
            return {'error':404,'method':method,'params':params}
