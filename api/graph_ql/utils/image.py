from os import makedirs, rename, remove, listdir
from os.path import join, dirname, isfile,isdir, getmtime
import sys

from .format import url_amigable,current_time

current_dir = dirname(__file__)

types = [
    "image/webp",
    "image/bmp",
    "image/gif",
    "image/pjpeg",
    "image/jpeg",
    "image/svg+xml",
    "image/png",
]
extensions = [".webp", ".bmp", ".ico", ".gif", ".jpeg", ".jpg", ".svg", ".xml", ".png"]
upload_dir = join(current_dir, "..", "..", "..", "public", "images")


def move(file_move, folder, subfolder, name_final, folder_tmp="tmp"):
    """mover archivo (normalmente) desde la carpeta temporal a la definitiva"""
    from os.path import splitext

    recortes = get_recortes(folder)
    folder_tmp = upload_dir + folder_tmp
    base_folder = folder
    folder = upload_dir + base_folder + "/" + str(name_final) + "/" + subfolder

    makedirs(folder, exist_ok=True)

    name, extension = splitext(file_move["tmp"])
    file_move["url"] = file_move["id"] + extension

    delete(base_folder, file_move, str(name_final), subfolder)

    rename(folder_tmp + "/" + file_move["tmp"], folder + "/" + file_move["url"])

    for recorte in recortes:
        final_file = folder + "/" + nombre_archivo(file_move["url"], recorte["tag"])

        rename(
            folder_tmp + "/" + nombre_archivo(file_move["tmp"], recorte["tag"]),
            final_file,
        )

        my_file = Path(
            folder_tmp + "/" + nombre_archivo(file_move["tmp"], recorte["tag"], "webp")
        )
        if not my_file.is_dir():
            final_file = (
                folder + "/" + nombre_archivo(file_move["url"], recorte["tag"], "webp")
            )
            rename(
                folder_tmp
                + "/"
                + nombre_archivo(file_move["tmp"], recorte["tag"], "webp"),
                final_file,
            )

    del file_move["tmp"]
    file_move["subfolder"] = subfolder
    return file_move


def copy(original_file, name_final, folder, subfolder="", parent_final="", tag="thumb"):
    """Copia un archivo y retorna la informacion del archivo nuevo """
    import os
    from shutil import copyfile

    respuesta = {"exito": False, "mensaje": ""}

    name, extension = os.path.splitext(original_file["url"])

    new_file = {
        "portada": True,
        "id": original_file["id"],
        "url": str(name_final) + extension,
        "parent": parent_final,
        "folder": folder,
        "subfolder": subfolder,
        "tmp": "",
    }
    original = generar_dir(original_file, tag)

    if original != "":
        base_folder = upload_dir + folder
        folder = base_folder
        if parent_final != "":
            folder += "/" + str(parent_final)

        if subfolder != "":
            folder += "/" + subfolder

        makedirs(folder, exist_ok=True)

        destino = folder + "/" + new_file["url"]
        if os.access(folder, os.W_OK):
            copyfile(original, destino)
            respuesta["exito"] = True
            respuesta["file"] = [new_file]
        else:
            respuesta["mensaje"] = (
                "La carpeta " + folder + " no tiene permisos de escritura"
            )
    else:
        respuesta["mensaje"] = "El archivo original no existe"
    return respuesta


def upload(file, folder_upload="tmp", name_final=""):
    """subir archivo"""
    import uuid
    import stat
    import os
    import tempfile

    folder = upload_dir
    respuesta = validate(file)
    if respuesta["exito"]:
        if "" == name_final:
            name_final = uuid.uuid4().hex
        else:
            name_final, extension = os.path.splitext(name_final)
            name_final = url_amigable("".join(name_final))

        name, extension = os.path.splitext(file["name"])
        extension = extension.lower()

        makedirs(folder, exist_ok=True)
        folder = join(folder, folder_upload)
        makedirs(folder, exist_ok=True)

        with open(join(folder, name_final + extension), "wb") as output_file:
            output_file.write(file["tmp_name"])

        if not respuesta["exito"]:
            respuesta["mensaje"] = (
                "Error al mover archivo. Permisos: "
                + oct(stat.S_IMODE(os.lstat(folder).st_mode))
                + ", carpeta: "
                + folder
            )
        else:
            respuesta["extension"] = extension.replace(".", "")
            respuesta["name"] = name_final
            respuesta["folder"] = folder_upload
            respuesta["original_name"] = file["name"]
            respuesta["mensaje"] = "Imagen " + file["name"] + " Subida correctamente"
    return respuesta


