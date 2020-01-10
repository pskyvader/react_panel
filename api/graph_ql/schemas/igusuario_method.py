
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import igusuario_model
from ..resolver import resolve

# __REPLACE
class igusuario_schema(SQLAlchemyObjectType):
    class Meta:
        model = igusuario_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idigusuario','usuario','estado']


def resolve_igusuario( args, info,idigusuario, **kwargs ):
    query= resolve(args,info,igusuario_schema,igusuario_model,idigusuario=idigusuario,**kwargs)
    return query.first()

def resolve_all_igusuario( args, info, **kwargs):
    query= resolve(args,info,igusuario_schema,igusuario_model,**kwargs)
    return query



all_igusuario = SQLAlchemyConnectionField(igusuario_schema,usuario=graphene.String(),estado=graphene.Boolean())
igusuario = graphene.Field(igusuario_schema,idigusuario=graphene.Int(),usuario=graphene.String(),estado=graphene.Boolean())

# __REPLACE