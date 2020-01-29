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


def Url(image_origin, recorte):
    from .utils import image
    if image_origin.table_name != None and image_origin.idparent != None:
        if width != None or heigth != None:
            if width == None:
                width = 0
            if heigth == None:
                heigth = 0
            image_origin.name = f"{width}x{heigth}"
            recorte['tag']=image_origin.name
        if extension != None:
            image_origin.extension = extension

        recorte["url"]= f"{image_origin.table_name}/{image_origin.idparent}/{image_origin.idimage}/{image_origin.name}.{image_origin.extension}"

        foto = {
            "tag": recorte['tag'],
            "url": recorte["url"],
        }
        image.recortar_foto(recorte, datos)
    else:
        foto = {
            "tag": "tmp",
            "url": f"tmp/{image_origin.idimage}/{image_origin.name}.{image_origin.extension}",
        }
    return foto
