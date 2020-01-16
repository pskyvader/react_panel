
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import igaccounts_model
from ..resolver import resolve
from ..mutator import mutation_create

# __REPLACE__

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
    print('QUERY',query)
    return query



all_igaccounts = SQLAlchemyConnectionField(igaccounts_schema,pk=graphene.String(),username=graphene.String(),full_name=graphene.String(),profile_pic_url=graphene.String(),biography=graphene.String(),follower_count=graphene.Int(),following_count=graphene.Int(),has_anonymous_profile_picture=graphene.Boolean(),is_private=graphene.Boolean(),is_business=graphene.Boolean(),is_verified=graphene.Boolean(),media_count=graphene.Int(),fecha=graphene.types.datetime.DateTime(),following=graphene.Boolean(),follower=graphene.Boolean(),favorito=graphene.Boolean(),hashtag=graphene.String())
igaccounts = graphene.Field(igaccounts_schema,idigaccounts=graphene.Int(),pk=graphene.String(),username=graphene.String(),full_name=graphene.String(),profile_pic_url=graphene.String(),biography=graphene.String(),follower_count=graphene.Int(),following_count=graphene.Int(),has_anonymous_profile_picture=graphene.Boolean(),is_private=graphene.Boolean(),is_business=graphene.Boolean(),is_verified=graphene.Boolean(),media_count=graphene.Int(),fecha=graphene.types.datetime.DateTime(),following=graphene.Boolean(),follower=graphene.Boolean(),favorito=graphene.Boolean(),hashtag=graphene.String())

# __REPLACE__



# Create a generic class to mutualize description of igaccounts _attributes for both queries and mutations
class igaccounts_attribute:
    # name = graphene.String(description="Name of the igaccounts.")
    pk=graphene.String()
    username=graphene.String()
    full_name=graphene.String()
    profile_pic_url=graphene.String()
    biography=graphene.String()
    follower_count=graphene.Int()
    following_count=graphene.Int()
    has_anonymous_profile_picture=graphene.Boolean()
    is_private=graphene.Boolean()
    is_business=graphene.Boolean()
    is_verified=graphene.Boolean()
    media_count=graphene.Int()
    fecha=graphene.types.datetime.DateTime()
    following=graphene.Boolean()
    follower=graphene.Boolean()
    favorito=graphene.Boolean()
    hashtag=graphene.String()
   



class create_igaccounts_input(graphene.InputObjectType, igaccounts_attribute):
    """Arguments to create a igaccounts."""
    pass


class create_igaccounts(graphene.Mutation):
    """Mutation to create a igaccounts."""
    igaccounts = graphene.Field(lambda: igaccounts_schema, description="igaccounts created by this mutation.")

    class Arguments:
        input = create_igaccounts_input(required=True)

    def mutate(self, info, input):
        igaccounts=mutation_create(igaccounts_model,idigaccounts)

        return create_igaccounts(igaccounts=igaccounts)


class update_igaccounts_input(graphene.InputObjectType, igaccounts_attribute):
    """Arguments to update a igaccounts."""
    idigaccounts = graphene.ID(required=True, description="Global Id of the igaccounts.")


class update_igaccounts(graphene.Mutation):
    """Update a igaccounts."""
    igaccounts = graphene.Field(lambda: igaccounts_schema, description="igaccounts updated by this mutation.")

    class Arguments:
        input = update_igaccounts_input(required=True)

    def mutate(self, info, input):
        igaccounts=mutation_update(igaccounts_model,idigaccounts)
        return update_igaccounts(igaccounts=igaccounts)