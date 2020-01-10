import json
from os.path import join, dirname, isfile
import sys

current_dir = dirname(__file__)

sys.path.append(join(current_dir, ".."))
sys.path.append(join(current_dir, "..", "python-library"))

config_file = join(current_dir, "..", "config", "config.json")
config = {}
with open(config_file) as f:
    config = json.load(f)

bdd_dir = join(current_dir, "..", "config", "bdd")
model_dir = join(current_dir, "..", "graph_ql", "model")
schemas_dir = join(current_dir, "..", "graph_ql", "schemas")

types = {
    "char(255)": {
        "text": "Texto",
        "value": "char(255)",
        "graphene_type": "graphene.String()",
        "alchemy_type": "Column(String(255), nullable=False)",
    },
    "int(11)": {
        "text": "Numero",
        "value": "int(11)",
        "graphene_type": "graphene.Int()",
        "alchemy_type": "Column(Integer, nullable=False)",
    },
    "tinyint(1)": {
        "text": "Bool",
        "value": "tinyint(1)",
        "graphene_type": "graphene.Boolean()",
        "alchemy_type": "Column(Boolean, nullable=False)",
    },
    "longtext": {
        "text": "Texto largo",
        "value": "longtext",
        "graphene_type": "graphene.String()",
        "alchemy_type": "Column(Text, nullable=False)",
    },
    "datetime": {
        "text": "Fecha y hora",
        "value": "datetime",
        "graphene_type": "graphene.types.datetime.DateTime()",
        "alchemy_type": "Column(DateTime, nullable=False)",
    },
    "json": {
        "text": "Campo JSON (archivos o imagenes)",
        "value": "json",
        "graphene_type": "graphene.JSONString()",
        "alchemy_type": "Column(JSON, nullable=False)",
    },
    "id": {
        "text": "Campo primario",
        "value": "int(11)",
        "graphene_type": "graphene.NonNull(graphene.ID)",
        "alchemy_type": "Column(Integer, primary_key=True, nullable=False)",
    },
}

black_list = ["password"]


file_cache = {}


def bdd_to_folder():
    file_str = bdd_dir + "bdd.json"
    try:
        with open(file_str, "r") as file1:
            tables = json.loads(file1.read())
            for t in tables:
                tablename = bdd_dir + t["tablename"] + ".json"
                with open(tablename, "w") as table:
                    table.write(json.dumps(t))
                    print("table", tablename, "created")
    except FileNotFoundError as e:
        print("archivo", file_str, "no existe", e)


def json_to_class(tablename, return_class=True):
    template = get_file(join(current_dir, "template_graphene.py"))
    table = json.loads(get_file(join(bdd_dir, tablename)))
    template = template.replace("TABLENAME", table["tablename"])
    template = template.replace("IDNAME", table["idname"])
    template = template.replace("PREFIX", config["prefix"])

    fields = ""
    for field in table["fields"]:
        str_field = field["titulo"] + "=" + types[field["tipo"]]["alchemy_type"]
        fields += str_field + "\n    "

    template = template.replace("FIELDS", fields)
    if return_class:
        return template


def json_to_model():
    json_files = file_list(bdd_dir)
    model_classes = ""
    for f in json_files:
        model_classes += json_to_class(f, return_class=True)+"\n"

    model_file = join(current_dir, "..", "graph_ql", "models.py")

    if replace_in_file(model_file, "# __MODELS__", "\n"+model_classes+ "\n"):
        print("Modelos creados correctamente!")
    else:
        print("Error al crear los modelos!")


def json_to_schema(force=False):
    json_files = file_list(bdd_dir)
    template_file = get_file(join(current_dir, "template_schema.py"))

    for f in json_files:
        template = template_file
        table = json.loads(get_file(join(bdd_dir, f)))

        f = f.replace(".json", "")
        template = template.replace("TABLENAME", f)
        fields = [
            field for field in table["fields"] if field["titulo"] not in black_list
        ]
        fields_str = ""
        for field in fields:
            if field["tipo"] != "json":
                fields_str += (
                    field["titulo"] + "=" + types[field["tipo"]]["graphene_type"] + "\n    "
                )
        template = template.replace("EXTRA_FIELDS_BREAK_LINE", fields_str[:-1])

        
        fields_str = ""
        for field in fields:
            if field["tipo"] != "json":
                fields_str += (
                    field["titulo"] + "=" + types[field["tipo"]]["graphene_type"] + ","
                )
        template = template.replace("EXTRA_FIELDS", fields_str[:-1])


        fields_str = ""
        for field in fields:
            fields_str += "'" + field["titulo"] + "',"
        template = template.replace("ONLY_FIELDS", fields_str[:-1])

        schema_file = join(schemas_dir, f + "_schema.py")
        if not force and isfile(schema_file):
            print("El archivo ", schema_file, " Existe, saltando...")
        else:
            if create_file(schema_file, template,force):
                print("schema creado correctamente!", schema_file)
            else:
                print("Error al crear el schema!", schema_file)


