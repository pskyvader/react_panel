from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import TABLENAME_model
from ..resolver import resolve
from ..mutator import mutation_create, mutation_update, mutation_delete


attribute = dict(
    EXTRA_FIELDS
    )
read_only_attribute = dict(
    READ_ONLY_FIELDS
    )
black_list_attribute = dict(
    BLACK_LIST_FIELDS
    )


class TABLENAME_schema(SQLAlchemyObjectType):
    class Meta:
        model = TABLENAME_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idTABLENAME"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )


def resolve_TABLENAME(args, info, idTABLENAME, **kwargs):
    query = resolve(
        args, info, TABLENAME_schema, TABLENAME_model, idTABLENAME=idTABLENAME, **kwargs
    )
    return query.first()


def resolve_all_TABLENAME(args, info, **kwargs):
    query = resolve(args, info, TABLENAME_schema, TABLENAME_model, **kwargs)
    return query


all_TABLENAME = SQLAlchemyConnectionField(
    TABLENAME_schema, sort=graphene.String(), **attribute
)
TABLENAME = graphene.Field(TABLENAME_schema, idTABLENAME=graphene.Int(), **attribute)

# Create a generic class to mutualize description of TABLENAME _attributes for both queries and mutations
class TABLENAME_attribute:
    # name = graphene.String(description="Name of the TABLENAME.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(TABLENAME_attribute, name, value)


class create_TABLENAME_input(graphene.InputObjectType, TABLENAME_attribute):
    """Arguments to create a TABLENAME."""

    pass


class create_TABLENAME(graphene.Mutation):
    """Mutation to create a TABLENAME."""

    TABLENAME = graphene.Field(
        TABLENAME_schema, description="TABLENAME created by this mutation."
    )

    class Arguments:
        input = create_TABLENAME_input(required=True)

    def mutate(self, info, input):
        TABLENAME = mutation_create(TABLENAME_model, input, "idTABLENAME",info)
        return create_TABLENAME(TABLENAME=TABLENAME)


class update_TABLENAME_input(graphene.InputObjectType, TABLENAME_attribute):
    """Arguments to update a TABLENAME."""

    idTABLENAME = graphene.ID(required=True, description="Global Id of the TABLENAME.")


class update_TABLENAME(graphene.Mutation):
    """Update a TABLENAME."""

    TABLENAME = graphene.Field(
        TABLENAME_schema, description="TABLENAME updated by this mutation."
    )

    class Arguments:
        input = update_TABLENAME_input(required=True)

    def mutate(self, info, input):
        TABLENAME = mutation_update(TABLENAME_model, input, "idTABLENAME",info)
        return update_TABLENAME(TABLENAME=TABLENAME)


class delete_TABLENAME_input(graphene.InputObjectType, TABLENAME_attribute):
    """Arguments to delete a TABLENAME."""

    idTABLENAME = graphene.ID(required=True, description="Global Id of the TABLENAME.")


class delete_TABLENAME(graphene.Mutation):
    """delete a TABLENAME."""

    ok = graphene.Boolean(description="TABLENAME deleted correctly.")
    message = graphene.String(description="TABLENAME deleted message.")

    class Arguments:
        input = delete_TABLENAME_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(TABLENAME_model, input, "idTABLENAME")
        return delete_TABLENAME(ok=ok, message=message)
