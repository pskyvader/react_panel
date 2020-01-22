from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import igtotal_model
from ..resolver import resolve
from ..mutator import mutation_create, mutation_update, mutation_delete


attribute = dict(
    tag=graphene.String(),
    fecha=graphene.types.datetime.DateTime(),
    cantidad=graphene.Int()
    )
read_only_attribute = dict(
    
    )
black_list_attribute = dict(
    
    )


class igtotal_schema(SQLAlchemyObjectType):
    class Meta:
        model = igtotal_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idigtotal"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )


def resolve_igtotal(args, info, idigtotal, **kwargs):
    query = resolve(
        args, info, igtotal_schema, igtotal_model, idigtotal=idigtotal, **kwargs
    )
    return query.first()


def resolve_all_igtotal(args, info, **kwargs):
    query = resolve(args, info, igtotal_schema, igtotal_model, **kwargs)
    return query


all_igtotal = SQLAlchemyConnectionField(
    igtotal_schema, sort=graphene.String(), **attribute
)
igtotal = graphene.Field(igtotal_schema, idigtotal=graphene.Int(), **attribute)

# Create a generic class to mutualize description of igtotal _attributes for both queries and mutations
class igtotal_attribute:
    # name = graphene.String(description="Name of the igtotal.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(igtotal_attribute, name, value)


class create_igtotal_input(graphene.InputObjectType, igtotal_attribute):
    """Arguments to create a igtotal."""

    pass


class create_igtotal(graphene.Mutation):
    """Mutation to create a igtotal."""

    igtotal = graphene.Field(
        igtotal_schema, description="igtotal created by this mutation."
    )

    class Arguments:
        input = create_igtotal_input(required=True)

    def mutate(self, info, input):
        igtotal = mutation_create(igtotal_model, input, "idigtotal")
        return create_igtotal(igtotal=igtotal)


class update_igtotal_input(graphene.InputObjectType, igtotal_attribute):
    """Arguments to update a igtotal."""

    idigtotal = graphene.ID(required=True, description="Global Id of the igtotal.")


class update_igtotal(graphene.Mutation):
    """Update a igtotal."""

    igtotal = graphene.Field(
        igtotal_schema, description="igtotal updated by this mutation."
    )

    class Arguments:
        input = update_igtotal_input(required=True)

    def mutate(self, info, input):
        igtotal = mutation_update(igtotal_model, input, "idigtotal")
        return update_igtotal(igtotal=igtotal)


class delete_igtotal_input(graphene.InputObjectType, igtotal_attribute):
    """Arguments to delete a igtotal."""

    idigtotal = graphene.ID(required=True, description="Global Id of the igtotal.")


class delete_igtotal(graphene.Mutation):
    """delete a igtotal."""

    ok = graphene.Boolean(description="igtotal deleted correctly.")
    message = graphene.String(description="igtotal deleted message.")

    class Arguments:
        input = delete_igtotal_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(igtotal_model, input, "idigtotal")
        return delete_igtotal(ok=ok, message=message)
