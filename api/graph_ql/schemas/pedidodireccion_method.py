
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import pedidodireccion_model
from ..resolver import resolve

# __REPLACE
class pedidodireccion_schema(SQLAlchemyObjectType):
    class Meta:
        model = pedidodireccion_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idpedidodireccion','idpedido','idusuariodireccion','idpedidoestado','precio','cookie_direccion','nombre','telefono','direccion_completa','referencias','fecha_entrega']


def resolve_pedidodireccion( args, info,idpedidodireccion, **kwargs ):
    query= resolve(args,info,pedidodireccion_schema,pedidodireccion_model,idpedidodireccion=idpedidodireccion,**kwargs)
    return query.first()

def resolve_all_pedidodireccion( args, info, **kwargs):
    query= resolve(args,info,pedidodireccion_schema,pedidodireccion_model,**kwargs)
    return query



all_pedidodireccion = SQLAlchemyConnectionField(pedidodireccion_schema,idpedido=graphene.Int(),idusuariodireccion=graphene.Int(),idpedidoestado=graphene.Int(),precio=graphene.Int(),cookie_direccion=graphene.String(),nombre=graphene.String(),telefono=graphene.String(),direccion_completa=graphene.String(),referencias=graphene.String(),fecha_entrega=graphene.types.datetime.DateTime())
pedidodireccion = graphene.Field(pedidodireccion_schema,idpedidodireccion=graphene.Int(),idpedido=graphene.Int(),idusuariodireccion=graphene.Int(),idpedidoestado=graphene.Int(),precio=graphene.Int(),cookie_direccion=graphene.String(),nombre=graphene.String(),telefono=graphene.String(),direccion_completa=graphene.String(),referencias=graphene.String(),fecha_entrega=graphene.types.datetime.DateTime())

# __REPLACE