import graphene
from graph_ql.schemas.administrador_schema import resolve_administrador

import json
from os.path import join, dirname
from utils.conversion import file_list,get_file


current_dir = dirname(__file__)

module_dir = join(current_dir, "..", "config", "modules")
module_list={}


json_files = file_list(module_dir)
for f in json_files:
    module_file = json.loads(get_file(join(module_dir, f)))
    module_list[module_file['module']]=module_file



class menu_object(graphene.ObjectType):
    field=graphene.String()
    titulo=graphene.String()




class mostrar_object(graphene.ObjectType):
    field=graphene.String()
    titulo=graphene.String()
    tipo=graphene.String()

class detalle_object(graphene.ObjectType):
    field=graphene.String()
    titulo=graphene.String()
    tipo=graphene.String()






class permisos_detail_object(graphene.ObjectType):
    field=graphene.String()
    estado=graphene.Boolean()
    

class permisos_object(graphene.ObjectType):
    menu=graphene.List(permisos_detail_object)
    mostrar=graphene.List(permisos_detail_object)
    detalle=graphene.List(permisos_detail_object)




class module_configuration_object(graphene.ObjectType):
    tipo=graphene.Int()
    titulo=graphene.String()
    orden=graphene.Int()
    aside=graphene.Boolean()
    hijos=graphene.Boolean()
    estado=graphene.Boolean()

    permisos=graphene.Field(permisos_object)


class module_object(graphene.ObjectType):
    icono=graphene.String()
    module=graphene.String()
    titulo=graphene.String()
    sub=graphene.String()
    padre=graphene.String()
    orden=graphene.Int()
    estado=graphene.Boolean()
    aside=graphene.Boolean()
    tipos=graphene.Boolean()

    menu=graphene.List(menu_object)
    mostrar=graphene.List(mostrar_object)
    detalle=graphene.List(detalle_object)
    hijo=graphene.List(module_configuration_object)



def check_permisos(hijo,tipo):
    if not hijo['aside']:
        return False
    
    if not str(tipo) in hijo['permisos']:
        return False
    
    return hijo['permisos'][tipo]['estado']


def resolve_all_module(args, info, idadministrador):
    administrador=resolve_administrador(args, info,idadministrador)
    if administrador==None:
        return []
    
    filtered_module_list={x for x in module_list if x['estado'] and x['aside'] and len(x['hijo'])>0}
    filtered_child_list={x for x in filtered_module_list if check_permisos(x['hijo'],administrador.tipo)}


    print(len(filtered_child_list))
    print(filtered_child_list)
    print(administrador.tipo)
    return [module_object()]


all_module = graphene.List( module_object, idadministrador=graphene.Int() )