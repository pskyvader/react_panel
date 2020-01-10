
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import mediopago_model
from ..resolver import resolve

# __REPLACE
class mediopago_schema(SQLAlchemyObjectType):
    class Meta:
        model = mediopago_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idmediopago','titulo','resumen','descripcion','orden','estado']


def resolve_mediopago( args, info,idmediopago, **kwargs ):
    query= resolve(args,info,mediopago_schema,mediopago_model,idmediopago=idmediopago,**kwargs)
    return query.first()

def resolve_all_mediopago( args, info, **kwargs):
    query= resolve(args,info,mediopago_schema,mediopago_model,**kwargs)
    return query



all_mediopago = SQLAlchemyConnectionField(mediopago_schema,titulo=graphene.String(),resumen=graphene.String(),descripcion=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean())
mediopago = graphene.Field(mediopago_schema,idmediopago=graphene.Int(),titulo=graphene.String(),resumen=graphene.String(),descripcion=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean())

# __REPLACE