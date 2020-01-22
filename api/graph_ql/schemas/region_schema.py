from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import region_model
from ..resolver import resolve
from ..mutator import mutation_create, mutation_update, mutation_delete


attribute = dict(
    titulo=graphene.String(),
    precio=graphene.Int(),
    orden=graphene.Int(),
    estado=graphene.Boolean()
    )
read_only_attribute = dict(
    
    )
black_list_attribute = dict(
    
    )


class region_schema(SQLAlchemyObjectType):
    class Meta:
        model = region_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idregion"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )


def resolve_region(args, info, idregion, **kwargs):
    query = resolve(
        args, info, region_schema, region_model, idregion=idregion, **kwargs
    )
    return query.first()


def resolve_all_region(args, info, **kwargs):
    query = resolve(args, info, region_schema, region_model, **kwargs)
    return query


all_region = SQLAlchemyConnectionField(
    region_schema, sort=graphene.String(), **attribute
)
region = graphene.Field(region_schema, idregion=graphene.Int(), **attribute)

# Create a generic class to mutualize description of region _attributes for both queries and mutations
class region_attribute:
    # name = graphene.String(description="Name of the region.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(region_attribute, name, value)


class create_region_input(graphene.InputObjectType, region_attribute):
    """Arguments to create a region."""

    pass


class create_region(graphene.Mutation):
    """Mutation to create a region."""

    region = graphene.Field(
        region_schema, description="region created by this mutation."
    )

    class Arguments:
        input = create_region_input(required=True)

    def mutate(self, info, input):
        region = mutation_create(region_model, input, "idregion")
        return create_region(region=region)


class update_region_input(graphene.InputObjectType, region_attribute):
    """Arguments to update a region."""

    idregion = graphene.ID(required=True, description="Global Id of the region.")


class update_region(graphene.Mutation):
    """Update a region."""

    region = graphene.Field(
        region_schema, description="region updated by this mutation."
    )

    class Arguments:
        input = update_region_input(required=True)

    def mutate(self, info, input):
        region = mutation_update(region_model, input, "idregion")
        return update_region(region=region)


class delete_region_input(graphene.InputObjectType, region_attribute):
    """Arguments to delete a region."""

    idregion = graphene.ID(required=True, description="Global Id of the region.")


class delete_region(graphene.Mutation):
    """delete a region."""

    ok = graphene.Boolean(description="region deleted correctly.")
    message = graphene.String(description="region deleted message.")

    class Arguments:
        input = delete_region_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(region_model, input, "idregion")
        return delete_region(ok=ok, message=message)
