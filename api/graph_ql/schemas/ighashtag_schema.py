
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import ighashtag_model
from ..resolver import resolve
from ..mutator import mutation_create,mutation_update

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

all_ighashtag = SQLAlchemyConnectionField(ighashtag_schema,sort=graphene.String(),hashtag=graphene.String(),following=graphene.Int(),follower=graphene.Int(),removed=graphene.Int(),eficiencia=graphene.Int(),eficiencia2=graphene.Int(),total=graphene.Int(),orden=graphene.Int(),estado=graphene.Boolean())
ighashtag = graphene.Field(ighashtag_schema,idighashtag=graphene.Int(),hashtag=graphene.String(),following=graphene.Int(),follower=graphene.Int(),removed=graphene.Int(),eficiencia=graphene.Int(),eficiencia2=graphene.Int(),total=graphene.Int(),orden=graphene.Int(),estado=graphene.Boolean())

# Create a generic class to mutualize description of ighashtag _attributes for both queries and mutations
class ighashtag_attribute:
    # name = graphene.String(description="Name of the ighashtag.")
    hashtag=graphene.String()
    following=graphene.Int()
    follower=graphene.Int()
    removed=graphene.Int()
    eficiencia=graphene.Int()
    eficiencia2=graphene.Int()
    total=graphene.Int()
    orden=graphene.Int()
    estado=graphene.Boolean()
   

class create_ighashtag_input(graphene.InputObjectType, ighashtag_attribute):
    """Arguments to create a ighashtag."""
    pass

class create_ighashtag(graphene.Mutation):
    """Mutation to create a ighashtag."""
    ighashtag = graphene.Field(lambda: ighashtag_schema, description="ighashtag created by this mutation.")

    class Arguments:
        input = create_ighashtag_input(required=True)

    def mutate(self, info, input):
        ighashtag=mutation_create(ighashtag_model,input,'idighashtag')
        return create_ighashtag(ighashtag=ighashtag)

class update_ighashtag_input(graphene.InputObjectType, ighashtag_attribute):
    """Arguments to update a ighashtag."""
    idighashtag = graphene.ID(required=True, description="Global Id of the ighashtag.")

class update_ighashtag(graphene.Mutation):
    """Update a ighashtag."""
    ighashtag = graphene.Field(lambda: ighashtag_schema, description="ighashtag updated by this mutation.")

    class Arguments:
        input = update_ighashtag_input(required=True)

    def mutate(self, info, input):
        ighashtag=mutation_update(ighashtag_model,input,'idighashtag')
        return update_ighashtag(ighashtag=ighashtag)