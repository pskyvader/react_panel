from pathlib import Path
from os import makedirs
from os import rename
from os.path import join, dirname
import sys

from .format import url_amigable

current_dir = dirname(__file__)

types = [ "image/webp", "image/bmp", "image/gif", "image/pjpeg", "image/jpeg", "image/svg+xml", "image/png", ]
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
        folder=join(folder,folder_upload)
        makedirs(folder, exist_ok=True)

        with open(join(folder,name_final + extension), "wb") as output_file:
            output_file.write(file["tmp_name"])

        if not respuesta["exito"]:
            respuesta["mensaje"] = (
                "Error al mover archivo. Permisos: "
                + oct(stat.S_IMODE(os.lstat(folder).st_mode))
                + ", carpeta: "
                + folder
            )
        else:
            respuesta["extension"] = extension
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



def recortar_foto(recorte, datos):
    """Recorta una foto"""
    from PIL import Image

    respuesta = {"exito": False, "mensaje": ""}
    ancho_maximo = recorte["ancho"]
    alto_maximo = recorte["alto"]
    ruta = upload_dir + datos["folder"] + "/"
    foto = datos["name"]
    etiqueta = recorte["tag"]
    tipo = recorte["tipo"]

    ruta_imagen = ruta + foto
    my_file = Path(ruta_imagen)
    if not my_file.is_file():
        respuesta["mensaje"] = "Archivo " + ruta_imagen + " no existe"
        return respuesta

    im = open(ruta_imagen)
    ancho, alto = im.size
    imagen_tipo = im.format.lower()

    proporcion_imagen = ancho / alto
    if None == ancho_maximo or 0 == ancho_maximo:
        ancho_maximo = int(round(alto_maximo * proporcion_imagen))
    if None == alto_maximo or 0 == alto_maximo:
        alto_maximo = int(round(ancho_maximo / proporcion_imagen))

    x, y, miniatura_ancho, miniatura_alto = proporcion_foto(
        ancho_maximo, alto_maximo, ancho, alto, tipo
    )

    if "png" == imagen_tipo:
        im = im.convert("RGBA")
    else:
        im = im.convert("RGB")

    foto_recorte = nombre_archivo(foto, etiqueta, "", True)
    foto_webp = nombre_archivo(foto, etiqueta, "webp", True)

    if tipo == "recortar":
        box = (x, y, ancho_maximo + x, alto_maximo + y)
        im = im.resize((miniatura_ancho, miniatura_alto), ANTIALIAS)
        new_im = im.crop(box)
    elif "rellenar" == tipo:
        if "png" == imagen_tipo:
            new_im = new("RGBA", (ancho_maximo, alto_maximo), (255, 255, 255, 0))
        else:
            new_im = new("RGB", (ancho_maximo, alto_maximo), (255, 255, 255))
        box = (x, y)
        im = im.resize((miniatura_ancho, miniatura_alto), ANTIALIAS)
        new_im.paste(im, (box))
    else:
        if ancho >= miniatura_ancho or alto >= miniatura_alto:
            if "png" == imagen_tipo:
                new_im = new("RGBA", (ancho_maximo, alto_maximo), (255, 255, 255, 0))
            else:
                new_im = new("RGB", (ancho_maximo, alto_maximo), (255, 255, 255))
            box = (x, y)
            im = im.resize((miniatura_ancho, miniatura_alto), ANTIALIAS)
            new_im.paste(im, (box))
        else:
            if "png" == imagen_tipo:
                new_im = new("RGBA", (ancho_maximo, alto_maximo), (255, 255, 255, 0))
            else:
                new_im = new("RGB", (ancho_maximo, alto_maximo), (255, 255, 255))

            # im=im.resize((miniatura_ancho, miniatura_alto), ANTIALIAS)
            # box = (x, y, ancho_maximo+x, alto_maximo+y)
            box = (x, y)
            new_im.paste(im, (box))

    my_file = Path(ruta + foto_recorte)
    if my_file.is_file():
        my_file.unlink()
    my_file = Path(ruta + foto_webp)
    if my_file.is_file():
        my_file.unlink()

    new_im.save(ruta + foto_recorte)
    # if "png" != imagen_tipo:
    new_im.save(ruta + foto_webp)

    respuesta["exito"] = True

    return respuesta



def nombre_archivo(file, tag="", extension="", remove=False):
    from os.path import splitext

    name, ext = splitext(file)
    if "" == extension:
        extension = ext
    else:
        extension = "." + extension

    if remove:
        name = ("".join(name)).split("-")
        if len(name) > 1:
            name.pop()

    name = url_amigable("".join(name))
    if "" != tag:
        return name + "-" + tag + extension
    else:
        return name + extension



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



def portada(fotos):
    portada = {}
    if len(fotos) > 0:
        portada = fotos[0]
        for f in fotos:
            if (isinstance(f["portada"], str) and "true" == f["portada"]) or (
                isinstance(f["portada"], bool) and f["portada"]
            ):
                portada = f
                break
    return portada



def delete(folder, file="", subfolder="", sub=""):
    import shutil

    if "" == file and "" != subfolder:
        url = upload_dir + folder + "/" + str(subfolder) + "/"
        if "" != sub:
            url += sub + "/"
        my_file = Path(url)
        if my_file.is_dir():
            shutil.rmtree(url)
    elif "" == file and "" == subfolder:
        url = upload_dir + folder + "/"
        my_file = Path(url)
        if my_file.is_dir():
            shutil.rmtree(url)
    else:
        recortes = get_recortes(folder)
        if "" != subfolder:
            subfolder += "/"
        if "" != sub:
            sub += "/"
        url = upload_dir + folder + "/" + subfolder + sub + file["url"]
        my_file = Path(url)
        if my_file.is_file():
            my_file.unlink()

        for recorte in recortes:
            url = (
                upload_dir
                + folder
                + "/"
                + subfolder
                + sub
                + nombre_archivo(file["url"], recorte["tag"])
            )
            my_file = Path(url)
            if my_file.is_file():
                my_file.unlink()

            url = (
                upload_dir
                + folder
                + "/"
                + subfolder
                + sub
                + nombre_archivo(file["url"], recorte["tag"], "webp")
            )

            my_file = Path(url)
            if my_file.is_file():

                my_file.unlink()



def delete_temp():
    from os import listdir
    from os.path import getmtime

    now = current_time("", False)
    horas = 1

    carpeta = upload_dir + "tmp/"  # ruta actual
    # obtenemos un archivo y luego otro sucesivamente
    for archivo in listdir(carpeta):
        my_file = Path(carpeta + archivo)
        if my_file.is_file():  # verificamos si es o no un archivo
            # si el archivo fue creado hace más de horas, borrar
            if (now - getmtime(carpeta + archivo)) / 3600 > horas:
                my_file.unlink()


