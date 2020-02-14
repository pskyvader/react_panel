from graph_ql.database import config
import json

def parse_post(environ, buffer):
    from cgi import FieldStorage
    from io import BytesIO

    post = {}
    p = FieldStorage(fp=BytesIO(buffer), environ=environ, keep_blank_values=True)
    if p.list != None:
        post = post_field(p)
    return post


def post_field(p):
    from cgi import MiniFieldStorage, FieldStorage
    from html import escape

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
                mime = get_content_type_by_filename(name)
                if mime == None:
                    mime = "text/plain"
                post["file"].append({"name": name, "type": mime, "tmp_name": tmpfile})
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
        raise RuntimeError("Error al obtener post: " + repr(error) + repr(p))
    return post


def get_content_type_by_filename(file_name):
    from os.path import basename

    mime_type = ""
    mime_map = {
        "js": "application/javascript",
        "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "xltx": "application/vnd.openxmlformats-officedocument.spreadsheetml.template",
        "potx": "application/vnd.openxmlformats-officedocument.presentationml.template",
        "ppsx": "application/vnd.openxmlformats-officedocument.presentationml.slideshow",
        "pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        "sldx": "application/vnd.openxmlformats-officedocument.presentationml.slide",
        "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "dotx": "application/vnd.openxmlformats-officedocument.wordprocessingml.template",
        "xlam": "application/vnd.ms-excel.addin.macroEnabled.12",
        "xlsb": "application/vnd.ms-excel.sheet.binary.macroEnabled.12",
        "apk": "application/vnd.android.package-archive",
    }

    try:
        suffix = ""
        name = basename(file_name)
        suffix = name.split(".")[-1]
        if suffix in mime_map.keys():
            mime_type = mime_map[suffix]
        else:
            import mimetypes

            mimetypes.init()
            mime_type = mimetypes.types_map["." + suffix]
    except Exception:
        mime_type = "application/octet-stream"
    if not mime_type:
        mime_type = "application/octet-stream"
    return mime_type


def url_amigable(url=""):
    url = replaceMultiple(url, ["á", "à", "â", "ã", "ª", "ä"], "a")
    url = replaceMultiple(url, ["Á", "À", "Â", "Ã", "Ä"], "A")
    url = replaceMultiple(url, ["Í", "Ì", "Î", "Ï"], "I")
    url = replaceMultiple(url, ["í", "ì", "î", "ï"], "i")
    url = replaceMultiple(url, ["é", "è", "ê", "ë"], "e")
    url = replaceMultiple(url, ["É", "È", "Ê", "Ë"], "E")
    url = replaceMultiple(url, ["ó", "ò", "ô", "õ", "ö"], "o")
    url = replaceMultiple(url, ["Ó", "Ò", "Ô", "Õ", "Ö"], "O")
    url = replaceMultiple(url, ["ú", "ù", "û", "ü"], "u")
    url = replaceMultiple(url, ["Ú", "Ù", "Û", "Ü"], "U")
    url = replaceMultiple(
        url, ["[", "^", "´", "`", "¨", "~", "]", " ", "/", "°", "º"], "-"
    )
    url = url.replace("ç", "c")
    url = url.replace("Ç", "C")
    url = url.replace("ñ", "n")
    url = url.replace("Ñ", "N")
    url = url.replace("Ý", "Y")
    url = url.replace("ý", "y")
    url = url.lower()
    return url


def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces:
        # Check if string is in the main string
        if elem in mainString:
            # Replace the string
            mainString = mainString.replace(elem, newString)
    return mainString


def current_time(formato:str="%Y-%m-%d %H:%M:%S", as_string:bool=True):
        """ fecha actual en zona horaria santiago, formato opcional
        :type formato:str:
        :param formato:str:
    
        :type as_string:bool:
        :param as_string:bool:
    
        :raises:
    
        :rtype: datetime.timestamp() or str
        """

        import datetime
        import pytz
        fecha = datetime.datetime.now(pytz.timezone(config["timezone"]))
        if as_string:
            return fecha.strftime(formato)
        else:
            return fecha.timestamp()


# https://gist.github.com/e96666ca4f059c3e5bc28abb711b5c92.git

class CompactJSONEncoder(json.JSONEncoder):
    """A JSON Encoder that puts small lists on single lines."""

    MAX_WIDTH = 60
    """Maximum width of a Single Line List (SLL)."""

    MAX_ITEMS = 2
    """Maximum number of items of a Single Line List (SLL)."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.indentation_level = 0

    def encode(self, o):
        """Encode JSON object *o* with respect to single line lists."""
        if isinstance(o, (list, tuple)):
            if self._is_single_line_list(o):
                return "[" + ", ".join(json.dumps(el) for el in o) + "]"
            else:
                self.indentation_level += 1
                output = [self.indent_str + self.encode(el) for el in o]
                self.indentation_level -= 1
                return "[\n" + ",\n".join(output) + "\n" + self.indent_str + "]"
        elif isinstance(o, dict):
            self.indentation_level += 1
            output = [
                self.indent_str + f"{json.dumps(k)}: {self.encode(v)}"
                for k, v in o.items()
            ]
            self.indentation_level -= 1
            return "{\n" + ",\n".join(output) + "\n" + self.indent_str + "}"
        else:
            return json.dumps(o)

    def _is_single_line_list(self, o):
        return (
            self._primitives_only(o)
            and len(o) <= self.MAX_ITEMS
            and len(str(o)) - 2 <= self.MAX_WIDTH
        )

    def _primitives_only(self, o):
        if isinstance(o, (list, tuple)):
            return not any(isinstance(el, (list, tuple, dict)) for el in o)

    @property
    def indent_str(self) -> str:
        return " " * self.indentation_level * self.indent
