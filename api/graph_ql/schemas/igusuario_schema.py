from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import igusuario_model
from ..resolver import resolve
from ..mutator import mutation_create, mutation_update, mutation_delete


attribute = dict(
    usuario=graphene.String(),
estado=graphene.Boolean()
    )
read_only_attribute = dict(
    
    )
black_list_attribute = dict(
    password=graphene.String()
    )


class igusuario_schema(SQLAlchemyObjectType):
    class Meta:
        model = igusuario_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idigusuario"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )
    
    


def resolve_igusuario(args, info, idigusuario, **kwargs):
    query = resolve(
        args, info, igusuario_schema, igusuario_model, idigusuario=idigusuario, **kwargs
    )
    return query.first()


def resolve_all_igusuario(args, info, **kwargs):
    query = resolve(args, info, igusuario_schema, igusuario_model, **kwargs)
    return query


all_igusuario = SQLAlchemyConnectionField( igusuario_schema, sort=graphene.String(), **attribute )
igusuario = graphene.Field(igusuario_schema, idigusuario=graphene.Int(), **attribute)

# Create a generic class to mutualize description of igusuario _attributes for both queries and mutations
class igusuario_attribute:
    # name = graphene.String(description="Name of the igusuario.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(igusuario_attribute, name, value)


class create_igusuario_input(graphene.InputObjectType, igusuario_attribute):
    """Arguments to create a igusuario."""

    pass


class create_igusuario(graphene.Mutation):
    """Mutation to create a igusuario."""

    igusuario = graphene.Field(
        igusuario_schema, description="igusuario created by this mutation."
    )

    class Arguments:
        input = create_igusuario_input(required=True)

    def mutate(self, info, input):
        igusuario = mutation_create(igusuario_model, input, "idigusuario",info)
        return create_igusuario(igusuario=igusuario)


class update_igusuario_input(graphene.InputObjectType, igusuario_attribute):
    """Arguments to update a igusuario."""

    idigusuario = graphene.ID(required=True, description="Global Id of the igusuario.")


class update_igusuario(graphene.Mutation):
    """Update a igusuario."""

    igusuario = graphene.Field(
        igusuario_schema, description="igusuario updated by this mutation."
    )

    class Arguments:
        input = update_igusuario_input(required=True)

    def mutate(self, info, input):
        igusuario = mutation_update(igusuario_model, input, "idigusuario",info)
        return update_igusuario(igusuario=igusuario)


class delete_igusuario_input(graphene.InputObjectType, igusuario_attribute):
    """Arguments to delete a igusuario."""

    idigusuario = graphene.ID(required=True, description="Global Id of the igusuario.")


class delete_igusuario(graphene.Mutation):
    """delete a igusuario."""

    ok = graphene.Boolean(description="igusuario deleted correctly.")
    message = graphene.String(description="igusuario deleted message.")

    class Arguments:
        input = delete_igusuario_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(igusuario_model, input, "idigusuario")
        return delete_igusuario(ok=ok, message=message)
