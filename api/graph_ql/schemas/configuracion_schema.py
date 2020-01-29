from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import configuracion_model
from ..resolver import resolve,Url
from ..mutator import mutation_create, mutation_update, mutation_delete


attribute = dict(
    variable=graphene.String(),
    valor=graphene.String()
    )
read_only_attribute = dict(
    
    )
black_list_attribute = dict(
    
    )


class configuracion_schema(SQLAlchemyObjectType):
    class Meta:
        model = configuracion_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idconfiguracion"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )
    
    


def resolve_configuracion(args, info, idconfiguracion, **kwargs):
    query = resolve(
        args, info, configuracion_schema, configuracion_model, idconfiguracion=idconfiguracion, **kwargs
    )
    return query.first()


def resolve_all_configuracion(args, info, **kwargs):
    query = resolve(args, info, configuracion_schema, configuracion_model, **kwargs)
    return query


all_configuracion = SQLAlchemyConnectionField( configuracion_schema, sort=graphene.String() , **attribute )
configuracion = graphene.Field(configuracion_schema, idconfiguracion=graphene.Int() , **attribute)

# Create a generic class to mutualize description of configuracion _attributes for both queries and mutations
class configuracion_attribute:
    # name = graphene.String(description="Name of the configuracion.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(configuracion_attribute, name, value)


class create_configuracion_input(graphene.InputObjectType, configuracion_attribute):
    """Arguments to create a configuracion."""

    pass


class create_configuracion(graphene.Mutation):
    """Mutation to create a configuracion."""

    configuracion = graphene.Field(
        configuracion_schema, description="configuracion created by this mutation."
    )

    class Arguments:
        input = create_configuracion_input(required=True)

    def mutate(self, info, input):
        configuracion = mutation_create(configuracion_model, input, "idconfiguracion",info)
        return create_configuracion(configuracion=configuracion)


class update_configuracion_input(graphene.InputObjectType, configuracion_attribute):
    """Arguments to update a configuracion."""

    idconfiguracion = graphene.ID(required=True, description="Global Id of the configuracion.")


class update_configuracion(graphene.Mutation):
    """Update a configuracion."""

    configuracion = graphene.Field(
        configuracion_schema, description="configuracion updated by this mutation."
    )

    class Arguments:
        input = update_configuracion_input(required=True)

    def mutate(self, info, input):
        configuracion = mutation_update(configuracion_model, input, "idconfiguracion",info)
        return update_configuracion(configuracion=configuracion)


class delete_configuracion_input(graphene.InputObjectType, configuracion_attribute):
    """Arguments to delete a configuracion."""

    idconfiguracion = graphene.ID(required=True, description="Global Id of the configuracion.")


class delete_configuracion(graphene.Mutation):
    """delete a configuracion."""

    ok = graphene.Boolean(description="configuracion deleted correctly.")
    message = graphene.String(description="configuracion deleted message.")

    class Arguments:
        input = delete_configuracion_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(configuracion_model, input, "idconfiguracion")
        return delete_configuracion(ok=ok, message=message)
