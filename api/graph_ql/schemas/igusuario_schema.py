
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import igusuario_model
from ..resolver import resolve
from ..mutator import mutation_create,mutation_update

class igusuario_schema(SQLAlchemyObjectType):
    class Meta:
        model = igusuario_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idigusuario','usuario','estado']

def resolve_igusuario( args, info,idigusuario, **kwargs ):
    query= resolve(args,info,igusuario_schema,igusuario_model,idigusuario=idigusuario,**kwargs)
    return query.first()

def resolve_all_igusuario( args, info, **kwargs):
    query= resolve(args,info,igusuario_schema,igusuario_model,**kwargs)
    return query

all_igusuario = SQLAlchemyConnectionField(igusuario_schema,sort=graphene.String(),usuario=graphene.String(),estado=graphene.Boolean())
igusuario = graphene.Field(igusuario_schema,idigusuario=graphene.Int(),usuario=graphene.String(),estado=graphene.Boolean())

# Create a generic class to mutualize description of igusuario _attributes for both queries and mutations
class igusuario_attribute:
    # name = graphene.String(description="Name of the igusuario.")
    usuario=graphene.String()
    estado=graphene.Boolean()
   

class create_igusuario_input(graphene.InputObjectType, igusuario_attribute):
    """Arguments to create a igusuario."""
    pass

class create_igusuario(graphene.Mutation):
    """Mutation to create a igusuario."""
    igusuario = graphene.Field(lambda: igusuario_schema, description="igusuario created by this mutation.")

    class Arguments:
        input = create_igusuario_input(required=True)

    def mutate(self, info, input):
        igusuario=mutation_create(igusuario_model,input,'idigusuario')
        return create_igusuario(igusuario=igusuario)

class update_igusuario_input(graphene.InputObjectType, igusuario_attribute):
    """Arguments to update a igusuario."""
    idigusuario = graphene.ID(required=True, description="Global Id of the igusuario.")

class update_igusuario(graphene.Mutation):
    """Update a igusuario."""
    igusuario = graphene.Field(lambda: igusuario_schema, description="igusuario updated by this mutation.")

    class Arguments:
        input = update_igusuario_input(required=True)

    def mutate(self, info, input):
        igusuario=mutation_update(igusuario_model,input,'idigusuario')
        return update_igusuario(igusuario=igusuario)