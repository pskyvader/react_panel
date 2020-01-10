
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import profile_model
from ..resolver import resolve

# __REPLACE
class profile_schema(SQLAlchemyObjectType):
    class Meta:
        model = profile_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idprofile','tipo','titulo','orden','estado']


def resolve_profile( args, info,idprofile, **kwargs ):
    query= resolve(args,info,profile_schema,profile_model,idprofile=idprofile,**kwargs)
    return query.first()

def resolve_all_profile( args, info, **kwargs):
    query= resolve(args,info,profile_schema,profile_model,**kwargs)
    return query



all_profile = SQLAlchemyConnectionField(profile_schema,tipo=graphene.Int(),titulo=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean())
profile = graphene.Field(profile_schema,idprofile=graphene.Int(),tipo=graphene.Int(),titulo=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean())

# __REPLACE