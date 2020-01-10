
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import producto_model
from ..resolver import resolve

# __REPLACE
class producto_schema(SQLAlchemyObjectType):
    class Meta:
        model = producto_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idproducto','idproductocategoria','tipo','titulo','url','foto','archivo','codigo','precio','descuento','descuento_fecha','stock','ventas','resumen','descripcion','keywords','metadescripcion','orden','estado','destacado']


def resolve_producto( args, info,idproducto, **kwargs ):
    query= resolve(args,info,producto_schema,producto_model,idproducto=idproducto,**kwargs)
    return query.first()

def resolve_all_producto( args, info, **kwargs):
    query= resolve(args,info,producto_schema,producto_model,**kwargs)
    return query



all_producto = SQLAlchemyConnectionField(producto_schema,idproductocategoria=graphene.String(),tipo=graphene.Int(),titulo=graphene.String(),url=graphene.String(),codigo=graphene.String(),precio=graphene.Int(),descuento=graphene.Int(),descuento_fecha=graphene.String(),stock=graphene.Int(),ventas=graphene.Int(),resumen=graphene.String(),descripcion=graphene.String(),keywords=graphene.String(),metadescripcion=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean(),destacado=graphene.Boolean())
producto = graphene.Field(producto_schema,idproducto=graphene.Int(),idproductocategoria=graphene.String(),tipo=graphene.Int(),titulo=graphene.String(),url=graphene.String(),codigo=graphene.String(),precio=graphene.Int(),descuento=graphene.Int(),descuento_fecha=graphene.String(),stock=graphene.Int(),ventas=graphene.Int(),resumen=graphene.String(),descripcion=graphene.String(),keywords=graphene.String(),metadescripcion=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean(),destacado=graphene.Boolean())

# __REPLACE