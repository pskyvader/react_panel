from .base import base
from app.models.logo import logo as logo_model
from core.image import image


def init(method, params):
    l = logo()
    return l.init(method, params, logo_model)


class logo(base):
    @classmethod
    def get(cls, id=0, *options):
        if id == 0:
            data = cls.model.getAll()
        else:
            data = cls.model.getById(id)
            if 'foto' in data:
                data['foto']=cls.process_image(data['foto'],options)
        return {"body": data}
    @classmethod
    def process_image(cls,images,options):
        recortes=image.get_recortes(cls.model.__name__)
        print(recortes)
        recortes=[x['tag'] for x in recortes]

        url_list=[]
        if "portada" in options:
            portada = image.portada(images)
            if len(options)>1:
                if options[1] in recortes:
                    url_list=[image.generar_url(portada, options[1])]
            else:
                for recorte in recortes:
                    url_list.append(image.generar_url(portada, recorte))
        elif len(options)>0:
            if options[1] in recortes:
                for i in images:
                    url_list.append(image.generar_url(i, options[1]))
        else:
            for i in images:
                for recorte in recortes:
                    url_list.append(image.generar_url(i, recorte))
        return url_list

    @classmethod
    def post(cls, id, *options):
        return {"body": {}}

    @classmethod
    def put(cls, id, *options):
        return {"body": {}}

    @classmethod
    def delete(cls, id, *options):
        return {"body": {}}

