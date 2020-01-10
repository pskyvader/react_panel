
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import seccion_model
from ..resolver import resolve

# __REPLACE
class seccion_schema(SQLAlchemyObjectType):
    class Meta:
        model = seccion_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idseccion','idseccioncategoria','tipo','titulo','subtitulo','url','foto','archivo','resumen','descripcion','keywords','metadescripcion','orden','estado','destacado']


def resolve_seccion( args, info,idseccion, **kwargs ):
    query= resolve(args,info,seccion_schema,seccion_model,idseccion=idseccion,**kwargs)
    return query.first()

def resolve_all_seccion( args, info, **kwargs):
    query= resolve(args,info,seccion_schema,seccion_model,**kwargs)
    return query



all_seccion = SQLAlchemyConnectionField(seccion_schema,idseccioncategoria=graphene.String(),tipo=graphene.Int(),titulo=graphene.String(),subtitulo=graphene.String(),url=graphene.String(),resumen=graphene.String(),descripcion=graphene.String(),keywords=graphene.String(),metadescripcion=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean(),destacado=graphene.Boolean())
seccion = graphene.Field(seccion_schema,idseccion=graphene.Int(),idseccioncategoria=graphene.String(),tipo=graphene.Int(),titulo=graphene.String(),subtitulo=graphene.String(),url=graphene.String(),resumen=graphene.String(),descripcion=graphene.String(),keywords=graphene.String(),metadescripcion=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean(),destacado=graphene.Boolean())

# __REPLACE