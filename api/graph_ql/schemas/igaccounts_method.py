
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import igaccounts_model
from ..resolver import resolve

# __REPLACE
class igaccounts_schema(SQLAlchemyObjectType):
    class Meta:
        model = igaccounts_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idigaccounts','pk','username','full_name','profile_pic_url','biography','follower_count','following_count','has_anonymous_profile_picture','is_private','is_business','is_verified','media_count','fecha','following','follower','favorito','hashtag']


def resolve_igaccounts( args, info,idigaccounts, **kwargs ):
    query= resolve(args,info,igaccounts_schema,igaccounts_model,idigaccounts=idigaccounts,**kwargs)
    return query.first()

def resolve_all_igaccounts( args, info, **kwargs):
    query= resolve(args,info,igaccounts_schema,igaccounts_model,**kwargs)
    return query



all_igaccounts = SQLAlchemyConnectionField(igaccounts_schema,pk=graphene.String(),username=graphene.String(),full_name=graphene.String(),profile_pic_url=graphene.String(),biography=graphene.String(),follower_count=graphene.Int(),following_count=graphene.Int(),has_anonymous_profile_picture=graphene.Boolean(),is_private=graphene.Boolean(),is_business=graphene.Boolean(),is_verified=graphene.Boolean(),media_count=graphene.Int(),fecha=graphene.types.datetime.DateTime(),following=graphene.Boolean(),follower=graphene.Boolean(),favorito=graphene.Boolean(),hashtag=graphene.String())
igaccounts = graphene.Field(igaccounts_schema,idigaccounts=graphene.Int(),pk=graphene.String(),username=graphene.String(),full_name=graphene.String(),profile_pic_url=graphene.String(),biography=graphene.String(),follower_count=graphene.Int(),following_count=graphene.Int(),has_anonymous_profile_picture=graphene.Boolean(),is_private=graphene.Boolean(),is_business=graphene.Boolean(),is_verified=graphene.Boolean(),media_count=graphene.Int(),fecha=graphene.types.datetime.DateTime(),following=graphene.Boolean(),follower=graphene.Boolean(),favorito=graphene.Boolean(),hashtag=graphene.String())

# __REPLACE