def validate(file):
    from os.path import splitext

    name, extension = splitext(file["name"])
    extension = extension.lower()
    respuesta = {"exito": False, "mensaje": "Error: formato no valido"}
    if "error" in file and 0 != file["error"]:
        respuesta["mensaje"] = "Error al subir archivo: " + file["error"]
    elif file["type"] not in types:
        respuesta["mensaje"] += ". Extension: " + file["type"]
    elif extension not in extensions:
        respuesta["mensaje"] += ".<br/> Extension de archivo: " + extension
    else:
        respuesta["exito"] = True
    return respuesta


def recortes_foto(archivo, recortes_foto):
    """Genera recortes de las fotos"""
    from PIL import Image

    respuesta = {"exito": False}
    ruta = upload_dir + archivo["folder"]
    foto = archivo["name"]
    ruta_imagen = ruta + "/" + foto
    my_file = Path(ruta_imagen)
    if not my_file.is_file():
        respuesta["mensaje"] = "Archivo " + ruta_imagen + " no existe"
        return respuesta

    im = open(ruta_imagen)
    ancho, alto = im.size

    ancho_maximo = 0
    alto_maximo = 0
    ancho_valido = 0
    alto_valido = 0

    for recorte in recortes_foto:
        if recorte["ancho"] != None and recorte["ancho"] > ancho_maximo:
            ancho_maximo = recorte["ancho"]
            if ancho_maximo > ancho_valido and ancho_maximo <= ancho:
                ancho_valido = ancho_maximo
        if recorte["alto"] != None and recorte["alto"] > alto_maximo:
            alto_maximo = recorte["alto"]
            if alto_maximo > alto_valido and alto_maximo <= alto:
                alto_valido = alto_maximo

    # si es valido, se crea una imagen intermedia para acelerar el proceso de recorte de las demas imagenes
    if (alto > (alto_valido * 1.5) and alto_valido > 0) or (
        ancho > (ancho_valido * 1.5) and ancho_valido > 0
    ):
        # alto proporcional segun mayor ancho valido
        # alto_final = (alto / ancho) * ancho_valido
        # ancho proporcional segun mayor alto valido
        ancho_final = int(round((ancho / alto) * alto_valido))
        if ancho_final >= ancho_valido:
            respuesta = recortar_foto(
                {
                    "tag": "recorte_previo",
                    "ancho": None,
                    "alto": alto_valido,
                    "calidad": 100,
                    "tipo": "rellenar",
                },
                archivo,
            )
        else:
            respuesta = recortar_foto(
                {
                    "tag": "recorte_previo",
                    "ancho": ancho_valido,
                    "alto": None,
                    "calidad": 100,
                    "tipo": "rellenar",
                },
                archivo,
            )

        if not respuesta["exito"]:
            return respuesta

        archivo_recorte = archivo.copy()
        archivo_recorte["name"] = nombre_archivo(
            archivo_recorte["name"], "recorte_previo"
        )
        for recorte in recortes_foto:
            if (
                recorte["ancho"] != None
                and recorte["ancho"] <= ancho_valido
                and recorte["alto"] != None
                and recorte["alto"] <= alto_valido
            ):
                respuesta = recortar_foto(recorte, archivo_recorte)
            else:
                respuesta = recortar_foto(recorte, archivo)

            if not respuesta["exito"]:
                return respuesta

    else:
        for recorte in recortes_foto:
            respuesta = recortar_foto(recorte, archivo)
            if not respuesta["exito"]:
                return respuesta

    return respuesta


