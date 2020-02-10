import graphene
from .utils.image import recortar_foto
from os.path import join
from urllib.request import pathname2url

class url_object(graphene.ObjectType):
    tag = graphene.String()
    url = graphene.String()

    def __init__(self, image_origin, recorte):
        if ( image_origin.table_name != None and image_origin.idparent != None and image_origin.field_name != None ):
            size_filter = (None, 0, "", "0")

            if (
                recorte["width"] not in size_filter
                or recorte["height"] not in size_filter
            ):
                if recorte["width"] in size_filter:
                    recorte["width"] = 0
                if recorte["height"] in size_filter:
                    recorte["height"] = 0

                recorte["tag"] = f"{recorte['width']}x{recorte['height']}"
            else:
                recorte["width"] = 0
                recorte["height"] = 0
                recorte["tag"] = image_origin.name

            if recorte["format"] == None:
                recorte["format"] = image_origin.extension

            recorte["folder"] = join(
                image_origin.table_name,
                str(image_origin.idparent),
                str(image_origin.field_name),
                str(image_origin.idimage),
            )

            response = recortar_foto(recorte, image_origin)
            if not response["exito"]:
                raise Exception(response["mensaje"])
            else:
                self.tag = recorte["tag"]
                self.url = response["url"]
        else:
            self.tag = "tmp"
            self.url = join(
                "tmp",
                str(image_origin.idimage),
                image_origin.name + "." + image_origin.extension,
            )

        self.url = pathname2url(self.url)


def resolve_url(parent, info,width=None,height=None,format=None,regenerate=False):
    recorte = {"width": width, "height": height, "format": format, "regenerate": regenerate}
    return Url(parent, recorte)


url = graphene.Field(url_object,width=graphene.String(), height=graphene.String(), format=graphene.String(), regenerate=graphene.Boolean())