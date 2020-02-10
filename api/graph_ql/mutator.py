from .database import db_session, encript
from .utils.image import delete, delete_temp,upload
from os.path import join

# from graphql_relay.node.node import from_global_id


def input_to_dictionary(input_variable):
    """Method to convert Graphene input_variables into dictionary"""
    dictionary = {}
    for key in input_variable:
        # Convert GraphQL global id to database id
        # if key[-2:] == 'id':
        # input_variable[key] = from_global_id(input_variable[key])[1]
        if key == "password":
            dictionary[key] = encript(input_variable[key])
        else:
            dictionary[key] = input_variable[key]
    return dictionary


def mutation_create(table_model, input, id_key, info):
    data = input_to_dictionary(input)
    table = table_model(**data)
    db_session.add(table)
    db_session.commit()
    if info.context.FILES != None:
        data[id_key] = getattr(table, id_key)
        data = process_file(data, id_key, info.context.FILES)
        if data != None:
            filter_id = getattr(table_model, id_key)
            table = db_session.query(table_model).filter(filter_id == data[id_key])
            if "exito" in data and not data["exito"]:
                db_session.delete(table.first())
                db_session.commit()
                raise Exception(data["mensaje"])
            else:
                table.update(data)
                db_session.commit()
                table = (
                    db_session.query(table_model)
                    .filter(filter_id == data[id_key])
                    .first()
                )
    return table


def mutation_update(table_model, input, id_key, info):
    data = input_to_dictionary(input)
    if info.context.FILES != None:
        data = process_file(data, id_key, info.context.FILES)
        if "exito" in data and not data["exito"]:
            raise Exception(data["mensaje"])

    filter_id = getattr(table_model, id_key)
    table = db_session.query(table_model).filter(filter_id == data[id_key])
    table.update(data)
    db_session.commit()
    table = db_session.query(table_model).filter(filter_id == data[id_key]).first()
    return table


def mutation_delete(table_model, input, id_key):
    data = input_to_dictionary(input)
    filter_id = getattr(table_model, id_key)
    table = db_session.query(table_model).filter(filter_id == data[id_key]).first()
    if table != None:
        if id_key == "idimage":
            if table.table_name != None and table.idparent != None:
                folder = join(table.table_name, str(table.idparent), str(table.field_name), str(table.idimage))
            else:
                folder = join("tmp", str(table.idimage), table.name + "." + table.extension)
            print(delete( folder, keep_original=False, original_file=table.name + "." + table.extension, ))
        db_session.delete(table)
        db_session.commit()
        return (True, "Delete correctly")
    else:
        return (False, id_key + " " + data[id_key] + " Doesn't exists")


def process_file(data, id_key, files):
    if id_key == "idimage" and len(files) == 1:
        f = files[0]
        folder = "tmp"
        name = ""
        if "table_name" in data and "idparent" in data and "field_name" in data and "idimage" in data:
            folder = join(
                data["table_name"], str(data["idparent"]), str(data["field_name"]), str(data["idimage"])
            )
            name = "original"
        respuesta = upload(f, folder, name)
        delete_temp()
        if respuesta["exito"]:
            data["name"] = respuesta["name"]
            data["extension"] = respuesta["extension"]
            return data
        else:
            return respuesta
    elif len(files) > 1:
        raise Exception("You can only parse 1 file at the time, and only in image table")

    return None
