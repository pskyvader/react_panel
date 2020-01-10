
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import log_model
from ..resolver import resolve

# __REPLACE
class log_schema(SQLAlchemyObjectType):
    class Meta:
        model = log_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idlog','administrador','tabla','accion','fecha']


def resolve_log( args, info,idlog, **kwargs ):
    query= resolve(args,info,log_schema,log_model,idlog=idlog,**kwargs)
    return query.first()

def resolve_all_log( args, info, **kwargs):
    query= resolve(args,info,log_schema,log_model,**kwargs)
    return query



all_log = SQLAlchemyConnectionField(log_schema,administrador=graphene.String(),tabla=graphene.String(),accion=graphene.String(),fecha=graphene.types.datetime.DateTime())
log = graphene.Field(log_schema,idlog=graphene.Int(),administrador=graphene.String(),tabla=graphene.String(),accion=graphene.String(),fecha=graphene.types.datetime.DateTime())

# __REPLACE