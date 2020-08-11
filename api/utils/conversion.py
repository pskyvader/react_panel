import sys
from os.path import dirname, isfile, join


current_dir = dirname(__file__)
sys.path.append(join(current_dir, ".."))

import json
import time
from os import listdir


from graph_ql.utils.format import MyEncoder, NoIndent

config_file = join(current_dir, "..", "config", "config.json")
config = {}
with open(config_file) as f:
    config = json.load(f)

bdd_dir = join(current_dir, "..", "config", "bdd")
module_dir = join(current_dir, "..", "config", "modules")
model_dir = join(current_dir, "..", "graph_ql", "model")
schemas_dir = join(current_dir, "..", "graph_ql", "schemas")

JSONTYPE = ".json"
INTTYPE = "int(11)"

types = {
    "char(255)": {
        "text": "Texto",
        "value": "char(255)",
        "graphene_type": "graphene.String()",
        "alchemy_type": "Column(String(255))",
    },
    INTTYPE: {
        "text": "Numero",
        "value": INTTYPE,
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
    "json": {
        "text": "Campo JSON (archivos o imagenes.... TEMPORAL)",
        "value": "json",
        "graphene_type": "graphene.JSONString()",
        "alchemy_type": "Column(JSON)",
    },
    "image": {"text": "Campo imagenes", "value": "image"},
    "id": {
        "text": "Campo primario",
        "value": INTTYPE,
        "graphene_type": "graphene.NonNull(graphene.ID)",
        "alchemy_type": "Column(Integer, primary_key=True, nullable=False)",
    },
}

black_list = ["password"]


file_cache = {}


def bdd_to_folder():
    file_str = join(bdd_dir, "bdd.json")
    try:
        with open(file_str, "r") as file1:
            tables = json.loads(file1.read())
            for t in tables:
                tablename = join(bdd_dir, t["tablename"] + JSONTYPE)
                with open(tablename, "w") as table:
                    table.write(json.dumps(t))
                    print("table", tablename, "created")
    except FileNotFoundError as e:
        print("archivo", file_str, "no existe", e)


def module_to_folder():
    file_str = join(module_dir, "..", "moduloconfiguracion.json")
    try:
        with open(file_str, "r") as file1:
            tables = json.loads(file1.read())
            number = 0
            for t in tables:
                if t["module"] == "separador":
                    number += 1
                    module = join(module_dir, t["module"] + str(number) + JSONTYPE)
                else:
                    module = join(module_dir, t["module"] + JSONTYPE)
                with open(module, "w") as table:
                    table.write(json.dumps(t))
                    print("modulo", module, "created")
    except FileNotFoundError as e:
        print("archivo", file_str, "no existe", e)


def set_modules(modulelist, table):
    """ Helper function for json to module
    :type modulelist: Dictionary
    :param modulelist: List of modules

    :type table: Dictionary
    :param table: Module (JSON file converted from modules folder)

    :rtype: Dictionary
    """
    for key in modulelist.keys():
        if key == "icono":
            icono = str(table[key]).split("_")
            modulelist[key] = "".join([i.capitalize() for i in icono])
        elif modulelist[key] != [] and not isinstance(modulelist[key], bool):
            modulelist[key] = table[key]
        elif modulelist[key] != []:
            modulelist[key] = bool(table[key])
        elif key != "hijo" and key != "menu":
            new_array = []
            for e in table[key]:
                if e["field"] == "0":
                    e["field"] = "id" + table["module"]
                new_array.append(NoIndent(e))
            modulelist[key] = new_array
    return modulelist


def set_estado(table_child, table_module):
    """ Helper function for set children
    :type table_child: Dictionary
    :param table_child: Module child

    :type table_module: String
    :param table_module: Name of the module

    :rtype: Dictionary
    """

    def parse_bool(element):
        return True if element == "true" else False

    new_permisos = {}
    for tipo in range(1, 4):
        new_permiso = {
            "estado": False,
            "menu": {},
            "mostrar": {},
            "detalle": {},
        }
        new_permiso["estado"] = (
            True if table_child["estado"][0]["estado"][str(tipo)] == "true" else False
        )

        for menu_hijo in table_child["menu"]:
            new_permiso["menu"][menu_hijo["field"]] = parse_bool(
                menu_hijo["estado"][str(tipo)]
            )

        new_permiso["menu"] = NoIndent(new_permiso["menu"])

        for mostrar_hijo in table_child["mostrar"].copy():
            if mostrar_hijo["field"] == "0":
                mostrar_hijo["field"] = "id" + table_module
            new_permiso["mostrar"][mostrar_hijo["field"]] = parse_bool(
                mostrar_hijo["estado"][str(tipo)]
            )

        new_permiso["mostrar"] = NoIndent(new_permiso["mostrar"])

        for detalle_hijo in table_child["detalle"]:
            new_permiso["detalle"][detalle_hijo["field"]] = parse_bool(
                detalle_hijo["estado"][str(tipo)]
            )
        new_permiso["detalle"] = NoIndent(new_permiso["detalle"])

        new_permisos[tipo] = new_permiso
    return new_permisos


def set_children(table):
    """ Helper function for json to module

    :type table: Dictionary
    :param table: Module (JSON file converted from modules folder)

    :rtype: Dictionary
    """
    child = {
        "tipo": 0,
        "titulo": "",
        "permisos": {},
        "orden": 0,
        "aside": False,
        "hijos": False,
    }
    new_children = []
    for table_child in table["hijo"]:
        new_child = child.copy()
        for k, v in new_child.items():
            if k != "permisos" and k != "estado":
                new_child[k] = (
                    table_child[k]
                    if not isinstance(new_child[k], bool)
                    else bool(table_child[k])
                )

        if "estado" in table_child:
            new_child["permisos"] = set_estado(table_child, table["module"])
        else:
            new_child["permisos"] = table_child["permisos"]

        new_children.append(new_child)
    return new_children


def set_menu(table):
    """ Helper function for json to module

    :type table: Dictionary
    :param table: Module (JSON file converted from modules folder)

    :rtype: Dictionary
    """

    menu = {"field": "", "titulo": ""}

    new_menus = []
    for hijo_menu in table["hijo"][0]["menu"]:
        new_menu = menu.copy()
        for key in new_menu.keys():
            new_menu[key] = hijo_menu[key]
        new_menus.append(NoIndent(new_menu))

    return new_menus


def json_to_module():
    module = {
        "icono": "",
        "module": "",
        "titulo": "",
        "sub": "",
        "padre": "",
        "menu": [],
        "mostrar": [],
        "detalle": [],
        "orden": 0,
        "estado": False,
        "aside": False,
        "tipos": False,
        "hijo": [],
    }

    json_files = file_list(module_dir)
    for f in json_files:
        new_module = module.copy()
        table = json.loads(get_file(join(module_dir, f)))
        new_module = set_modules(new_module, table)

        if table["module"] == "separador":
            new_module["estado"] = {"1": True, "2": True, "3": False}
        else:
            if "menu" in table["hijo"][0]:
                new_module["menu"] = set_menu(table)

            new_module["hijo"] = set_children(table)

        if create_file(
            join(module_dir, f),
            json.dumps(new_module, cls=MyEncoder, sort_keys=False, indent=4),
            True,
        ):
            print("modulo creado correctamente!", f)
        else:
            print("Error al crear el modulo!", f)


def json_to_class(tablename, return_class=True):
    template = get_file(join(current_dir, "template_graphene.py"))
    table = json.loads(get_file(join(bdd_dir, tablename)))
    template = template.replace("TABLENAME", table["tablename"])
    template = template.replace("IDNAME", table["idname"])
    template = template.replace("PREFIX", config["prefix"])

    fields = ""
    for field in table["fields"]:
        if field["tipo"] in types and "alchemy_type" in types[field["tipo"]]:
            str_field = "{0}={1}\n    ".format(
                field["titulo"], types[field["tipo"]]["alchemy_type"]
            )
            fields += str_field

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


def set_fields(file_name):

    """ Helper function for json to schema
    :type file_name: String
    :param file_name: File name for schema JSON

    :rtype: tuple (dict,str,str,str)
    """
    table = json.loads(get_file(join(bdd_dir, file_name)))
    image_fields = []

    fields_str = ""
    fields_read_only = ""
    fields_black_list = ""

    for field in table["fields"]:
        if field["tipo"] in types and "alchemy_type" in types[field["tipo"]]:
            field_format = "{0}={1},\n".format(
                field["titulo"], types[field["tipo"]]["graphene_type"]
            )
            if field["titulo"] not in black_list:
                fields_str += field_format
            else:
                fields_black_list += field_format
        else:
            if field["tipo"] != "image":
                field_format = "{0}={1},\n".format(
                    field["titulo"], types[field["tipo"]]["graphene_type"]
                )
                fields_read_only += field_format
            else:
                image_fields.append(field["titulo"])
    return (image_fields, fields_str, fields_read_only, fields_black_list)


def set_extra(image_fields,file_name):
    template_file_image = get_file(join(current_dir, "template_image.py"))
    extra_import = ""
    extra_schema = ""

    if file_name == "image":
        extra_import = "from .. import url_object"
        extra_schema = "url=url_object.url\n    resolve_url=url_object.resolve_url"
    elif len(image_fields) > 0:
        extra_import = "from .image_schema import all_image,resolve_all_image"

        for image in image_fields:
            extra_schema += template_file_image.replace("FIELD", image).replace(
                "TABLENAME", file_name
            )
    return (extra_import, extra_schema)


def json_to_schema(force=False):
    json_files = file_list(bdd_dir)
    template_file = get_file(join(current_dir, "template_schema.py"))

    for file_name in json_files:
        template = template_file

        (image_fields, fields_str, fields_read_only, fields_black_list) = set_fields(
            file_name
        )

        file_name = file_name.replace(JSONTYPE, "")
        template = template.replace("TABLENAME", file_name)


        template = template.replace("EXTRA_FIELDS", fields_str.rstrip()[:-1])
        template = template.replace("READ_ONLY_FIELDS", fields_read_only.rstrip()[:-1])
        template = template.replace(
            "BLACK_LIST_FIELDS", fields_black_list.rstrip()[:-1]
        )

        (extra_import, extra_schema) = set_extra(image_fields,file_name)

        template = template.replace("EXTRA_IMPORT", extra_import)
        template = template.replace("EXTRA_SCHEMA", extra_schema)

        schema_file = join(schemas_dir, file_name + "_schema.py")
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


if __name__ == "__main__":
    module_to_folder()
    bdd_to_folder()
    json_to_model()
    json_to_schema(force=True)
    json_to_module()
