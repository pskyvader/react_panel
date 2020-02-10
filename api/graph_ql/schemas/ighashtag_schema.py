from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import ighashtag_model
from ..resolver import resolve
from ..mutator import mutation_create, mutation_update, mutation_delete
from .. import url_schema


attribute = dict(
    hashtag=graphene.String(),
    following=graphene.Int(),
    follower=graphene.Int(),
    removed=graphene.Int(),
    eficiencia=graphene.Int(),
    eficiencia2=graphene.Int(),
    total=graphene.Int(),
    orden=graphene.Int(),
    estado=graphene.Boolean()
    )
read_only_attribute = dict(
    
    )
black_list_attribute = dict(
    
    )


class ighashtag_schema(SQLAlchemyObjectType):
    class Meta:
        model = ighashtag_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idighashtag"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )
    
    


def resolve_ighashtag(args, info, idighashtag, **kwargs):
    query = resolve(
        args, info, ighashtag_schema, ighashtag_model, idighashtag=idighashtag, **kwargs
    )
    return query.first()


def resolve_all_ighashtag(args, info, **kwargs):
    query = resolve(args, info, ighashtag_schema, ighashtag_model, **kwargs)
    return query


all_ighashtag = SQLAlchemyConnectionField( ighashtag_schema, sort=graphene.String(), **attribute )
ighashtag = graphene.Field(ighashtag_schema, idighashtag=graphene.Int(), **attribute)

# Create a generic class to mutualize description of ighashtag _attributes for both queries and mutations
class ighashtag_attribute:
    # name = graphene.String(description="Name of the ighashtag.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(ighashtag_attribute, name, value)


class create_ighashtag_input(graphene.InputObjectType, ighashtag_attribute):
    """Arguments to create a ighashtag."""

    pass


class create_ighashtag(graphene.Mutation):
    """Mutation to create a ighashtag."""

    ighashtag = graphene.Field(
        ighashtag_schema, description="ighashtag created by this mutation."
    )

    class Arguments:
        input = create_ighashtag_input(required=True)

    def mutate(self, info, input):
        ighashtag = mutation_create(ighashtag_model, input, "idighashtag",info)
        return create_ighashtag(ighashtag=ighashtag)


class update_ighashtag_input(graphene.InputObjectType, ighashtag_attribute):
    """Arguments to update a ighashtag."""

    idighashtag = graphene.ID(required=True, description="Global Id of the ighashtag.")


class update_ighashtag(graphene.Mutation):
    """Update a ighashtag."""

    ighashtag = graphene.Field(
        ighashtag_schema, description="ighashtag updated by this mutation."
    )

    class Arguments:
        input = update_ighashtag_input(required=True)

    def mutate(self, info, input):
        ighashtag = mutation_update(ighashtag_model, input, "idighashtag",info)
        return update_ighashtag(ighashtag=ighashtag)


class delete_ighashtag_input(graphene.InputObjectType, ighashtag_attribute):
    """Arguments to delete a ighashtag."""

    idighashtag = graphene.ID(required=True, description="Global Id of the ighashtag.")


class delete_ighashtag(graphene.Mutation):
    """delete a ighashtag."""

    ok = graphene.Boolean(description="ighashtag deleted correctly.")
    message = graphene.String(description="ighashtag deleted message.")

    class Arguments:
        input = delete_ighashtag_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(ighashtag_model, input, "idighashtag")
        return delete_ighashtag(ok=ok, message=message)
