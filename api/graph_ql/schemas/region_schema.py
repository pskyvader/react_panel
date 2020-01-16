
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import region_model
from ..resolver import resolve
from ..mutator import mutation_create,mutation_update

# __REPLACE__

class region_schema(SQLAlchemyObjectType):
    class Meta:
        model = region_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idregion','titulo','precio','orden','estado']


def resolve_region( args, info,idregion, **kwargs ):
    query= resolve(args,info,region_schema,region_model,idregion=idregion,**kwargs)
    return query.first()

def resolve_all_region( args, info, **kwargs):
    query= resolve(args,info,region_schema,region_model,**kwargs)
    return query



all_region = SQLAlchemyConnectionField(region_schema,titulo=graphene.String(),precio=graphene.Int(),orden=graphene.Int(),estado=graphene.Boolean())
region = graphene.Field(region_schema,idregion=graphene.Int(),titulo=graphene.String(),precio=graphene.Int(),orden=graphene.Int(),estado=graphene.Boolean())

# __REPLACE__



# Create a generic class to mutualize description of region _attributes for both queries and mutations
class region_attribute:
    # name = graphene.String(description="Name of the region.")
    titulo=graphene.String()
    precio=graphene.Int()
    orden=graphene.Int()
    estado=graphene.Boolean()
   



class create_region_input(graphene.InputObjectType, region_attribute):
    """Arguments to create a region."""
    pass


class create_region(graphene.Mutation):
    """Mutation to create a region."""
    region = graphene.Field(lambda: region_schema, description="region created by this mutation.")

    class Arguments:
        input = create_region_input(required=True)

    def mutate(self, info, input):
        region=mutation_create(region_model,input,'idregion')

        return create_region(region=region)


class update_region_input(graphene.InputObjectType, region_attribute):
    """Arguments to update a region."""
    idregion = graphene.ID(required=True, description="Global Id of the region.")


class update_region(graphene.Mutation):
    """Update a region."""
    region = graphene.Field(lambda: region_schema, description="region updated by this mutation.")

    class Arguments:
        input = update_region_input(required=True)

    def mutate(self, info, input):
        region=mutation_update(region_model,input,'idregion')
        return update_region(region=region)