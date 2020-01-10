
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import seccioncategoria_model
from ..resolver import resolve

# __REPLACE
class seccioncategoria_schema(SQLAlchemyObjectType):
    class Meta:
        model = seccioncategoria_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idseccioncategoria','idpadre','tipo','titulo','url','foto','resumen','descripcion','keywords','metadescripcion','orden','estado','destacado']


def resolve_seccioncategoria( args, info,idseccioncategoria, **kwargs ):
    query= resolve(args,info,seccioncategoria_schema,seccioncategoria_model,idseccioncategoria=idseccioncategoria,**kwargs)
    return query.first()

def resolve_all_seccioncategoria( args, info, **kwargs):
    query= resolve(args,info,seccioncategoria_schema,seccioncategoria_model,**kwargs)
    return query



all_seccioncategoria = SQLAlchemyConnectionField(seccioncategoria_schema,idpadre=graphene.String(),tipo=graphene.Int(),titulo=graphene.String(),url=graphene.String(),resumen=graphene.String(),descripcion=graphene.String(),keywords=graphene.String(),metadescripcion=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean(),destacado=graphene.Boolean())
seccioncategoria = graphene.Field(seccioncategoria_schema,idseccioncategoria=graphene.Int(),idpadre=graphene.String(),tipo=graphene.Int(),titulo=graphene.String(),url=graphene.String(),resumen=graphene.String(),descripcion=graphene.String(),keywords=graphene.String(),metadescripcion=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean(),destacado=graphene.Boolean())

# __REPLACE