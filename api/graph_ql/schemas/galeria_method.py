
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import galeria_model
from ..resolver import resolve

# __REPLACE
class galeria_schema(SQLAlchemyObjectType):
    class Meta:
        model = galeria_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idgaleria','tipo','titulo','url','subtitulo','foto','resumen','keywords','metadescripcion','orden','estado']


def resolve_galeria( args, info,idgaleria, **kwargs ):
    query= resolve(args,info,galeria_schema,galeria_model,idgaleria=idgaleria,**kwargs)
    return query.first()

def resolve_all_galeria( args, info, **kwargs):
    query= resolve(args,info,galeria_schema,galeria_model,**kwargs)
    return query



all_galeria = SQLAlchemyConnectionField(galeria_schema,tipo=graphene.Int(),titulo=graphene.String(),url=graphene.String(),subtitulo=graphene.String(),resumen=graphene.String(),keywords=graphene.String(),metadescripcion=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean())
galeria = graphene.Field(galeria_schema,idgaleria=graphene.Int(),tipo=graphene.Int(),titulo=graphene.String(),url=graphene.String(),subtitulo=graphene.String(),resumen=graphene.String(),keywords=graphene.String(),metadescripcion=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean())

# __REPLACE