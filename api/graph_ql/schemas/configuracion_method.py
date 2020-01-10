
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import configuracion_model
from ..resolver import resolve

# __REPLACE
class configuracion_schema(SQLAlchemyObjectType):
    class Meta:
        model = configuracion_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idconfiguracion','variable','valor']


def resolve_configuracion( args, info,idconfiguracion, **kwargs ):
    query= resolve(args,info,configuracion_schema,configuracion_model,idconfiguracion=idconfiguracion,**kwargs)
    return query.first()

def resolve_all_configuracion( args, info, **kwargs):
    query= resolve(args,info,configuracion_schema,configuracion_model,**kwargs)
    return query



all_configuracion = SQLAlchemyConnectionField(configuracion_schema,variable=graphene.String(),valor=graphene.String())
configuracion = graphene.Field(configuracion_schema,idconfiguracion=graphene.Int(),variable=graphene.String(),valor=graphene.String())

# __REPLACE