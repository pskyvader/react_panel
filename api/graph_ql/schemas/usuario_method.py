
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import usuario_model
from ..resolver import resolve

# __REPLACE
class usuario_schema(SQLAlchemyObjectType):
    class Meta:
        model = usuario_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idusuario','tipo','nombre','telefono','email','foto','estado','cookie']


def resolve_usuario( args, info,idusuario, **kwargs ):
    query= resolve(args,info,usuario_schema,usuario_model,idusuario=idusuario,**kwargs)
    return query.first()

def resolve_all_usuario( args, info, **kwargs):
    query= resolve(args,info,usuario_schema,usuario_model,**kwargs)
    return query



all_usuario = SQLAlchemyConnectionField(usuario_schema,tipo=graphene.Int(),nombre=graphene.String(),telefono=graphene.String(),email=graphene.String(),estado=graphene.Boolean(),cookie=graphene.String())
usuario = graphene.Field(usuario_schema,idusuario=graphene.Int(),tipo=graphene.Int(),nombre=graphene.String(),telefono=graphene.String(),email=graphene.String(),estado=graphene.Boolean(),cookie=graphene.String())

# __REPLACE