def proporcion_foto(ancho_maximo, alto_maximo, ancho, alto, tipo):
    """Obtener proporciones de foto final"""
    proporcion_imagen = ancho / alto
    proporcion_miniatura = ancho_maximo / alto_maximo
    miniatura_ancho = ancho_maximo
    miniatura_alto = alto_maximo

    if tipo == "recortar":
        if proporcion_imagen > proporcion_miniatura:
            miniatura_ancho = alto_maximo * proporcion_imagen
        elif proporcion_imagen < proporcion_miniatura:
            miniatura_alto = ancho_maximo / proporcion_imagen

        x = (miniatura_ancho - ancho_maximo) / 2
        y = (miniatura_alto - alto_maximo) / 2
    else:
        if proporcion_imagen > proporcion_miniatura:
            if ancho > alto:
                miniatura_alto = ancho_maximo / proporcion_imagen
            else:
                if ancho_maximo > alto_maximo:
                    miniatura_alto = alto_maximo * proporcion_imagen
                else:
                    miniatura_alto = ancho_maximo / proporcion_imagen

        elif proporcion_imagen < proporcion_miniatura:
            if ancho_maximo > alto_maximo:
                miniatura_ancho = alto_maximo * proporcion_imagen
            elif ancho_maximo < alto_maximo:
                miniatura_ancho = ancho_maximo * proporcion_miniatura
            else:
                miniatura_ancho = ancho_maximo * proporcion_imagen

        if tipo == "centrar" and ancho < miniatura_ancho and alto < miniatura_alto:
            x = (ancho_maximo - ancho) / 2
            y = (alto_maximo - alto) / 2
        else:
            x = (ancho_maximo - miniatura_ancho) / 2
            y = (alto_maximo - miniatura_alto) / 2
    return (
        int(round(x)),
        int(round(y)),
        int(round(miniatura_ancho)),
        int(round(miniatura_alto)),
    )



class cache_image():
    cache=[]
    cache_obj=None
    def exists_url(self,url):
        if url in self.cache:
            return True
        elif isfile(url):
            self.cache.append(url)
            return True
        return False
    
    @staticmethod
    def exists(url):
        if cache_image.cache_obj==None:
            cache_image.cache_obj=cache_image()
        return cache_image.cache_obj.exists_url(url)

    @staticmethod
    def empty(url=None):
        if cache_image.cache_obj==None:
            cache_image.cache_obj=cache_image()

        if url!=None:
            cache_image.cache_obj.cache.remove(url)
            remove(url)
        else:
            cache_image.cache_obj.cache=[]

