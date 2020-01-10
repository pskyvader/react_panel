
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import pedido_model
from ..resolver import resolve
from ..mutator import mutation_create

# __REPLACE__

class pedido_schema(SQLAlchemyObjectType):
    class Meta:
        model = pedido_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idpedido','tipo','cookie_pedido','fecha_creacion','fecha_pago','idusuario','idpedidoestado','idmediopago','nombre','email','telefono','total_original','total','comentarios','pedido_manual']


def resolve_pedido( args, info,idpedido, **kwargs ):
    query= resolve(args,info,pedido_schema,pedido_model,idpedido=idpedido,**kwargs)
    return query.first()

def resolve_all_pedido( args, info, **kwargs):
    query= resolve(args,info,pedido_schema,pedido_model,**kwargs)
    return query



all_pedido = SQLAlchemyConnectionField(pedido_schema,tipo=graphene.Int(),cookie_pedido=graphene.String(),fecha_creacion=graphene.types.datetime.DateTime(),fecha_pago=graphene.types.datetime.DateTime(),idusuario=graphene.Int(),idpedidoestado=graphene.Int(),idmediopago=graphene.Int(),nombre=graphene.String(),email=graphene.String(),telefono=graphene.String(),total_original=graphene.Int(),total=graphene.Int(),comentarios=graphene.String(),pedido_manual=graphene.Boolean())
pedido = graphene.Field(pedido_schema,idpedido=graphene.Int(),tipo=graphene.Int(),cookie_pedido=graphene.String(),fecha_creacion=graphene.types.datetime.DateTime(),fecha_pago=graphene.types.datetime.DateTime(),idusuario=graphene.Int(),idpedidoestado=graphene.Int(),idmediopago=graphene.Int(),nombre=graphene.String(),email=graphene.String(),telefono=graphene.String(),total_original=graphene.Int(),total=graphene.Int(),comentarios=graphene.String(),pedido_manual=graphene.Boolean())

# __REPLACE__



# Create a generic class to mutualize description of pedido _attributes for both queries and mutations
class pedido_attribute:
    # name = graphene.String(description="Name of the pedido.")
    tipo=graphene.Int()
    cookie_pedido=graphene.String()
    fecha_creacion=graphene.types.datetime.DateTime()
    fecha_pago=graphene.types.datetime.DateTime()
    idusuario=graphene.Int()
    idpedidoestado=graphene.Int()
    idmediopago=graphene.Int()
    nombre=graphene.String()
    email=graphene.String()
    telefono=graphene.String()
    total_original=graphene.Int()
    total=graphene.Int()
    comentarios=graphene.String()
    pedido_manual=graphene.Boolean()
   



class create_pedido_input(graphene.InputObjectType, pedido_attribute):
    """Arguments to create a pedido."""
    pass


class create_pedido(graphene.Mutation):
    """Mutation to create a pedido."""
    pedido = graphene.Field(lambda: pedido_schema, description="pedido created by this mutation.")

    class Arguments:
        input = create_pedido_input(required=True)

    def mutate(self, info, input):
        pedido=mutation_create(pedido_model,idpedido)

        return create_pedido(pedido=pedido)


class update_pedido_input(graphene.InputObjectType, pedido_attribute):
    """Arguments to update a pedido."""
    idpedido = graphene.ID(required=True, description="Global Id of the pedido.")


class update_pedido(graphene.Mutation):
    """Update a pedido."""
    pedido = graphene.Field(lambda: pedido_schema, description="pedido updated by this mutation.")

    class Arguments:
        input = update_pedido_input(required=True)

    def mutate(self, info, input):
        pedido=mutation_update(pedido_model,idpedido)
        return update_pedido(pedido=pedido)