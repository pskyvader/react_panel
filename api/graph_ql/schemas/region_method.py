
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import region_model
from ..resolver import resolve

# __REPLACE
class region_schema(SQLAlchemyObjectType):
    class Meta:
        model = region_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idregion','titulo','precio','orden','estado']


def resolve_region( args, info,idregion, **kwargs ):
    query= resolve(args,info,region_schema,region_model,idregion=idregion,**kwargs)
    return query.first()

def resolve_all_region( args, info, **kwargs):
    query= resolve(args,info,region_schema,region_model,**kwargs)
    return query



all_region = SQLAlchemyConnectionField(region_schema,titulo=graphene.String(),precio=graphene.Int(),orden=graphene.Int(),estado=graphene.Boolean())
region = graphene.Field(region_schema,idregion=graphene.Int(),titulo=graphene.String(),precio=graphene.Int(),orden=graphene.Int(),estado=graphene.Boolean())

# __REPLACE