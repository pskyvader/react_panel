import graphene
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
    tag=graphene.String()
    url=graphene.String()
    def __init__(self, image_origin, recorte):
        print(image_origin.table_name,image_origin.idparent,image_origin.name,image_origin.extension)
        from .utils.image import recortar_foto
        if image_origin.table_name != None and image_origin.idparent != None:
            if recorte['width'] != None or recorte['height'] != None:
                if recorte['width'] == None:
                    recorte['width'] = 0
                if recorte['height'] == None:
                    recorte['height'] = 0
                recorte['tag']=f"{recorte['width']}x{recorte['height']}"
            else:
                recorte['tag']='original'
            if recorte['format'] != None:
                recorte["format"] = recorte['format']
            else:
                recorte["format"] = ""

            recorte["folder"]= f"{image_origin.table_name}/{image_origin.idparent}/{image_origin.idimage}/"

            response=recortar_foto(recorte, image_origin)
            if response['exito']!=True:
                raise Exception(response['mensaje'])
            else:
                self.tag= recorte['tag'],
                self.url=response["url"],
        else:
            self.tag= "tmp"
            self.url=f"tmp/{image_origin.idimage}/{image_origin.name}.{image_origin.extension}"