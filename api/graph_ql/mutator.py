def input_to_dictionary(input_variable,id_key):
    """Method to convert Graphene input_variables into dictionary"""
    dictionary = {}
    for key in input_variable:
        # Convert GraphQL global id to database id
        if key[-2:] == id_key:
            input_variable[key] = from_global_id(input_variable[key])[1]
        dictionary[key] = input_variable[key]
    return dictionary

def mutation_create(table_model):
    data = utils.input_to_dictionary(input)
    table = table_model(**data)
    db_session.add(table)
    db_session.commit()
    return table