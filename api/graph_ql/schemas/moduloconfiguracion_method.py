
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import moduloconfiguracion_model
from ..resolver import resolve

# __REPLACE
class moduloconfiguracion_schema(SQLAlchemyObjectType):
    class Meta:
        model = moduloconfiguracion_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idmoduloconfiguracion','icono','module','titulo','sub','padre','mostrar','detalle','orden','estado','aside','tipos']


def resolve_moduloconfiguracion( args, info,idmoduloconfiguracion, **kwargs ):
    query= resolve(args,info,moduloconfiguracion_schema,moduloconfiguracion_model,idmoduloconfiguracion=idmoduloconfiguracion,**kwargs)
    return query.first()

def resolve_all_moduloconfiguracion( args, info, **kwargs):
    query= resolve(args,info,moduloconfiguracion_schema,moduloconfiguracion_model,**kwargs)
    return query



all_moduloconfiguracion = SQLAlchemyConnectionField(moduloconfiguracion_schema,icono=graphene.String(),module=graphene.String(),titulo=graphene.String(),sub=graphene.String(),padre=graphene.String(),mostrar=graphene.String(),detalle=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean(),aside=graphene.Boolean(),tipos=graphene.Boolean())
moduloconfiguracion = graphene.Field(moduloconfiguracion_schema,idmoduloconfiguracion=graphene.Int(),icono=graphene.String(),module=graphene.String(),titulo=graphene.String(),sub=graphene.String(),padre=graphene.String(),mostrar=graphene.String(),detalle=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean(),aside=graphene.Boolean(),tipos=graphene.Boolean())

# __REPLACE