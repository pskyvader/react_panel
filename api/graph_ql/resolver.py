
cache_models={}


def resolve(args, info, table_schema, table_model, **kwargs):
    query = table_schema.get_query(info=info)
    model=get_model(table_model)
    for c,filter_column in model.items():
        filter_value = kwargs.get(c, None)
        if filter_value != None:
            query = query.filter( filter_column == filter_value)
    return query

def get_model(table_model):
    name=table_model.__table__.name
    if name not in cache_models:
        columns = table_model.__table__.columns.keys()
        cache_models[name]={}
        for c in columns:
            filter_column=getattr(table_model,c)
            cache_models[name][c]=filter_column
    else:
        print('already',name)
    return cache_models[name]