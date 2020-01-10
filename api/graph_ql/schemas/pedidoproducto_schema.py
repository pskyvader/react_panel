
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import pedidoproducto_model
from ..resolver import resolve
from ..mutator import mutation_create

# __REPLACE__

class pedidoproducto_schema(SQLAlchemyObjectType):
    class Meta:
        model = pedidoproducto_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idpedidoproducto','idpedido','idpedidodireccion','idproducto','titulo','foto','mensaje','idproductoatributo','titulo_atributo','precio','cantidad','total']


def resolve_pedidoproducto( args, info,idpedidoproducto, **kwargs ):
    query= resolve(args,info,pedidoproducto_schema,pedidoproducto_model,idpedidoproducto=idpedidoproducto,**kwargs)
    return query.first()

def resolve_all_pedidoproducto( args, info, **kwargs):
    query= resolve(args,info,pedidoproducto_schema,pedidoproducto_model,**kwargs)
    return query



all_pedidoproducto = SQLAlchemyConnectionField(pedidoproducto_schema,idpedido=graphene.Int(),idpedidodireccion=graphene.Int(),idproducto=graphene.Int(),titulo=graphene.String(),mensaje=graphene.String(),idproductoatributo=graphene.Int(),titulo_atributo=graphene.String(),precio=graphene.Int(),cantidad=graphene.Int(),total=graphene.Int())
pedidoproducto = graphene.Field(pedidoproducto_schema,idpedidoproducto=graphene.Int(),idpedido=graphene.Int(),idpedidodireccion=graphene.Int(),idproducto=graphene.Int(),titulo=graphene.String(),mensaje=graphene.String(),idproductoatributo=graphene.Int(),titulo_atributo=graphene.String(),precio=graphene.Int(),cantidad=graphene.Int(),total=graphene.Int())

# __REPLACE__



# Create a generic class to mutualize description of pedidoproducto _attributes for both queries and mutations
class pedidoproducto_attribute:
    # name = graphene.String(description="Name of the pedidoproducto.")
    idpedido=graphene.Int()
    idpedidodireccion=graphene.Int()
    idproducto=graphene.Int()
    titulo=graphene.String()
    mensaje=graphene.String()
    idproductoatributo=graphene.Int()
    titulo_atributo=graphene.String()
    precio=graphene.Int()
    cantidad=graphene.Int()
    total=graphene.Int()
   



class create_pedidoproducto_input(graphene.InputObjectType, pedidoproducto_attribute):
    """Arguments to create a pedidoproducto."""
    pass


class create_pedidoproducto(graphene.Mutation):
    """Mutation to create a pedidoproducto."""
    pedidoproducto = graphene.Field(lambda: pedidoproducto_schema, description="pedidoproducto created by this mutation.")

    class Arguments:
        input = create_pedidoproducto_input(required=True)

    def mutate(self, info, input):
        pedidoproducto=mutation_create(pedidoproducto_model,idpedidoproducto)

        return create_pedidoproducto(pedidoproducto=pedidoproducto)


class update_pedidoproducto_input(graphene.InputObjectType, pedidoproducto_attribute):
    """Arguments to update a pedidoproducto."""
    idpedidoproducto = graphene.ID(required=True, description="Global Id of the pedidoproducto.")


class update_pedidoproducto(graphene.Mutation):
    """Update a pedidoproducto."""
    pedidoproducto = graphene.Field(lambda: pedidoproducto_schema, description="pedidoproducto updated by this mutation.")

    class Arguments:
        input = update_pedidoproducto_input(required=True)

    def mutate(self, info, input):
        pedidoproducto=mutation_update(pedidoproducto_model,idpedidoproducto)
        return update_pedidoproducto(pedidoproducto=pedidoproducto)