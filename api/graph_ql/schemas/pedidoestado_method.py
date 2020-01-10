
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import pedidoestado_model
from ..resolver import resolve

# __REPLACE
class pedidoestado_schema(SQLAlchemyObjectType):
    class Meta:
        model = pedidoestado_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idpedidoestado','tipo','titulo','resumen','color','orden','estado']


def resolve_pedidoestado( args, info,idpedidoestado, **kwargs ):
    query= resolve(args,info,pedidoestado_schema,pedidoestado_model,idpedidoestado=idpedidoestado,**kwargs)
    return query.first()

def resolve_all_pedidoestado( args, info, **kwargs):
    query= resolve(args,info,pedidoestado_schema,pedidoestado_model,**kwargs)
    return query



all_pedidoestado = SQLAlchemyConnectionField(pedidoestado_schema,tipo=graphene.Int(),titulo=graphene.String(),resumen=graphene.String(),color=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean())
pedidoestado = graphene.Field(pedidoestado_schema,idpedidoestado=graphene.Int(),tipo=graphene.Int(),titulo=graphene.String(),resumen=graphene.String(),color=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean())

# __REPLACE