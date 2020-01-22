from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import direccion_model
from ..resolver import resolve
from ..mutator import mutation_create, mutation_update, mutation_delete


attribute = dict(
    idusuario=graphene.Int(),
    tipo=graphene.Int(),
    titulo=graphene.String(),
    nombre=graphene.String(),
    direccion=graphene.String(),
    idcomuna=graphene.Int(),
    telefono=graphene.String(),
    villa=graphene.String(),
    edificio=graphene.String(),
    departamento=graphene.String(),
    condominio=graphene.String(),
    casa=graphene.String(),
    empresa=graphene.String(),
    referencias=graphene.String()
    )
read_only_attribute = dict(
    
    )
black_list_attribute = dict(
    
    )


class direccion_schema(SQLAlchemyObjectType):
    class Meta:
        model = direccion_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["iddireccion"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )
    
    


def resolve_direccion(args, info, iddireccion, **kwargs):
    query = resolve(
        args, info, direccion_schema, direccion_model, iddireccion=iddireccion, **kwargs
    )
    return query.first()


def resolve_all_direccion(args, info, **kwargs):
    query = resolve(args, info, direccion_schema, direccion_model, **kwargs)
    return query


all_direccion = SQLAlchemyConnectionField( direccion_schema, sort=graphene.String() , **attribute )
direccion = graphene.Field(direccion_schema, iddireccion=graphene.Int() , **attribute)

# Create a generic class to mutualize description of direccion _attributes for both queries and mutations
class direccion_attribute:
    # name = graphene.String(description="Name of the direccion.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(direccion_attribute, name, value)


class create_direccion_input(graphene.InputObjectType, direccion_attribute):
    """Arguments to create a direccion."""

    pass


class create_direccion(graphene.Mutation):
    """Mutation to create a direccion."""

    direccion = graphene.Field(
        direccion_schema, description="direccion created by this mutation."
    )

    class Arguments:
        input = create_direccion_input(required=True)

    def mutate(self, info, input):
        direccion = mutation_create(direccion_model, input, "iddireccion",info)
        return create_direccion(direccion=direccion)


class update_direccion_input(graphene.InputObjectType, direccion_attribute):
    """Arguments to update a direccion."""

    iddireccion = graphene.ID(required=True, description="Global Id of the direccion.")


class update_direccion(graphene.Mutation):
    """Update a direccion."""

    direccion = graphene.Field(
        direccion_schema, description="direccion updated by this mutation."
    )

    class Arguments:
        input = update_direccion_input(required=True)

    def mutate(self, info, input):
        direccion = mutation_update(direccion_model, input, "iddireccion",info)
        return update_direccion(direccion=direccion)


class delete_direccion_input(graphene.InputObjectType, direccion_attribute):
    """Arguments to delete a direccion."""

    iddireccion = graphene.ID(required=True, description="Global Id of the direccion.")


class delete_direccion(graphene.Mutation):
    """delete a direccion."""

    ok = graphene.Boolean(description="direccion deleted correctly.")
    message = graphene.String(description="direccion deleted message.")

    class Arguments:
        input = delete_direccion_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(direccion_model, input, "iddireccion")
        return delete_direccion(ok=ok, message=message)
