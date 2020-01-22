from .database import db_session,encript
# from graphql_relay.node.node import from_global_id


def input_to_dictionary(input_variable):
    """Method to convert Graphene input_variables into dictionary"""
    dictionary = {}
    for key in input_variable:
        # Convert GraphQL global id to database id
        # if key[-2:] == 'id':
            # input_variable[key] = from_global_id(input_variable[key])[1]
        if key=='password':
            dictionary[key] = encript(input_variable[key])
        else:
            dictionary[key] = input_variable[key]
    return dictionary
    

def mutation_create(table_model,input,id_key,info):
    data = input_to_dictionary(input)
    table = table_model(**data)
    db_session.add(table)
    db_session.commit()
    if info.context.FILES!=None:
        data=process_file(data,id_key,info.context.FILES)
        if data!=None:
            filter_id=getattr(table_model,id_key)
            table = db_session.query(table_model).filter(filter_id==getattr(table,id_key))
            table.update(data)
    return table


def mutation_update(table_model,input,id_key,info):
    data = input_to_dictionary(input)
    filter_id=getattr(table_model,id_key)
    table = db_session.query(table_model).filter(filter_id==data[id_key])
    table.update(data)
    db_session.commit()
    if info.context.FILES!=None:
        data=process_file(data,id_key,info.context.FILES)
        if data!=None:
            table.update(data)
    table = db_session.query(table_model).filter(filter_id==data[id_key]).first()
    return table


def mutation_delete(table_model,input,id_key):
    data = input_to_dictionary(input)
    filter_id=getattr(table_model,id_key)
    table = db_session.query(table_model).filter(filter_id==data[id_key]).first()
    if table!=None:
        db_session.delete(table)
        db_session.commit()
        return (True,'Delete correctly')
    else:
        return (False,id_key+' '+ data[id_key] +" Doesn't exists")


def process_file(data,id_key,files):
    from .utils import image
    from os.path import join
    if id_key=='idimage' and len(files)==1:
        f=files[0]
        folder="tmp"
        name=""
        if 'table' in data and 'idparent' in data and 'idimage' in data:
            folder=join(data['table'],str(data['idparent']),str(data['idimage']))
            name="original"
        archivo = image.upload(f, folder,name)
        data['name']=archivo['name']
        data['extension']=archivo['extension']
        print(archivo)
        return data
    return None