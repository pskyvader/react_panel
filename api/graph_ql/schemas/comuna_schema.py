from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import comuna_model
from ..resolver import resolve
from ..mutator import mutation_create, mutation_update, mutation_delete


attribute = dict(
    idregion=graphene.Int(),
    titulo=graphene.String(),
    precio=graphene.Int(),
    orden=graphene.Int(),
    estado=graphene.Boolean()
    )
read_only_attribute = dict(
    
    )
black_list_attribute = dict(
    
    )


class comuna_schema(SQLAlchemyObjectType):
    class Meta:
        model = comuna_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idcomuna"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )
    
    


def resolve_comuna(args, info, idcomuna, **kwargs):
    query = resolve(
        args, info, comuna_schema, comuna_model, idcomuna=idcomuna, **kwargs
    )
    return query.first()


def resolve_all_comuna(args, info, **kwargs):
    query = resolve(args, info, comuna_schema, comuna_model, **kwargs)
    return query


all_comuna = SQLAlchemyConnectionField( comuna_schema, sort=graphene.String(), **attribute )
comuna = graphene.Field(comuna_schema, idcomuna=graphene.Int(), **attribute)

# Create a generic class to mutualize description of comuna _attributes for both queries and mutations
class comuna_attribute:
    # name = graphene.String(description="Name of the comuna.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(comuna_attribute, name, value)


class create_comuna_input(graphene.InputObjectType, comuna_attribute):
    """Arguments to create a comuna."""

    pass


class create_comuna(graphene.Mutation):
    """Mutation to create a comuna."""

    comuna = graphene.Field(
        comuna_schema, description="comuna created by this mutation."
    )

    class Arguments:
        input = create_comuna_input(required=True)

    def mutate(self, info, input):
        comuna = mutation_create(comuna_model, input, "idcomuna",info)
        return create_comuna(comuna=comuna)


class update_comuna_input(graphene.InputObjectType, comuna_attribute):
    """Arguments to update a comuna."""

    idcomuna = graphene.ID(required=True, description="Global Id of the comuna.")


class update_comuna(graphene.Mutation):
    """Update a comuna."""

    comuna = graphene.Field(
        comuna_schema, description="comuna updated by this mutation."
    )

    class Arguments:
        input = update_comuna_input(required=True)

    def mutate(self, info, input):
        comuna = mutation_update(comuna_model, input, "idcomuna",info)
        return update_comuna(comuna=comuna)


class delete_comuna_input(graphene.InputObjectType, comuna_attribute):
    """Arguments to delete a comuna."""

    idcomuna = graphene.ID(required=True, description="Global Id of the comuna.")


class delete_comuna(graphene.Mutation):
    """delete a comuna."""

    ok = graphene.Boolean(description="comuna deleted correctly.")
    message = graphene.String(description="comuna deleted message.")

    class Arguments:
        input = delete_comuna_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(comuna_model, input, "idcomuna")
        return delete_comuna(ok=ok, message=message)
