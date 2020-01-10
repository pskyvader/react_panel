
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import ighashtag_model
from ..resolver import resolve

# __REPLACE
class ighashtag_schema(SQLAlchemyObjectType):
    class Meta:
        model = ighashtag_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idighashtag','hashtag','following','follower','removed','eficiencia','eficiencia2','total','orden','estado']


def resolve_ighashtag( args, info,idighashtag, **kwargs ):
    query= resolve(args,info,ighashtag_schema,ighashtag_model,idighashtag=idighashtag,**kwargs)
    return query.first()

def resolve_all_ighashtag( args, info, **kwargs):
    query= resolve(args,info,ighashtag_schema,ighashtag_model,**kwargs)
    return query



all_ighashtag = SQLAlchemyConnectionField(ighashtag_schema,hashtag=graphene.String(),following=graphene.Int(),follower=graphene.Int(),removed=graphene.Int(),eficiencia=graphene.Int(),eficiencia2=graphene.Int(),total=graphene.Int(),orden=graphene.Int(),estado=graphene.Boolean())
ighashtag = graphene.Field(ighashtag_schema,idighashtag=graphene.Int(),hashtag=graphene.String(),following=graphene.Int(),follower=graphene.Int(),removed=graphene.Int(),eficiencia=graphene.Int(),eficiencia2=graphene.Int(),total=graphene.Int(),orden=graphene.Int(),estado=graphene.Boolean())

# __REPLACE