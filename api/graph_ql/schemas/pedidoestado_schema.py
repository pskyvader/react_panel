
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import pedidoestado_model
from ..resolver import resolve
from ..mutator import mutation_create,mutation_update

class pedidoestado_schema(SQLAlchemyObjectType):
    class Meta:
        model = pedidoestado_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idpedidoestado','tipo','titulo','resumen','color','orden','estado']

def resolve_pedidoestado( args, info,idpedidoestado, **kwargs ):
    query= resolve(args,info,pedidoestado_schema,pedidoestado_model,idpedidoestado=idpedidoestado,**kwargs)
    return query.first()

def resolve_all_pedidoestado( args, info, **kwargs):
    query= resolve(args,info,pedidoestado_schema,pedidoestado_model,**kwargs)
    return query

all_pedidoestado = SQLAlchemyConnectionField(pedidoestado_schema,sort=graphene.String(),tipo=graphene.Int(),titulo=graphene.String(),resumen=graphene.String(),color=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean())
pedidoestado = graphene.Field(pedidoestado_schema,idpedidoestado=graphene.Int(),tipo=graphene.Int(),titulo=graphene.String(),resumen=graphene.String(),color=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean())

# Create a generic class to mutualize description of pedidoestado _attributes for both queries and mutations
class pedidoestado_attribute:
    # name = graphene.String(description="Name of the pedidoestado.")
    tipo=graphene.Int()
    titulo=graphene.String()
    resumen=graphene.String()
    color=graphene.String()
    orden=graphene.Int()
    estado=graphene.Boolean()
   

class create_pedidoestado_input(graphene.InputObjectType, pedidoestado_attribute):
    """Arguments to create a pedidoestado."""
    pass

class create_pedidoestado(graphene.Mutation):
    """Mutation to create a pedidoestado."""
    pedidoestado = graphene.Field(lambda: pedidoestado_schema, description="pedidoestado created by this mutation.")

    class Arguments:
        input = create_pedidoestado_input(required=True)

    def mutate(self, info, input):
        pedidoestado=mutation_create(pedidoestado_model,input,'idpedidoestado')
        return create_pedidoestado(pedidoestado=pedidoestado)

class update_pedidoestado_input(graphene.InputObjectType, pedidoestado_attribute):
    """Arguments to update a pedidoestado."""
    idpedidoestado = graphene.ID(required=True, description="Global Id of the pedidoestado.")

class update_pedidoestado(graphene.Mutation):
    """Update a pedidoestado."""
    pedidoestado = graphene.Field(lambda: pedidoestado_schema, description="pedidoestado updated by this mutation.")

    class Arguments:
        input = update_pedidoestado_input(required=True)

    def mutate(self, info, input):
        pedidoestado=mutation_update(pedidoestado_model,input,'idpedidoestado')
        return update_pedidoestado(pedidoestado=pedidoestado)