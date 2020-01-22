from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import pedidodireccion_model
from ..resolver import resolve
from ..mutator import mutation_create, mutation_update, mutation_delete


attribute = dict(
    idpedido=graphene.Int(),
    idusuariodireccion=graphene.Int(),
    idpedidoestado=graphene.Int(),
    precio=graphene.Int(),
    cookie_direccion=graphene.String(),
    nombre=graphene.String(),
    telefono=graphene.String(),
    direccion_completa=graphene.String(),
    referencias=graphene.String(),
    fecha_entrega=graphene.types.datetime.DateTime()
    )
read_only_attribute = dict(
    
    )
black_list_attribute = dict(
    
    )


class pedidodireccion_schema(SQLAlchemyObjectType):
    class Meta:
        model = pedidodireccion_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idpedidodireccion"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )
    
    


def resolve_pedidodireccion(args, info, idpedidodireccion, **kwargs):
    query = resolve(
        args, info, pedidodireccion_schema, pedidodireccion_model, idpedidodireccion=idpedidodireccion, **kwargs
    )
    return query.first()


def resolve_all_pedidodireccion(args, info, **kwargs):
    query = resolve(args, info, pedidodireccion_schema, pedidodireccion_model, **kwargs)
    return query


all_pedidodireccion = SQLAlchemyConnectionField( pedidodireccion_schema, sort=graphene.String() , **attribute )
pedidodireccion = graphene.Field(pedidodireccion_schema, idpedidodireccion=graphene.Int() , **attribute)

# Create a generic class to mutualize description of pedidodireccion _attributes for both queries and mutations
class pedidodireccion_attribute:
    # name = graphene.String(description="Name of the pedidodireccion.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(pedidodireccion_attribute, name, value)


class create_pedidodireccion_input(graphene.InputObjectType, pedidodireccion_attribute):
    """Arguments to create a pedidodireccion."""

    pass


class create_pedidodireccion(graphene.Mutation):
    """Mutation to create a pedidodireccion."""

    pedidodireccion = graphene.Field(
        pedidodireccion_schema, description="pedidodireccion created by this mutation."
    )

    class Arguments:
        input = create_pedidodireccion_input(required=True)

    def mutate(self, info, input):
        pedidodireccion = mutation_create(pedidodireccion_model, input, "idpedidodireccion",info)
        return create_pedidodireccion(pedidodireccion=pedidodireccion)


class update_pedidodireccion_input(graphene.InputObjectType, pedidodireccion_attribute):
    """Arguments to update a pedidodireccion."""

    idpedidodireccion = graphene.ID(required=True, description="Global Id of the pedidodireccion.")


class update_pedidodireccion(graphene.Mutation):
    """Update a pedidodireccion."""

    pedidodireccion = graphene.Field(
        pedidodireccion_schema, description="pedidodireccion updated by this mutation."
    )

    class Arguments:
        input = update_pedidodireccion_input(required=True)

    def mutate(self, info, input):
        pedidodireccion = mutation_update(pedidodireccion_model, input, "idpedidodireccion",info)
        return update_pedidodireccion(pedidodireccion=pedidodireccion)


class delete_pedidodireccion_input(graphene.InputObjectType, pedidodireccion_attribute):
    """Arguments to delete a pedidodireccion."""

    idpedidodireccion = graphene.ID(required=True, description="Global Id of the pedidodireccion.")


class delete_pedidodireccion(graphene.Mutation):
    """delete a pedidodireccion."""

    ok = graphene.Boolean(description="pedidodireccion deleted correctly.")
    message = graphene.String(description="pedidodireccion deleted message.")

    class Arguments:
        input = delete_pedidodireccion_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(pedidodireccion_model, input, "idpedidodireccion")
        return delete_pedidodireccion(ok=ok, message=message)
