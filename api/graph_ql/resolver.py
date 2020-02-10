import graphene
from .utils.image import recortar_foto
from os.path import join
from urllib.request import pathname2url

cache_models = {}


def resolve(args, info, table_schema, table_model, **kwargs):
    query = table_schema.get_query(info=info)
    model = get_model(table_model)
    for c, filter_column in model.items():
        filter_value = kwargs.get(c, None)
        if filter_value != None:
            query = query.filter(filter_column == filter_value)

    sort_value = kwargs.get("sort", None)
    if sort_value != None:
        value, pos = sort_value.split(" ")
        if value in model:
            if pos.lower() in ["asc", "desc"]:
                query = query.order_by(getattr(model[value], pos.lower())())
            else:
                raise NameError("Invalid sort", pos)
        else:
            raise NameError("Field not found", value)
    return query


def get_model(table_model):
    name = table_model.__table__.name
    if name not in cache_models:
        columns = table_model.__table__.columns.keys()
        cache_models[name] = {}
        for c in columns:
            filter_column = getattr(table_model, c)
            cache_models[name][c] = filter_column
    return cache_models[name]


class Url(graphene.ObjectType):
    tag = graphene.String()
    url = graphene.String()

    def __init__(self, image_origin, recorte):
        if image_origin.table_name != None and image_origin.idparent != None:
            size_filter=(None,0,"","0")
            
            if recorte["width"] not in size_filter or recorte["height"] not in size_filter:
                if recorte["width"] in size_filter:
                    recorte["width"] = 0
                if recorte["height"] in size_filter:
                    recorte["height"] = 0

                recorte["tag"] = f"{recorte['width']}x{recorte['height']}"
            else:
                recorte["width"] = 0
                recorte["height"] = 0
                recorte["tag"] = image_origin.name

            if recorte["format"] == None:
                recorte["format"] = image_origin.extension

            recorte["folder"] = join( image_origin.table_name, str(image_origin.idparent), str(image_origin.field_name), str(image_origin.idimage) )

            response = recortar_foto(recorte, image_origin)
            if not response["exito"]:
                raise Exception(response["mensaje"])
            else:
                self.tag = recorte["tag"]
                self.url = response["url"]
        else:
            self.tag = "tmp"
            self.url = join( "tmp", str(image_origin.idimage), image_origin.name + "." + image_origin.extension, )


        self.url=pathname2url(self.url)


