from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import igaccounts_model
from ..resolver import resolve
from ..mutator import mutation_create, mutation_update, mutation_delete
from .. import url_object


attribute = dict(
    pk=graphene.String(),
    username=graphene.String(),
    full_name=graphene.String(),
    profile_pic_url=graphene.String(),
    biography=graphene.String(),
    follower_count=graphene.Int(),
    following_count=graphene.Int(),
    has_anonymous_profile_picture=graphene.Boolean(),
    is_private=graphene.Boolean(),
    is_business=graphene.Boolean(),
    is_verified=graphene.Boolean(),
    media_count=graphene.Int(),
    fecha=graphene.types.datetime.DateTime(),
    following=graphene.Boolean(),
    follower=graphene.Boolean(),
    favorito=graphene.Boolean(),
    hashtag=graphene.String()
    )
read_only_attribute = dict(
    
    )
black_list_attribute = dict(
    
    )


class igaccounts_schema(SQLAlchemyObjectType):
    class Meta:
        model = igaccounts_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idigaccounts"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )
    
    


def resolve_igaccounts(args, info, idigaccounts, **kwargs):
    query = resolve(
        args, info, igaccounts_schema, igaccounts_model, idigaccounts=idigaccounts, **kwargs
    )
    return query.first()


def resolve_all_igaccounts(args, info, **kwargs):
    query = resolve(args, info, igaccounts_schema, igaccounts_model, **kwargs)
    return query


all_igaccounts = SQLAlchemyConnectionField( igaccounts_schema, sort=graphene.String(), **attribute )
igaccounts = graphene.Field(igaccounts_schema, idigaccounts=graphene.Int(), **attribute)

# Create a generic class to mutualize description of igaccounts _attributes for both queries and mutations
class igaccounts_attribute:
    # name = graphene.String(description="Name of the igaccounts.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(igaccounts_attribute, name, value)


class create_igaccounts_input(graphene.InputObjectType, igaccounts_attribute):
    """Arguments to create a igaccounts."""

    pass


class create_igaccounts(graphene.Mutation):
    """Mutation to create a igaccounts."""

    igaccounts = graphene.Field(
        igaccounts_schema, description="igaccounts created by this mutation."
    )

    class Arguments:
        input = create_igaccounts_input(required=True)

    def mutate(self, info, input):
        igaccounts = mutation_create(igaccounts_model, input, "idigaccounts",info)
        return create_igaccounts(igaccounts=igaccounts)


class update_igaccounts_input(graphene.InputObjectType, igaccounts_attribute):
    """Arguments to update a igaccounts."""

    idigaccounts = graphene.ID(required=True, description="Global Id of the igaccounts.")


class update_igaccounts(graphene.Mutation):
    """Update a igaccounts."""

    igaccounts = graphene.Field(
        igaccounts_schema, description="igaccounts updated by this mutation."
    )

    class Arguments:
        input = update_igaccounts_input(required=True)

    def mutate(self, info, input):
        igaccounts = mutation_update(igaccounts_model, input, "idigaccounts",info)
        return update_igaccounts(igaccounts=igaccounts)


class delete_igaccounts_input(graphene.InputObjectType, igaccounts_attribute):
    """Arguments to delete a igaccounts."""

    idigaccounts = graphene.ID(required=True, description="Global Id of the igaccounts.")


class delete_igaccounts(graphene.Mutation):
    """delete a igaccounts."""

    ok = graphene.Boolean(description="igaccounts deleted correctly.")
    message = graphene.String(description="igaccounts deleted message.")

    class Arguments:
        input = delete_igaccounts_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(igaccounts_model, input, "idigaccounts")
        return delete_igaccounts(ok=ok, message=message)
