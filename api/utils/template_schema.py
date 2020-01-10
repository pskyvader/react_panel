
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import TABLENAME_model
from ..resolver import resolve
from ..mutator import mutation_create

# __REPLACE__

class TABLENAME_schema(SQLAlchemyObjectType):
    class Meta:
        model = TABLENAME_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idTABLENAME',ONLY_FIELDS]


def resolve_TABLENAME( args, info,idTABLENAME, **kwargs ):
    query= resolve(args,info,TABLENAME_schema,TABLENAME_model,idTABLENAME=idTABLENAME,**kwargs)
    return query.first()

def resolve_all_TABLENAME( args, info, **kwargs):
    query= resolve(args,info,TABLENAME_schema,TABLENAME_model,**kwargs)
    return query



all_TABLENAME = SQLAlchemyConnectionField(TABLENAME_schema,EXTRA_FIELDS)
TABLENAME = graphene.Field(TABLENAME_schema,idTABLENAME=graphene.Int(),EXTRA_FIELDS)

# __REPLACE__



# Create a generic class to mutualize description of TABLENAME _attributes for both queries and mutations
class TABLENAME_attribute:
    # name = graphene.String(description="Name of the TABLENAME.")
    EXTRA_FIELDS_BREAK_LINE



class create_TABLENAME_input(graphene.InputObjectType, TABLENAME_attribute):
    """Arguments to create a TABLENAME."""
    pass


class create_TABLENAME(graphene.Mutation):
    """Mutation to create a TABLENAME."""
    TABLENAME = graphene.Field(lambda: TABLENAME_schema, description="TABLENAME created by this mutation.")

    class Arguments:
        input = create_TABLENAME_input(required=True)

    def mutate(self, info, input):
        TABLENAME=mutation_create(TABLENAME_model,idTABLENAME)

        return create_TABLENAME(TABLENAME=TABLENAME)


class update_TABLENAME_input(graphene.InputObjectType, TABLENAME_attribute):
    """Arguments to update a TABLENAME."""
    idTABLENAME = graphene.ID(required=True, description="Global Id of the TABLENAME.")


class update_TABLENAME(graphene.Mutation):
    """Update a TABLENAME."""
    TABLENAME = graphene.Field(lambda: TABLENAME_schema, description="TABLENAME updated by this mutation.")

    class Arguments:
        input = update_TABLENAME_input(required=True)

    def mutate(self, info, input):
        TABLENAME=mutation_update(TABLENAME_model,idTABLENAME)
        return update_TABLENAME(TABLENAME=TABLENAME)