
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import comuna_model
from ..resolver import resolve
from ..mutator import mutation_create,mutation_update

class comuna_schema(SQLAlchemyObjectType):
    class Meta:
        model = comuna_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idcomuna','idregion','titulo','precio','orden','estado']

def resolve_comuna( args, info,idcomuna, **kwargs ):
    query= resolve(args,info,comuna_schema,comuna_model,idcomuna=idcomuna,**kwargs)
    return query.first()

def resolve_all_comuna( args, info, **kwargs):
    query= resolve(args,info,comuna_schema,comuna_model,**kwargs)
    return query

all_comuna = SQLAlchemyConnectionField(comuna_schema,sort=graphene.String(),idregion=graphene.Int(),titulo=graphene.String(),precio=graphene.Int(),orden=graphene.Int(),estado=graphene.Boolean())
comuna = graphene.Field(comuna_schema,idcomuna=graphene.Int(),idregion=graphene.Int(),titulo=graphene.String(),precio=graphene.Int(),orden=graphene.Int(),estado=graphene.Boolean())

# Create a generic class to mutualize description of comuna _attributes for both queries and mutations
class comuna_attribute:
    # name = graphene.String(description="Name of the comuna.")
    idregion=graphene.Int()
    titulo=graphene.String()
    precio=graphene.Int()
    orden=graphene.Int()
    estado=graphene.Boolean()
   

class create_comuna_input(graphene.InputObjectType, comuna_attribute):
    """Arguments to create a comuna."""
    pass

class create_comuna(graphene.Mutation):
    """Mutation to create a comuna."""
    comuna = graphene.Field(lambda: comuna_schema, description="comuna created by this mutation.")

    class Arguments:
        input = create_comuna_input(required=True)

    def mutate(self, info, input):
        comuna=mutation_create(comuna_model,input,'idcomuna')
        return create_comuna(comuna=comuna)

class update_comuna_input(graphene.InputObjectType, comuna_attribute):
    """Arguments to update a comuna."""
    idcomuna = graphene.ID(required=True, description="Global Id of the comuna.")

class update_comuna(graphene.Mutation):
    """Update a comuna."""
    comuna = graphene.Field(lambda: comuna_schema, description="comuna updated by this mutation.")

    class Arguments:
        input = update_comuna_input(required=True)

    def mutate(self, info, input):
        comuna=mutation_update(comuna_model,input,'idcomuna')
        return update_comuna(comuna=comuna)