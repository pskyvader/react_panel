
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import sitemap_model
from ..resolver import resolve

# __REPLACE
class sitemap_schema(SQLAlchemyObjectType):
    class Meta:
        model = sitemap_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idsitemap','idpadre','url','depth','valid','ready']


def resolve_sitemap( args, info,idsitemap, **kwargs ):
    query= resolve(args,info,sitemap_schema,sitemap_model,idsitemap=idsitemap,**kwargs)
    return query.first()

def resolve_all_sitemap( args, info, **kwargs):
    query= resolve(args,info,sitemap_schema,sitemap_model,**kwargs)
    return query



all_sitemap = SQLAlchemyConnectionField(sitemap_schema,idpadre=graphene.Int(),url=graphene.String(),depth=graphene.Int(),valid=graphene.String(),ready=graphene.Boolean())
sitemap = graphene.Field(sitemap_schema,idsitemap=graphene.Int(),idpadre=graphene.Int(),url=graphene.String(),depth=graphene.Int(),valid=graphene.String(),ready=graphene.Boolean())

# __REPLACE