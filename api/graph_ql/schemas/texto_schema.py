from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import texto_model
from ..resolver import resolve
from ..mutator import mutation_create, mutation_update, mutation_delete


attribute = dict(
    tipo=graphene.String(),
    titulo=graphene.String(),
    url=graphene.String(),
    descripcion=graphene.String(),
    texto=graphene.String(),
    mapa=graphene.String(),
    orden=graphene.Int(),
    estado=graphene.Boolean()
    )
read_only_attribute = dict(
    
    )
black_list_attribute = dict(
    
    )


class texto_schema(SQLAlchemyObjectType):
    class Meta:
        model = texto_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idtexto"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )


def resolve_texto(args, info, idtexto, **kwargs):
    query = resolve(
        args, info, texto_schema, texto_model, idtexto=idtexto, **kwargs
    )
    return query.first()


def resolve_all_texto(args, info, **kwargs):
    query = resolve(args, info, texto_schema, texto_model, **kwargs)
    return query


all_texto = SQLAlchemyConnectionField(
    texto_schema, sort=graphene.String(), **attribute
)
texto = graphene.Field(texto_schema, idtexto=graphene.Int(), **attribute)

# Create a generic class to mutualize description of texto _attributes for both queries and mutations
class texto_attribute:
    # name = graphene.String(description="Name of the texto.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(texto_attribute, name, value)


class create_texto_input(graphene.InputObjectType, texto_attribute):
    """Arguments to create a texto."""

    pass


class create_texto(graphene.Mutation):
    """Mutation to create a texto."""

    texto = graphene.Field(
        texto_schema, description="texto created by this mutation."
    )

    class Arguments:
        input = create_texto_input(required=True)

    def mutate(self, info, input):
        texto = mutation_create(texto_model, input, "idtexto",info)
        return create_texto(texto=texto)


class update_texto_input(graphene.InputObjectType, texto_attribute):
    """Arguments to update a texto."""

    idtexto = graphene.ID(required=True, description="Global Id of the texto.")


class update_texto(graphene.Mutation):
    """Update a texto."""

    texto = graphene.Field(
        texto_schema, description="texto updated by this mutation."
    )

    class Arguments:
        input = update_texto_input(required=True)

    def mutate(self, info, input):
        texto = mutation_update(texto_model, input, "idtexto",info)
        return update_texto(texto=texto)


class delete_texto_input(graphene.InputObjectType, texto_attribute):
    """Arguments to delete a texto."""

    idtexto = graphene.ID(required=True, description="Global Id of the texto.")


class delete_texto(graphene.Mutation):
    """delete a texto."""

    ok = graphene.Boolean(description="texto deleted correctly.")
    message = graphene.String(description="texto deleted message.")

    class Arguments:
        input = delete_texto_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(texto_model, input, "idtexto")
        return delete_texto(ok=ok, message=message)
