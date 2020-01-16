from .database import db_session

def input_to_dictionary(input_variable,id_key):
    """Method to convert Graphene input_variables into dictionary"""
    dictionary = {}
    for key in input_variable:
        # Convert GraphQL global id to database id
        if key[-2:] == id_key:
            input_variable[key] = from_global_id(input_variable[key])[1]
        dictionary[key] = input_variable[key]
    return dictionary

def mutation_create(table_model,input,id_key):
    data = input_to_dictionary(input,id_key)
    table = table_model(**data)
    db_session.add(table)
    db_session.commit()
    return table


def mutation_update(table_model,input,id_key):
    data = input_to_dictionary(input,id_key)
    table = db_session.query(table_model).filter_by(id=data[id_key])
    table.update(data)
    db_session.commit()
    table = db_session.query(table_model).filter_by(id=data[id_key]).first()
    return table
