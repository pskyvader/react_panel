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
        # print('Error al obtener post: ' + repr(error) + repr(p)
        raise RuntimeError("Error al obtener post: " + repr(error) + repr(p))
    return post


def get_content_type_by_filename(file_name):
    from os.path import basename

    mime_type = ""
    mime_map = {}
    mime_map["js"] = "application/javascript"
    mime_map["xlsx"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    mime_map["xltx"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.template"
    mime_map["potx"] = "application/vnd.openxmlformats-officedocument.presentationml.template"
    mime_map["ppsx"] = "application/vnd.openxmlformats-officedocument.presentationml.slideshow"
    mime_map["pptx"] = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    mime_map["sldx"] = "application/vnd.openxmlformats-officedocument.presentationml.slide"
    mime_map["docx"] = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    mime_map["dotx"] = "application/vnd.openxmlformats-officedocument.wordprocessingml.template"
    mime_map["xlam"] = "application/vnd.ms-excel.addin.macroEnabled.12"
    mime_map["xlsb"] = "application/vnd.ms-excel.sheet.binary.macroEnabled.12"
    mime_map["apk"] = "application/vnd.android.package-archive"
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
