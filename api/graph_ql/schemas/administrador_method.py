
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import administrador_model
from ..resolver import resolve

# __REPLACE
class administrador_schema(SQLAlchemyObjectType):
    class Meta:
        model = administrador_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idadministrador','tipo','email','nombre','foto','estado','cookie']


def resolve_administrador( args, info,idadministrador, **kwargs ):
    query= resolve(args,info,administrador_schema,administrador_model,idadministrador=idadministrador,**kwargs)
    return query.first()

def resolve_all_administrador( args, info, **kwargs):
    query= resolve(args,info,administrador_schema,administrador_model,**kwargs)
    return query



all_administrador = SQLAlchemyConnectionField(administrador_schema,tipo=graphene.Int(),email=graphene.String(),nombre=graphene.String(),estado=graphene.Boolean(),cookie=graphene.String())
administrador = graphene.Field(administrador_schema,idadministrador=graphene.Int(),tipo=graphene.Int(),email=graphene.String(),nombre=graphene.String(),estado=graphene.Boolean(),cookie=graphene.String())

# __REPLACE