def json_to_query():
    json_files = file_list(bdd_dir)
    template = get_file(join(current_dir, "template_query.py"))

    method_classes = ""
    for f in json_files:
        f = f.replace(".json", "")
        method_classes += "\n    " + (template.replace("TABLENAME", f)) + "\n    "

    method_file = join(current_dir, "..", "graph_ql", "schema.py")
    if replace_in_file(method_file, "# __QUERY__", method_classes + "\n"):
        print("metodos creados correctamente!")
    else:
        print("Error al crear los metodos!")



def json_to_mutation():
    json_files = file_list(bdd_dir)
    template = get_file(join(current_dir, "template_mutation.py"))

    method_classes = ""
    for f in json_files:
        f = f.replace(".json", "")
        method_classes += "\n    " + (template.replace("TABLENAME", f)) + "\n    "

    method_file = join(current_dir, "..", "graph_ql", "schema.py")
    if replace_in_file(method_file, "# __MUTATION__", method_classes + "\n"):
        print("metodos creados correctamente!")
    else:
        print("Error al crear los metodos!")



def json_to_types():
    json_files = file_list(bdd_dir)
    template = "schema = graphene.Schema(query=Query,mutation=Mutation, types=[TYPES])"
    type_classes = ""
    type_str = ""
    for f in json_files:
        f = f.replace(".json", "")
        type_str += f + "_schema." + f + "_schema,"

    type_classes = template.replace("TYPES", type_str)

    type_file = join(current_dir, "..", "graph_ql", "schema.py")
    if replace_in_file(type_file, "# __TYPES__", "\n" + type_classes + "\n"):
        print("types creados correctamente!")
    else:
        print("Error al crear los types!")


def json_to_init():
    json_files = file_list(bdd_dir)
    template = '__all__ = [INIT]'
    type_classes = ""
    type_str = ""
    for f in json_files:
        f = f.replace(".json", "")
        type_str +='"'+ f + '_schema",'

    type_classes = template.replace("INIT", type_str[:-1])

    init_file = join(current_dir, "..", "graph_ql", "schemas",'__init__.py')
    if replace_in_file(init_file, "# __INIT__", "\n" + type_classes + "\n"):
        print("Init creados correctamente!")
    else:
        print("Error al crear los Init!")






def get_file(file_name):
    if file_name in file_cache:
        return file_cache[file_name]
    else:
        with open(file_name, "r") as tpl:
            file = tpl.read()
        file_cache[file_name] = file
        return file


def file_list(directory):
    from os import listdir

    files = [f for f in listdir(directory) if isfile(join(directory, f))]
    return files


def replace_in_file(file_name, tag, content):
    with open(file_name, "a+") as tmp:
        tmp.seek(0)
        temp_file = tmp.read()
    parts = temp_file.split(tag)
    if len(parts) != 3:
        raise KeyError(
            tag + " Not found (must be only 2 tags with this name in file)" + file_name,
            len(parts),
        )
    else:
        with open(file_name, "w") as class_table:
            class_table.write(parts[0])
            class_table.write(tag + "\n    ")
            class_table.write(content)
            class_table.write(tag + "\n    ")
            class_table.write(parts[2])
            return True
    return False


def create_file(file_name, content,force=False):
    if isfile(file_name) and not force:
        raise FileExistsError(file_name + " Already exists")
    else:
        with open(file_name, "w") as class_table:
            class_table.write(content)
            return True
    return False


# bdd_to_folder()
json_to_model()
json_to_schema(force=True)
json_to_query()
json_to_mutation()
json_to_types()
json_to_init()
