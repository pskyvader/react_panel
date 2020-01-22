from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import seccion_model
from ..resolver import resolve
from ..mutator import mutation_create, mutation_update, mutation_delete


attribute = dict(
    idseccioncategoria=graphene.String(),
    tipo=graphene.Int(),
    titulo=graphene.String(),
    subtitulo=graphene.String(),
    url=graphene.String(),
    resumen=graphene.String(),
    descripcion=graphene.String(),
    keywords=graphene.String(),
    metadescripcion=graphene.String(),
    orden=graphene.Int(),
    estado=graphene.Boolean(),
    destacado=graphene.Boolean()
    )
read_only_attribute = dict(
    foto=graphene.JSONString(),
    archivo=graphene.JSONString()
    )
black_list_attribute = dict(
    
    )


class seccion_schema(SQLAlchemyObjectType):
    class Meta:
        model = seccion_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idseccion"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )


def resolve_seccion(args, info, idseccion, **kwargs):
    query = resolve(
        args, info, seccion_schema, seccion_model, idseccion=idseccion, **kwargs
    )
    return query.first()


def resolve_all_seccion(args, info, **kwargs):
    query = resolve(args, info, seccion_schema, seccion_model, **kwargs)
    return query


all_seccion = SQLAlchemyConnectionField(
    seccion_schema, sort=graphene.String(), **attribute
)
seccion = graphene.Field(seccion_schema, idseccion=graphene.Int(), **attribute)

# Create a generic class to mutualize description of seccion _attributes for both queries and mutations
class seccion_attribute:
    # name = graphene.String(description="Name of the seccion.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(seccion_attribute, name, value)


class create_seccion_input(graphene.InputObjectType, seccion_attribute):
    """Arguments to create a seccion."""

    pass


class create_seccion(graphene.Mutation):
    """Mutation to create a seccion."""

    seccion = graphene.Field(
        seccion_schema, description="seccion created by this mutation."
    )

    class Arguments:
        input = create_seccion_input(required=True)

    def mutate(self, info, input):
        seccion = mutation_create(seccion_model, input, "idseccion",info)
        return create_seccion(seccion=seccion)


class update_seccion_input(graphene.InputObjectType, seccion_attribute):
    """Arguments to update a seccion."""

    idseccion = graphene.ID(required=True, description="Global Id of the seccion.")


class update_seccion(graphene.Mutation):
    """Update a seccion."""

    seccion = graphene.Field(
        seccion_schema, description="seccion updated by this mutation."
    )

    class Arguments:
        input = update_seccion_input(required=True)

    def mutate(self, info, input):
        seccion = mutation_update(seccion_model, input, "idseccion",info)
        return update_seccion(seccion=seccion)


class delete_seccion_input(graphene.InputObjectType, seccion_attribute):
    """Arguments to delete a seccion."""

    idseccion = graphene.ID(required=True, description="Global Id of the seccion.")


class delete_seccion(graphene.Mutation):
    """delete a seccion."""

    ok = graphene.Boolean(description="seccion deleted correctly.")
    message = graphene.String(description="seccion deleted message.")

    class Arguments:
        input = delete_seccion_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(seccion_model, input, "idseccion")
        return delete_seccion(ok=ok, message=message)
