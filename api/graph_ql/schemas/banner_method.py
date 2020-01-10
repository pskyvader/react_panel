
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import banner_model
from ..resolver import resolve

# __REPLACE
class banner_schema(SQLAlchemyObjectType):
    class Meta:
        model = banner_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idbanner','tipo','titulo','texto1','texto2','texto3','texto','link','foto','orden','estado']


def resolve_banner( args, info,idbanner, **kwargs ):
    query= resolve(args,info,banner_schema,banner_model,idbanner=idbanner,**kwargs)
    return query.first()

def resolve_all_banner( args, info, **kwargs):
    query= resolve(args,info,banner_schema,banner_model,**kwargs)
    return query



all_banner = SQLAlchemyConnectionField(banner_schema,tipo=graphene.Int(),titulo=graphene.String(),texto1=graphene.String(),texto2=graphene.String(),texto3=graphene.String(),texto=graphene.String(),link=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean())
banner = graphene.Field(banner_schema,idbanner=graphene.Int(),tipo=graphene.Int(),titulo=graphene.String(),texto1=graphene.String(),texto2=graphene.String(),texto3=graphene.String(),texto=graphene.String(),link=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean())

# __REPLACE