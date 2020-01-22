from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import modulo_model
from ..resolver import resolve
from ..mutator import mutation_create, mutation_update, mutation_delete


attribute = dict(
    idmoduloconfiguracion=graphene.Int(),
    tipo=graphene.Int(),
    titulo=graphene.String(),
    menu=graphene.String(),
    mostrar=graphene.String(),
    detalle=graphene.String(),
    recortes=graphene.String(),
    orden=graphene.Int(),
    estado=graphene.String(),
    aside=graphene.Boolean(),
    hijos=graphene.Boolean()
    )
read_only_attribute = dict(
    
    )
black_list_attribute = dict(
    
    )


class modulo_schema(SQLAlchemyObjectType):
    class Meta:
        model = modulo_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idmodulo"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )


def resolve_modulo(args, info, idmodulo, **kwargs):
    query = resolve(
        args, info, modulo_schema, modulo_model, idmodulo=idmodulo, **kwargs
    )
    return query.first()


def resolve_all_modulo(args, info, **kwargs):
    query = resolve(args, info, modulo_schema, modulo_model, **kwargs)
    return query


all_modulo = SQLAlchemyConnectionField(
    modulo_schema, sort=graphene.String(), **attribute
)
modulo = graphene.Field(modulo_schema, idmodulo=graphene.Int(), **attribute)

# Create a generic class to mutualize description of modulo _attributes for both queries and mutations
class modulo_attribute:
    # name = graphene.String(description="Name of the modulo.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(modulo_attribute, name, value)


class create_modulo_input(graphene.InputObjectType, modulo_attribute):
    """Arguments to create a modulo."""

    pass


class create_modulo(graphene.Mutation):
    """Mutation to create a modulo."""

    modulo = graphene.Field(
        modulo_schema, description="modulo created by this mutation."
    )

    class Arguments:
        input = create_modulo_input(required=True)

    def mutate(self, info, input):
        modulo = mutation_create(modulo_model, input, "idmodulo")
        return create_modulo(modulo=modulo)


class update_modulo_input(graphene.InputObjectType, modulo_attribute):
    """Arguments to update a modulo."""

    idmodulo = graphene.ID(required=True, description="Global Id of the modulo.")


class update_modulo(graphene.Mutation):
    """Update a modulo."""

    modulo = graphene.Field(
        modulo_schema, description="modulo updated by this mutation."
    )

    class Arguments:
        input = update_modulo_input(required=True)

    def mutate(self, info, input):
        modulo = mutation_update(modulo_model, input, "idmodulo")
        return update_modulo(modulo=modulo)


class delete_modulo_input(graphene.InputObjectType, modulo_attribute):
    """Arguments to delete a modulo."""

    idmodulo = graphene.ID(required=True, description="Global Id of the modulo.")


class delete_modulo(graphene.Mutation):
    """delete a modulo."""

    ok = graphene.Boolean(description="modulo deleted correctly.")
    message = graphene.String(description="modulo deleted message.")

    class Arguments:
        input = delete_modulo_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(modulo_model, input, "idmodulo")
        return delete_modulo(ok=ok, message=message)
