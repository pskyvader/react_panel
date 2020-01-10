
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import texto_model
from ..resolver import resolve

# __REPLACE
class texto_schema(SQLAlchemyObjectType):
    class Meta:
        model = texto_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idtexto','tipo','titulo','url','descripcion','texto','mapa','orden','estado']


def resolve_texto( args, info,idtexto, **kwargs ):
    query= resolve(args,info,texto_schema,texto_model,idtexto=idtexto,**kwargs)
    return query.first()

def resolve_all_texto( args, info, **kwargs):
    query= resolve(args,info,texto_schema,texto_model,**kwargs)
    return query



all_texto = SQLAlchemyConnectionField(texto_schema,tipo=graphene.String(),titulo=graphene.String(),url=graphene.String(),descripcion=graphene.String(),texto=graphene.String(),mapa=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean())
texto = graphene.Field(texto_schema,idtexto=graphene.Int(),tipo=graphene.String(),titulo=graphene.String(),url=graphene.String(),descripcion=graphene.String(),texto=graphene.String(),mapa=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean())

# __REPLACE