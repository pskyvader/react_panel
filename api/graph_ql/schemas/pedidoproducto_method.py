
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import pedidoproducto_model
from ..resolver import resolve

# __REPLACE
class pedidoproducto_schema(SQLAlchemyObjectType):
    class Meta:
        model = pedidoproducto_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idpedidoproducto','idpedido','idpedidodireccion','idproducto','titulo','foto','mensaje','idproductoatributo','titulo_atributo','precio','cantidad','total']


def resolve_pedidoproducto( args, info,idpedidoproducto, **kwargs ):
    query= resolve(args,info,pedidoproducto_schema,pedidoproducto_model,idpedidoproducto=idpedidoproducto,**kwargs)
    return query.first()

def resolve_all_pedidoproducto( args, info, **kwargs):
    query= resolve(args,info,pedidoproducto_schema,pedidoproducto_model,**kwargs)
    return query



all_pedidoproducto = SQLAlchemyConnectionField(pedidoproducto_schema,idpedido=graphene.Int(),idpedidodireccion=graphene.Int(),idproducto=graphene.Int(),titulo=graphene.String(),mensaje=graphene.String(),idproductoatributo=graphene.Int(),titulo_atributo=graphene.String(),precio=graphene.Int(),cantidad=graphene.Int(),total=graphene.Int())
pedidoproducto = graphene.Field(pedidoproducto_schema,idpedidoproducto=graphene.Int(),idpedido=graphene.Int(),idpedidodireccion=graphene.Int(),idproducto=graphene.Int(),titulo=graphene.String(),mensaje=graphene.String(),idproductoatributo=graphene.Int(),titulo_atributo=graphene.String(),precio=graphene.Int(),cantidad=graphene.Int(),total=graphene.Int())

# __REPLACE