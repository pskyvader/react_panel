from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import galeria_model
from ..resolver import resolve,Url
from ..mutator import mutation_create, mutation_update, mutation_delete


attribute = dict(
    tipo=graphene.Int(),
    titulo=graphene.String(),
    url=graphene.String(),
    subtitulo=graphene.String(),
    resumen=graphene.String(),
    keywords=graphene.String(),
    metadescripcion=graphene.String(),
    orden=graphene.Int(),
    estado=graphene.Boolean()
    )
read_only_attribute = dict(
    foto=graphene.JSONString()
    )
black_list_attribute = dict(
    
    )


class galeria_schema(SQLAlchemyObjectType):
    class Meta:
        model = galeria_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idgaleria"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )
    
    


def resolve_galeria(args, info, idgaleria, **kwargs):
    query = resolve(
        args, info, galeria_schema, galeria_model, idgaleria=idgaleria, **kwargs
    )
    return query.first()


def resolve_all_galeria(args, info, **kwargs):
    query = resolve(args, info, galeria_schema, galeria_model, **kwargs)
    return query


all_galeria = SQLAlchemyConnectionField( galeria_schema, sort=graphene.String() , **attribute )
galeria = graphene.Field(galeria_schema, idgaleria=graphene.Int() , **attribute)

# Create a generic class to mutualize description of galeria _attributes for both queries and mutations
class galeria_attribute:
    # name = graphene.String(description="Name of the galeria.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(galeria_attribute, name, value)


class create_galeria_input(graphene.InputObjectType, galeria_attribute):
    """Arguments to create a galeria."""

    pass


class create_galeria(graphene.Mutation):
    """Mutation to create a galeria."""

    galeria = graphene.Field(
        galeria_schema, description="galeria created by this mutation."
    )

    class Arguments:
        input = create_galeria_input(required=True)

    def mutate(self, info, input):
        galeria = mutation_create(galeria_model, input, "idgaleria",info)
        return create_galeria(galeria=galeria)


class update_galeria_input(graphene.InputObjectType, galeria_attribute):
    """Arguments to update a galeria."""

    idgaleria = graphene.ID(required=True, description="Global Id of the galeria.")


class update_galeria(graphene.Mutation):
    """Update a galeria."""

    galeria = graphene.Field(
        galeria_schema, description="galeria updated by this mutation."
    )

    class Arguments:
        input = update_galeria_input(required=True)

    def mutate(self, info, input):
        galeria = mutation_update(galeria_model, input, "idgaleria",info)
        return update_galeria(galeria=galeria)


class delete_galeria_input(graphene.InputObjectType, galeria_attribute):
    """Arguments to delete a galeria."""

    idgaleria = graphene.ID(required=True, description="Global Id of the galeria.")


class delete_galeria(graphene.Mutation):
    """delete a galeria."""

    ok = graphene.Boolean(description="galeria deleted correctly.")
    message = graphene.String(description="galeria deleted message.")

    class Arguments:
        input = delete_galeria_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(galeria_model, input, "idgaleria")
        return delete_galeria(ok=ok, message=message)
