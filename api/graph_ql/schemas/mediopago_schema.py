from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import mediopago_model
from ..resolver import resolve
from ..mutator import mutation_create, mutation_update, mutation_delete


attribute = dict(
    titulo=graphene.String(),
    resumen=graphene.String(),
    descripcion=graphene.String(),
    orden=graphene.Int(),
    estado=graphene.Boolean()
    )
read_only_attribute = dict(
    
    )
black_list_attribute = dict(
    
    )


class mediopago_schema(SQLAlchemyObjectType):
    class Meta:
        model = mediopago_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idmediopago"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )
    
    


def resolve_mediopago(args, info, idmediopago, **kwargs):
    query = resolve(
        args, info, mediopago_schema, mediopago_model, idmediopago=idmediopago, **kwargs
    )
    return query.first()


def resolve_all_mediopago(args, info, **kwargs):
    query = resolve(args, info, mediopago_schema, mediopago_model, **kwargs)
    return query


all_mediopago = SQLAlchemyConnectionField( mediopago_schema, sort=graphene.String(), **attribute )
mediopago = graphene.Field(mediopago_schema, idmediopago=graphene.Int(), **attribute)

# Create a generic class to mutualize description of mediopago _attributes for both queries and mutations
class mediopago_attribute:
    # name = graphene.String(description="Name of the mediopago.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(mediopago_attribute, name, value)


class create_mediopago_input(graphene.InputObjectType, mediopago_attribute):
    """Arguments to create a mediopago."""

    pass


class create_mediopago(graphene.Mutation):
    """Mutation to create a mediopago."""

    mediopago = graphene.Field(
        mediopago_schema, description="mediopago created by this mutation."
    )

    class Arguments:
        input = create_mediopago_input(required=True)

    def mutate(self, info, input):
        mediopago = mutation_create(mediopago_model, input, "idmediopago",info)
        return create_mediopago(mediopago=mediopago)


class update_mediopago_input(graphene.InputObjectType, mediopago_attribute):
    """Arguments to update a mediopago."""

    idmediopago = graphene.ID(required=True, description="Global Id of the mediopago.")


class update_mediopago(graphene.Mutation):
    """Update a mediopago."""

    mediopago = graphene.Field(
        mediopago_schema, description="mediopago updated by this mutation."
    )

    class Arguments:
        input = update_mediopago_input(required=True)

    def mutate(self, info, input):
        mediopago = mutation_update(mediopago_model, input, "idmediopago",info)
        return update_mediopago(mediopago=mediopago)


class delete_mediopago_input(graphene.InputObjectType, mediopago_attribute):
    """Arguments to delete a mediopago."""

    idmediopago = graphene.ID(required=True, description="Global Id of the mediopago.")


class delete_mediopago(graphene.Mutation):
    """delete a mediopago."""

    ok = graphene.Boolean(description="mediopago deleted correctly.")
    message = graphene.String(description="mediopago deleted message.")

    class Arguments:
        input = delete_mediopago_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(mediopago_model, input, "idmediopago")
        return delete_mediopago(ok=ok, message=message)
