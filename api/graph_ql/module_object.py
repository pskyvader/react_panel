import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from os.path import join
from graph_ql.schemas.administrador_schema import resolve_administrador


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



    
def resolve_all_module(args, info, idadministrador):
    administrador=resolve_administrador(args, info,idadministrador)
    print(administrador.tipo)
    return administrador


all_module = graphene.List( module_object, idadministrador=graphene.Int() )