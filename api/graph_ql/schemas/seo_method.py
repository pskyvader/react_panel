
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import seo_model
from ..resolver import resolve

# __REPLACE
class seo_schema(SQLAlchemyObjectType):
    class Meta:
        model = seo_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idseo','titulo','url','subtitulo','foto','banner','modulo_front','modulo_back','tipo_modulo','link_menu','keywords','metadescripcion','orden','menu','submenu','estado']


def resolve_seo( args, info,idseo, **kwargs ):
    query= resolve(args,info,seo_schema,seo_model,idseo=idseo,**kwargs)
    return query.first()

def resolve_all_seo( args, info, **kwargs):
    query= resolve(args,info,seo_schema,seo_model,**kwargs)
    return query



all_seo = SQLAlchemyConnectionField(seo_schema,titulo=graphene.String(),url=graphene.String(),subtitulo=graphene.String(),modulo_front=graphene.String(),modulo_back=graphene.String(),tipo_modulo=graphene.Int(),link_menu=graphene.String(),keywords=graphene.String(),metadescripcion=graphene.String(),orden=graphene.Int(),menu=graphene.Boolean(),submenu=graphene.Boolean(),estado=graphene.Boolean())
seo = graphene.Field(seo_schema,idseo=graphene.Int(),titulo=graphene.String(),url=graphene.String(),subtitulo=graphene.String(),modulo_front=graphene.String(),modulo_back=graphene.String(),tipo_modulo=graphene.Int(),link_menu=graphene.String(),keywords=graphene.String(),metadescripcion=graphene.String(),orden=graphene.Int(),menu=graphene.Boolean(),submenu=graphene.Boolean(),estado=graphene.Boolean())

# __REPLACE