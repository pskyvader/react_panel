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

cache_module_permissions={}


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
    estado=graphene.Boolean()
    menu=graphene.List(permisos_detail_object)
    mostrar=graphene.List(permisos_detail_object)
    detalle=graphene.List(permisos_detail_object)

    def resolve_menu(parent,info,*args, **kwargs):
        list_menu=[]
        for k,m in parent['menu'].items():
            list_menu.append(permisos_detail_object(field=k,estado=m))
        return list_menu




class module_configuration_object(graphene.ObjectType):
    tipo=graphene.Int()
    titulo=graphene.String()
    orden=graphene.Int()
    aside=graphene.Boolean()
    hijos=graphene.Boolean()
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



def check_permisos(hijos,tipo):
    for hijo in hijos:
        if hijo['aside'] and str(tipo) in hijo['permisos'] and hijo['permisos'][str(tipo)]['estado']:
            return True
    
    return False

def filter_permissions(list,tipo):
    module_list_final={}

    for k,v in list.items():
        c_module=v.copy()
        c_module['hijo']=[]
        for hijo in v['hijo']:
            c_hijo=hijo.copy()
            c_hijo['permisos']={}
            if str(tipo) in hijo['permisos'] and hijo['permisos'][str(tipo)]['estado']:
                c_hijo['permisos']=hijo['permisos'][str(tipo)]
            if c_hijo['permisos']!={}:
                c_module['hijo'].append(c_hijo)
        if c_module['hijo']!=[]:
            module_list_final[c_module['orden']]=c_module

    return [v for k, v in sorted(module_list_final.items(), key=lambda item: item[0])]


def resolve_all_module(args, info, idadministrador):
    administrador=resolve_administrador(args, info,idadministrador)
    if administrador==None:
        return []
    
    filtered_module_list={x:v for x,v in module_list.items() if v['estado'] and v['aside'] and len(v['hijo'])>0 and check_permisos(v['hijo'],administrador.tipo) }
    filtered_module=filter_permissions(filtered_module_list,administrador.tipo)


    final_list=[]
    for m in filtered_module:
        m_o=module_object()
        for k, v in m.items():
            setattr(m_o, k, v)
                    

        final_list.append(m_o)

    cache_module_permissions[administrador.tipo]=final_list

    return final_list


all_module = graphene.List( module_object, idadministrador=graphene.Int() )