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
        parts = sort_value.split(" ")
        if len(parts)!=2:
            raise NameError("Invalid sort", parts,"valid: ASC|DESC")
        else:
            value, pos=parts

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