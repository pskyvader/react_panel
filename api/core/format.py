def parse_get(query_string):
    from cgi import parse_qs

    get = dict(parse_qs(query_string))
    if "url" in get:
        del get["url"]
    for k, u in get.items():
        if len(u) == 1:
            get[k] = u[0]
    get = format_array(get)
    get = parse_values(get)
    return get



def parse_post(environ):
    from cgi import FieldStorage
    from io import BytesIO

    post = {}
    if environ["REQUEST_METHOD"] == "POST":
        post_env = environ.copy()
        post_env["QUERY_STRING"] = ""
        post_env["CONTENT_LENGTH"] = int(environ.get("CONTENT_LENGTH", 0))
        buffer = post_env["wsgi.input"].read(post_env["CONTENT_LENGTH"])
        p = FieldStorage(
            fp=BytesIO(buffer), environ=post_env, keep_blank_values=True
        )
        if p.list != None:
            post = post_field(p)

    post = format_array(post)
    post = parse_values(post)
    return post

def post_field(p):
    from cgi import MiniFieldStorage, FieldStorage, escape
    from .functions import functions

    post = {}
    try:
        for key in p.keys():
            if (
                isinstance(p[key], FieldStorage)
                and p[key].file
                and p[key].filename != None
            ):
                if not "file" in post:
                    post["file"] = []
                tmpfile = p[key].file.read()
                name = escape(p[key].filename)
                mime = functions.get_content_type_by_filename(name)
                if mime == None:
                    mime = "text/plain"
                post["file"].append(
                    {"name": name, "type": mime, "tmp_name": tmpfile}
                )
            elif isinstance(p[key], MiniFieldStorage) or isinstance(
                p[key], FieldStorage
            ):
                post[key] = p[key].value
            elif isinstance(p[key], list):
                tmp_list = []
                for a in p[key]:
                    if isinstance(a, MiniFieldStorage):
                        tmp_list.append(a.value)
                    else:
                        tmp_list.append(a)
                post[key] = tmp_list
            else:
                post[key] = p[key]
    except Exception as error:
        # print('Error al obtener post: ' + repr(error) + repr(p)
        raise RuntimeError("Error al obtener post: " + repr(error) + repr(p))
    return post

def format_array(var_original: dict):
    var = var_original.copy()
    var_copy = var.copy()
    aux = {}
    for k, i in var_copy.items():
        # si existe simbolo de array
        if "[" in k:
            # separar key principal de key dentro de array
            final_key, rest = str(k).split("[", 1)
            if rest != "":
                if final_key not in aux:
                    aux[final_key] = {}

                # comprobar si existe simbolo de cerrado, sino se guarda directamente
                if rest.find("]") == -1:
                    aux[final_key][rest] = i
                # comprobar si existe mas de un valor en sub key, sino se recupera el primer y unico valor
                elif rest.find("[") == -1:
                    rest = str(rest).split("]", 1)[0]
                    aux[final_key][rest] = i
                else:
                    if rest.find("]") < rest.find("["):
                        rest1, rest2 = str(rest).split("]", 1)
                        aux[final_key][rest1 + rest2] = i
                    else:
                        print(
                            "error de formato, formato aceptado: a[b][c][d]=valor"
                        )
                        break
                aux[final_key] = format_array(aux[final_key])
            else:
                aux[final_key] = i
            del var[k]
        elif k == "":
            final_key = len(var_copy) - 1
            aux[final_key] = i
            del var[k]

    var = merge(var, aux)
    if len(var) == 1:
        key, value = next(iter(var.items()))
        if isinstance(key, int) and key == 0:
            var = value
    return var

def parse_values(var: dict):
    var_copy = var.copy()
    if isinstance(var_copy, list):
        for i in var_copy:
            if isinstance(i, str):
                try:
                    aux_var = json.loads(i)
                    if isinstance(aux_var, dict) or isinstance(aux_var, list):
                        i = aux_var
                except:
                    pass
            elif isinstance(i, dict) or isinstance(i, list):
                i = app.parse_values(i)
    elif isinstance(var_copy, dict):
        for k, i in var_copy.items():
            if isinstance(i, str):
                try:
                    aux_var = json.loads(i)
                    if isinstance(aux_var, dict) or isinstance(aux_var, list):
                        var_copy[k] = app.parse_values(aux_var)
                except:
                    pass
            elif isinstance(i, dict) or isinstance(i, list):
                var_copy[k] = app.parse_values(i)
    elif isinstance(var_copy, str):
        try:
            aux_var = json.loads(var_copy)
            if isinstance(aux_var, dict) or isinstance(aux_var, list):
                var_copy = app.parse_values(aux_var)
        except:
            pass

    return var_copy

def parse_ip(environ):
    try:
        return str(environ["HTTP_X_FORWARDED_FOR"].split(",")[-1]).strip()
    except KeyError:
        return environ["REMOTE_ADDR"]

def merge(a, b, path=None):
    "merges b into a"
    if path is None:
        path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                app.merge(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass  # same leaf value
            else:
                raise Exception("Conflict at %s" % ".".join(path + [str(key)]))
        else:
            a[key] = b[key]
    return a