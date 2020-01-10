
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import productocategoria_model
from ..resolver import resolve

# __REPLACE
class productocategoria_schema(SQLAlchemyObjectType):
    class Meta:
        model = productocategoria_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idproductocategoria','idpadre','tipo','titulo','url','foto','descuento','descuento_fecha','resumen','descripcion','keywords','metadescripcion','orden','estado','destacado']


def resolve_productocategoria( args, info,idproductocategoria, **kwargs ):
    query= resolve(args,info,productocategoria_schema,productocategoria_model,idproductocategoria=idproductocategoria,**kwargs)
    return query.first()

def resolve_all_productocategoria( args, info, **kwargs):
    query= resolve(args,info,productocategoria_schema,productocategoria_model,**kwargs)
    return query



all_productocategoria = SQLAlchemyConnectionField(productocategoria_schema,idpadre=graphene.String(),tipo=graphene.Int(),titulo=graphene.String(),url=graphene.String(),descuento=graphene.Int(),descuento_fecha=graphene.String(),resumen=graphene.String(),descripcion=graphene.String(),keywords=graphene.String(),metadescripcion=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean(),destacado=graphene.Boolean())
productocategoria = graphene.Field(productocategoria_schema,idproductocategoria=graphene.Int(),idpadre=graphene.String(),tipo=graphene.Int(),titulo=graphene.String(),url=graphene.String(),descuento=graphene.Int(),descuento_fecha=graphene.String(),resumen=graphene.String(),descripcion=graphene.String(),keywords=graphene.String(),metadescripcion=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean(),destacado=graphene.Boolean())

# __REPLACE