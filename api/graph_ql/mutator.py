from .database import db_session,encript
from graphql_relay.node.node import from_global_id

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
    if info.context.FILES!=None:
        data=process_file(data,id_key,info.context.FILES)
    table = table_model(**data)
    db_session.add(table)
    db_session.commit()
    return table


def mutation_update(table_model,input,id_key,info):
    data = input_to_dictionary(input)
    if info.context.FILES!=None:
        data=process_file(data,id_key,info.context.FILES)
    filter_id=getattr(table_model,id_key)
    table = db_session.query(table_model).filter(filter_id==data[id_key])
    table.update(data)
    db_session.commit()
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
    for f in files:
        print(f)
    return data