def recortar_foto(recorte, datos):
    """Recorta una foto"""
    from PIL import Image

    respuesta = {"exito": False, "mensaje": ""}
    ancho_maximo = ( int(recorte["width"]) if recorte["width"] != None else 0 )
    alto_maximo = ( int(recorte["height"]) if recorte["height"] != None else 0 )
    ruta = recorte["folder"]
    foto = datos.name
    etiqueta = recorte["tag"] if ancho_maximo!=0 or alto_maximo!=0 else ""
    tipo = recorte.get("tipo", "rellenar")

    ruta_imagen = join(ruta, foto + "." + datos.extension)


    if not cache_image.exists(join(upload_dir, ruta_imagen)):
        respuesta["mensaje"] = "Archivo " + ruta_imagen + " no existe"
        return respuesta

    url = join(ruta, nombre_archivo(foto + "." + datos.extension, etiqueta, recorte["format"]))
    foto_recorte = join(upload_dir, url)
    if not recorte["regenerate"] and cache_image.exists(foto_recorte):
        respuesta["mensaje"] = "Archivo " + url + " ya existe"
        respuesta["exito"] = True
        respuesta["url"] = url
        return respuesta
        

    im = Image.open(join(upload_dir, ruta_imagen))
    ancho, alto = im.size
    imagen_tipo = im.format.lower()

    proporcion_imagen = ancho / alto
    if  0 == ancho_maximo:
        if 0 == alto_maximo:
            alto_maximo = alto
            ancho_maximo = ancho
        else:
            ancho_maximo = int(round(alto_maximo * proporcion_imagen))
    elif 0 == alto_maximo:
        alto_maximo = int(round(ancho_maximo / proporcion_imagen))

    x, y, miniatura_ancho, miniatura_alto = proporcion_foto(
        ancho_maximo, alto_maximo, ancho, alto, tipo
    )

    if "png" == imagen_tipo:
        im = im.convert("RGBA")
    else:
        im = im.convert("RGB")

    if tipo == "recortar":
        box = (x, y, ancho_maximo + x, alto_maximo + y)
        im = im.resize((miniatura_ancho, miniatura_alto), Image.ANTIALIAS)
        new_im = im.crop(box)
    else:
        if "png" == recorte["format"] or "webp" == recorte["format"]:
            new_im = Image.new("RGBA", (ancho_maximo, alto_maximo), (255, 255, 255, 0))
        else:
            new_im = Image.new("RGB", (ancho_maximo, alto_maximo), (255, 255, 255))

        if "rellenar" == tipo:
            box = (x, y)
            im = im.resize((miniatura_ancho, miniatura_alto), Image.ANTIALIAS)
            new_im.paste(im, (box))
        else: # Centrar
            if ancho >= miniatura_ancho or alto >= miniatura_alto:
                box = (x, y)
                im = im.resize((miniatura_ancho, miniatura_alto), Image.ANTIALIAS)
                new_im.paste(im, (box))
            else:
                box = (x, y)
                new_im.paste(im, (box))

    if cache_image.exists(foto_recorte):
        cache_image.empty(foto_recorte)

    new_im.save(foto_recorte)

    respuesta["exito"] = True
    respuesta["url"] = url
    return respuesta


def nombre_archivo(file, tag="", extension=""):
    from os.path import splitext

    name, ext = splitext(file)
    extension = ext if "" == extension else "." + extension
    name = url_amigable("".join(name))
    return (tag if tag != "" else name) + extension


def generar_dir(file, tag="thumb", extension="", folder="", subfolder=""):
    if "" == folder:
        folder = file["folder"]
    if "" != subfolder:
        subfolder += "/"
    elif file["parent"] != "":
        subfolder = str(file["parent"]) + "/"
        if file["subfolder"] != "":
            subfolder += file["subfolder"] + "/"

    url = folder + "/" + subfolder + (nombre_archivo(file["url"], tag, extension))
    archivo = upload_dir + url
    my_file = Path(archivo)
    if not my_file.is_file():
        archivo = ""
    return archivo


def delete(folder, keep_original,original_file=None):
    import shutil

    directory = join(upload_dir, folder)
    if keep_original:
        if original_file==None:
            raise FileNotFoundError("You must provide a valid original file name")
        original_found=False
        for file in listdir(directory):
            file = join(directory, file)
            if cache_image.exists(file):
                if original_file in file:
                    original_found=True
                else:
                    cache_image.empty(file)
            if isdir(file):
                shutil.rmtree(file)
                cache_image.empty()
        if original_found:
            return "All directory files but original deleted"
        else:
            return "All directory files deleted. Original not found"
    else:
        if isdir(directory):
            shutil.rmtree(directory)
            cache_image.empty()
            return "Directory deleted"
        else:
            return directory+" Not a directory"



def delete_temp():
    now = current_time("", False)
    horas = 1
    carpeta = join(upload_dir , "tmp")  # ruta actual
    # obtenemos un archivo y luego otro sucesivamente
    for archivo in listdir(carpeta):
        file = join(carpeta + archivo)
        if cache_image.exists(file):
            if (now - getmtime(file)) / 3600 > horas:
                cache_image.empty(file)

