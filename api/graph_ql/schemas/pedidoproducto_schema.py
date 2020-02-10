from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import pedidoproducto_model
from ..resolver import resolve
from ..mutator import mutation_create, mutation_update, mutation_delete
from .image_schema import all_image,resolve_all_image

attribute = dict(
    idpedido=graphene.Int(),
    idpedidodireccion=graphene.Int(),
    idproducto=graphene.Int(),
    titulo=graphene.String(),
    mensaje=graphene.String(),
    idproductoatributo=graphene.Int(),
    titulo_atributo=graphene.String(),
    precio=graphene.Int(),
    cantidad=graphene.Int(),
    total=graphene.Int()
    )
read_only_attribute = dict(
    
    )
black_list_attribute = dict(
    
    )


class pedidoproducto_schema(SQLAlchemyObjectType):
    class Meta:
        model = pedidoproducto_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idpedidoproducto"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )
    
    
    foto=all_image
    def resolve_foto(parent,info, **kwargs):
        return resolve_all_image(parent,info,table_name='pedidoproducto',idparent=parent.idpedidoproducto,field_name='foto',**kwargs)



def resolve_pedidoproducto(args, info, idpedidoproducto, **kwargs):
    query = resolve(
        args, info, pedidoproducto_schema, pedidoproducto_model, idpedidoproducto=idpedidoproducto, **kwargs
    )
    return query.first()


def resolve_all_pedidoproducto(args, info, **kwargs):
    query = resolve(args, info, pedidoproducto_schema, pedidoproducto_model, **kwargs)
    return query


all_pedidoproducto = SQLAlchemyConnectionField( pedidoproducto_schema, sort=graphene.String(), **attribute )
pedidoproducto = graphene.Field(pedidoproducto_schema, idpedidoproducto=graphene.Int(), **attribute)

# Create a generic class to mutualize description of pedidoproducto _attributes for both queries and mutations
class pedidoproducto_attribute:
    # name = graphene.String(description="Name of the pedidoproducto.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(pedidoproducto_attribute, name, value)


class create_pedidoproducto_input(graphene.InputObjectType, pedidoproducto_attribute):
    """Arguments to create a pedidoproducto."""

    pass


class create_pedidoproducto(graphene.Mutation):
    """Mutation to create a pedidoproducto."""

    pedidoproducto = graphene.Field(
        pedidoproducto_schema, description="pedidoproducto created by this mutation."
    )

    class Arguments:
        input = create_pedidoproducto_input(required=True)

    def mutate(self, info, input):
        pedidoproducto = mutation_create(pedidoproducto_model, input, "idpedidoproducto",info)
        return create_pedidoproducto(pedidoproducto=pedidoproducto)


class update_pedidoproducto_input(graphene.InputObjectType, pedidoproducto_attribute):
    """Arguments to update a pedidoproducto."""

    idpedidoproducto = graphene.ID(required=True, description="Global Id of the pedidoproducto.")


class update_pedidoproducto(graphene.Mutation):
    """Update a pedidoproducto."""

    pedidoproducto = graphene.Field(
        pedidoproducto_schema, description="pedidoproducto updated by this mutation."
    )

    class Arguments:
        input = update_pedidoproducto_input(required=True)

    def mutate(self, info, input):
        pedidoproducto = mutation_update(pedidoproducto_model, input, "idpedidoproducto",info)
        return update_pedidoproducto(pedidoproducto=pedidoproducto)


class delete_pedidoproducto_input(graphene.InputObjectType, pedidoproducto_attribute):
    """Arguments to delete a pedidoproducto."""

    idpedidoproducto = graphene.ID(required=True, description="Global Id of the pedidoproducto.")


class delete_pedidoproducto(graphene.Mutation):
    """delete a pedidoproducto."""

    ok = graphene.Boolean(description="pedidoproducto deleted correctly.")
    message = graphene.String(description="pedidoproducto deleted message.")

    class Arguments:
        input = delete_pedidoproducto_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(pedidoproducto_model, input, "idpedidoproducto")
        return delete_pedidoproducto(ok=ok, message=message)
