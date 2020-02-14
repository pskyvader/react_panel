import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from os.path import join


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



class module_configuration_object(graphene.ObjectType):
    tipo=graphene.Int()
    titulo=graphene.String()
    orden=graphene.Int()
    aside=graphene.Boolean()
    hijos=graphene.Boolean()
    estado=graphene.Boolean()



class permisos_object(graphene.ObjectType):
    menu=graphene.List(permisos_detail_object)
    mostrar=graphene.List(permisos_detail_object)
    detalle=graphene.List(permisos_detail_object)


class permisos_detail_object(graphene.ObjectType):
    field=graphene.String()
    estado=graphene.Boolean()
    


    
def resolve_all_direccion(args, info, **kwargs):
    query = resolve(args, info, direccion_schema, direccion_model, **kwargs)
    return query


all_direccion = SQLAlchemyConnectionField( direccion_schema, sort=graphene.String(), **attribute )