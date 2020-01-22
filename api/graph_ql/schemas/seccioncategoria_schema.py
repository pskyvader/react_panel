from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import seccioncategoria_model
from ..resolver import resolve
from ..mutator import mutation_create, mutation_update, mutation_delete


attribute = dict(
    idpadre=graphene.String(),
    tipo=graphene.Int(),
    titulo=graphene.String(),
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
    foto=graphene.JSONString()
    )
black_list_attribute = dict(
    
    )


class seccioncategoria_schema(SQLAlchemyObjectType):
    class Meta:
        model = seccioncategoria_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idseccioncategoria"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )
    
    


def resolve_seccioncategoria(args, info, idseccioncategoria, **kwargs):
    query = resolve(
        args, info, seccioncategoria_schema, seccioncategoria_model, idseccioncategoria=idseccioncategoria, **kwargs
    )
    return query.first()


def resolve_all_seccioncategoria(args, info, **kwargs):
    query = resolve(args, info, seccioncategoria_schema, seccioncategoria_model, **kwargs)
    return query


all_seccioncategoria = SQLAlchemyConnectionField( seccioncategoria_schema, sort=graphene.String() , **attribute )
seccioncategoria = graphene.Field(seccioncategoria_schema, idseccioncategoria=graphene.Int() , **attribute)

# Create a generic class to mutualize description of seccioncategoria _attributes for both queries and mutations
class seccioncategoria_attribute:
    # name = graphene.String(description="Name of the seccioncategoria.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(seccioncategoria_attribute, name, value)


class create_seccioncategoria_input(graphene.InputObjectType, seccioncategoria_attribute):
    """Arguments to create a seccioncategoria."""

    pass


class create_seccioncategoria(graphene.Mutation):
    """Mutation to create a seccioncategoria."""

    seccioncategoria = graphene.Field(
        seccioncategoria_schema, description="seccioncategoria created by this mutation."
    )

    class Arguments:
        input = create_seccioncategoria_input(required=True)

    def mutate(self, info, input):
        seccioncategoria = mutation_create(seccioncategoria_model, input, "idseccioncategoria",info)
        return create_seccioncategoria(seccioncategoria=seccioncategoria)


class update_seccioncategoria_input(graphene.InputObjectType, seccioncategoria_attribute):
    """Arguments to update a seccioncategoria."""

    idseccioncategoria = graphene.ID(required=True, description="Global Id of the seccioncategoria.")


class update_seccioncategoria(graphene.Mutation):
    """Update a seccioncategoria."""

    seccioncategoria = graphene.Field(
        seccioncategoria_schema, description="seccioncategoria updated by this mutation."
    )

    class Arguments:
        input = update_seccioncategoria_input(required=True)

    def mutate(self, info, input):
        seccioncategoria = mutation_update(seccioncategoria_model, input, "idseccioncategoria",info)
        return update_seccioncategoria(seccioncategoria=seccioncategoria)


class delete_seccioncategoria_input(graphene.InputObjectType, seccioncategoria_attribute):
    """Arguments to delete a seccioncategoria."""

    idseccioncategoria = graphene.ID(required=True, description="Global Id of the seccioncategoria.")


class delete_seccioncategoria(graphene.Mutation):
    """delete a seccioncategoria."""

    ok = graphene.Boolean(description="seccioncategoria deleted correctly.")
    message = graphene.String(description="seccioncategoria deleted message.")

    class Arguments:
        input = delete_seccioncategoria_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(seccioncategoria_model, input, "idseccioncategoria")
        return delete_seccioncategoria(ok=ok, message=message)
