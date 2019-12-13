from core.image import image

class base:
    model=None
    @classmethod
    def init(cls,method,params,model):
        cls.model=model
        if len(params)>1:
            options=tuple(params[1:])
        else:
            options=()
        if method=='GET':
            if len(params)>0:
                return cls.get(int(params[0]),*options)
            else:
                return cls.get()
        elif len(params)>0:
            if method=='POST':
                return cls.post(int(params[0]),*options)
            elif method=='PUT':
                return cls.put(int(params[0]),*options)
            elif method=='DELETE':
                return cls.delete(int(params[0]),*options)
        else:
            return {'error':404,'method':method,'params':params}



    @classmethod
    def get(cls, id=0, *options):
        if id == 0:
            data = cls.model.getAll()
            if len(data)>0 and 'foto' in data[0]:
                recortes=image.get_recortes(cls.model.__name__)
                recortes=[x['tag'] for x in recortes]
                for d in data:
                    d['foto']=cls.process_image(d['foto'],options,recortes)
        else:
            data = cls.model.getById(id)
            if 'foto' in data:
                recortes=image.get_recortes(cls.model.__name__)
                recortes=[x['tag'] for x in recortes]
                data['foto']=cls.process_image(data['foto'],options,recortes)
        return {"body": data}
        
    def post(self,id,*params):
        return {'body':{}}
        
    def put(self,id,*params):
        return {'body':{}}
        
    def delete(self,id,*params):
        return {'body':{}}



        
    @classmethod
    def process_image(cls,images,options,recortes):
        url_list=[]
        if "portada" in options:
            portada = image.portada(images)
            if len(options)>1:
                if options[1] in recortes:
                    url_list=[(options[1],image.generar_url(portada, options[1]))]
            else:
                for recorte in recortes:
                    url_list.append((recorte,image.generar_url(portada, recorte)))
        elif len(options)>0:
            if options[1] in recortes:
                for i in images:
                    url_list.append((recorte,image.generar_url(i, options[1])))
        else:
            for i in images:
                for recorte in recortes:
                    url_list.append((recorte,image.generar_url(i, recorte)))
        return url_list