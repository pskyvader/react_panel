import json
from os.path import join, dirname, isfile
import sys

current_dir = dirname(__file__)
sys.path.append(join(current_dir, ".."))


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
        "alchemy_type": "Column(String(255))",
    },
    "int(11)": {
        "text": "Numero",
        "value": "int(11)",
        "graphene_type": "graphene.Int()",
        "alchemy_type": "Column(Integer)",
    },
    "tinyint(1)": {
        "text": "Bool",
        "value": "tinyint(1)",
        "graphene_type": "graphene.Boolean()",
        "alchemy_type": "Column(Boolean, nullable=False, default=False)",
    },
    "longtext": {
        "text": "Texto largo",
        "value": "longtext",
        "graphene_type": "graphene.String()",
        "alchemy_type": "Column(Text)",
    },
    "datetime": {
        "text": "Fecha y hora",
        "value": "datetime",
        "graphene_type": "graphene.types.datetime.DateTime()",
        "alchemy_type": "Column(DateTime)",
    },
    "image": {
        "text": "Campo imagenes",
        "value": "image"
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
        str_field = field["titulo"] + " = " + types[field["tipo"]]["alchemy_type"]
        fields += str_field + "\n    "

    template = template.replace("FIELDS", fields)
    if return_class:
        return template


def json_to_model():
    json_files = file_list(bdd_dir)
    model_classes = ""
    for f in json_files:
        model_classes += json_to_class(f, return_class=True) + "\n"

    model_file = join(current_dir, "..", "graph_ql", "models.py")

    if replace_in_file(model_file, "# __MODELS__", "\n" + model_classes + "\n"):
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

        fields_str = ""
        fields_read_only = ""
        fields_black_list = ""

        for field in table["fields"]:
            if field["tipo"] != "json":
                if field["titulo"] not in black_list:
                    fields_str += (
                        field["titulo"]
                        + "="
                        + types[field["tipo"]]["graphene_type"]
                        + ",\n    "
                    )
                else:
                    fields_black_list += (
                        field["titulo"]
                        + "="
                        + types[field["tipo"]]["graphene_type"]
                        + ",\n    "
                    )
            else:
                fields_read_only += (
                    field["titulo"]
                    + "="
                    + types[field["tipo"]]["graphene_type"]
                    + ",\n    "
                )

        template = template.replace("EXTRA_FIELDS", fields_str.rstrip()[:-1])
        template = template.replace("READ_ONLY_FIELDS", fields_read_only.rstrip()[:-1])
        template = template.replace(
            "BLACK_LIST_FIELDS", fields_black_list.rstrip()[:-1]
        )

        extra_schema=""
        if f=='image':
            extra_schema = "url=url_object.url\n    resolve_url=url_object.resolve_url"
        template = template.replace("EXTRA_SCHEMA", extra_schema)


        schema_file = join(schemas_dir, f + "_schema.py")
        if not force and isfile(schema_file):
            print("El archivo ", schema_file, " Existe, saltando...")
        else:
            if create_file(schema_file, template, force):
                print("schema creado correctamente!", schema_file)
            else:
                print("Error al crear el schema!", schema_file)


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


def create_file(file_name, content, force=False):
    if isfile(file_name) and not force:
        raise FileExistsError(file_name + " Already exists")
    else:
        with open(file_name, "w") as class_table:
            class_table.write(content)
            return True
    return False


bdd_to_folder()
json_to_model()
json_to_schema(force=True)
