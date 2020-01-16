
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import igtotal_model
from ..resolver import resolve
from ..mutator import mutation_create,mutation_update

class igtotal_schema(SQLAlchemyObjectType):
    class Meta:
        model = igtotal_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idigtotal','tag','fecha','cantidad']

def resolve_igtotal( args, info,idigtotal, **kwargs ):
    query= resolve(args,info,igtotal_schema,igtotal_model,idigtotal=idigtotal,**kwargs)
    return query.first()

def resolve_all_igtotal( args, info, **kwargs):
    query= resolve(args,info,igtotal_schema,igtotal_model,**kwargs)
    return query

all_igtotal = SQLAlchemyConnectionField(igtotal_schema,sort=graphene.String(),tag=graphene.String(),fecha=graphene.types.datetime.DateTime(),cantidad=graphene.Int())
igtotal = graphene.Field(igtotal_schema,idigtotal=graphene.Int(),tag=graphene.String(),fecha=graphene.types.datetime.DateTime(),cantidad=graphene.Int())

# Create a generic class to mutualize description of igtotal _attributes for both queries and mutations
class igtotal_attribute:
    # name = graphene.String(description="Name of the igtotal.")
    tag=graphene.String()
    fecha=graphene.types.datetime.DateTime()
    cantidad=graphene.Int()
   

class create_igtotal_input(graphene.InputObjectType, igtotal_attribute):
    """Arguments to create a igtotal."""
    pass

class create_igtotal(graphene.Mutation):
    """Mutation to create a igtotal."""
    igtotal = graphene.Field(lambda: igtotal_schema, description="igtotal created by this mutation.")

    class Arguments:
        input = create_igtotal_input(required=True)

    def mutate(self, info, input):
        igtotal=mutation_create(igtotal_model,input,'idigtotal')
        return create_igtotal(igtotal=igtotal)

class update_igtotal_input(graphene.InputObjectType, igtotal_attribute):
    """Arguments to update a igtotal."""
    idigtotal = graphene.ID(required=True, description="Global Id of the igtotal.")

class update_igtotal(graphene.Mutation):
    """Update a igtotal."""
    igtotal = graphene.Field(lambda: igtotal_schema, description="igtotal updated by this mutation.")

    class Arguments:
        input = update_igtotal_input(required=True)

    def mutate(self, info, input):
        igtotal=mutation_update(igtotal_model,input,'idigtotal')
        return update_igtotal(igtotal=igtotal)