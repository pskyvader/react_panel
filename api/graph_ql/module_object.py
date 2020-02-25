import graphene
from graph_ql.schemas.administrador_schema import resolve_administrador

import json
from os.path import join, dirname
from utils.conversion import file_list, get_file


current_dir = dirname(__file__)

module_dir = join(current_dir, "..", "config", "modules")
module_list = []


json_files = file_list(module_dir)
for f in json_files:
    module_file = json.loads(get_file(join(module_dir, f)))
    module_list.append(module_file)

cache_module_permissions = {}
cache_detail = {}


class menu_object(graphene.ObjectType):
    field = graphene.String()
    titulo = graphene.String()


class mostrar_object(graphene.ObjectType):
    field = graphene.String()
    titulo = graphene.String()
    tipo = graphene.String()


class detalle_object(graphene.ObjectType):
    field = graphene.String()
    titulo = graphene.String()
    tipo = graphene.String()


class permisos_detail_object(graphene.ObjectType):
    field = graphene.String()
    titulo = graphene.String()
    tipo = graphene.String()
    estado = graphene.Boolean()


class permisos_object(graphene.ObjectType):
    estado = graphene.Boolean()
    menu = graphene.List(permisos_detail_object,estado=graphene.Boolean())
    mostrar = graphene.List(permisos_detail_object,estado=graphene.Boolean())
    detalle = graphene.List(permisos_detail_object,estado=graphene.Boolean())

    def resolve_menu(parent, info,estado=None):
        list_menu = []
        temp_list={}
        for m in parent['parent']['menu']:
            temp_list[m['field']]=m
        for k, m in parent["menu"].items():
            temp_list[k]['estado']=m

        for k, m in temp_list.items():
            if estado==None or m['estado']==estado:
                list_menu.append(permisos_detail_object(**m))
        return list_menu

    def resolve_mostrar(parent, info,estado=None):
        list_mostrar = []
        temp_list={}
        for m in parent['parent']['mostrar']:
            temp_list[m['field']]=m
        for k, m in parent["mostrar"].items():
            temp_list[k]['estado']=m

        for k, m in temp_list.items():
            if estado==None or m['estado']==estado:
                list_mostrar.append(permisos_detail_object(**m))
        return list_mostrar

    def resolve_detalle(parent, info,estado=None):
        list_detalle = []
        temp_list={}
        for m in parent['parent']['detalle']:
            temp_list[m['field']]=m
        for k, m in parent["detalle"].items():
            temp_list[k]['estado']=m

        for k, m in temp_list.items():
            if estado==None or m['estado']==estado:
                list_detalle.append(permisos_detail_object(**m))
        return list_detalle


class module_configuration_object(graphene.ObjectType):
    tipo = graphene.Int()
    titulo = graphene.String()
    orden = graphene.Int()
    aside = graphene.Boolean()
    hijos = graphene.Boolean()
    permisos = graphene.Field(permisos_object)


class module_object(graphene.ObjectType):
    icono = graphene.String()
    module = graphene.String()
    titulo = graphene.String()
    sub = graphene.String()
    padre = graphene.String()
    orden = graphene.Int()
    estado = graphene.Boolean()
    aside = graphene.Boolean()
    tipos = graphene.Boolean()

    menu = graphene.List(menu_object)
    mostrar = graphene.List(mostrar_object)
    detalle = graphene.List(detalle_object)
    hijo = graphene.List(module_configuration_object, tipo=graphene.Int())


    def resolve_hijo(parent, info, tipo=None):
        if tipo == None:
            return parent.hijo
        else:
            for i in parent.hijo:
                if tipo == i["tipo"]:
                    i['permisos']['parent']={ 'menu':parent.menu, 'mostrar':parent.mostrar, 'detalle':parent.detalle }
                    return [module_configuration_object(**i)]
            return None


def filter_permissions(list_modules, tipo):
    module_list_final = []

    for v in list_modules:
        c_module = v.copy()
        if c_module["module"] == "separador":
            if str(tipo) in c_module["estado"] and c_module["estado"][str(tipo)]:
                module_list_final.append(c_module)
        else:
            c_module["hijo"] = []
            for hijo in v["hijo"]:
                c_hijo = hijo.copy()
                c_hijo["permisos"] = {}
                if ( str(tipo) in hijo["permisos"] and hijo["permisos"][str(tipo)]["estado"] ):
                    c_hijo["permisos"] = hijo["permisos"][str(tipo)]
                if c_hijo["permisos"] != {}:
                    c_module["hijo"].append(c_hijo)
            if c_module["hijo"] != []:
                module_list_final.append(c_module)

    return [v for v in sorted(module_list_final, key=lambda item: item["orden"])]


def resolve_all_module(args, info, idadministrador):
    administrador = resolve_administrador(args, info, idadministrador)
    if administrador == None:
        return None

    if administrador.tipo in cache_module_permissions:
        return cache_module_permissions[administrador.tipo]

    filtered_module = filter_permissions(module_list, administrador.tipo)

    final_list = []
    for m in filtered_module:
        m_o = module_object(**m)
        final_list.append(m_o)
    cache_module_permissions[administrador.tipo] = final_list

    return final_list


def resolve_module(args, info, idadministrador, module):
    administrador = resolve_administrador(args, info, idadministrador)
    if administrador == None:
        return None

    if administrador.tipo in cache_detail and module in cache_detail[administrador.tipo]:
        return cache_detail[administrador.tipo][module]

    filtered_module = filter_permissions(module_list, administrador.tipo)
    module_detail = next(item for item in filtered_module if item["module"] == module)

    m_o = module_object(**module_detail)
    # for k, v in module_detail.items():
    #     setattr(m_o, k, v)

    if administrador.tipo not in cache_detail:
        cache_detail[administrador.tipo] = {}

    if module not in cache_detail[administrador.tipo]:
        cache_detail[administrador.tipo][module] = m_o

    return m_o


all_module = graphene.List(module_object, idadministrador=graphene.Int(required=True))
module = graphene.Field( module_object, idadministrador=graphene.Int(required=True), module=graphene.String(required=True))

