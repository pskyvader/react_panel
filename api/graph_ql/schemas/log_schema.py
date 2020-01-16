
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import log_model
from ..resolver import resolve
from ..mutator import mutation_create,mutation_update

# __REPLACE__

class log_schema(SQLAlchemyObjectType):
    class Meta:
        model = log_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idlog','administrador','tabla','accion','fecha']


def resolve_log( args, info,idlog, **kwargs ):
    query= resolve(args,info,log_schema,log_model,idlog=idlog,**kwargs)
    return query.first()

def resolve_all_log( args, info, **kwargs):
    query= resolve(args,info,log_schema,log_model,**kwargs)
    return query



all_log = SQLAlchemyConnectionField(log_schema,administrador=graphene.String(),tabla=graphene.String(),accion=graphene.String(),fecha=graphene.types.datetime.DateTime())
log = graphene.Field(log_schema,idlog=graphene.Int(),administrador=graphene.String(),tabla=graphene.String(),accion=graphene.String(),fecha=graphene.types.datetime.DateTime())

# __REPLACE__



# Create a generic class to mutualize description of log _attributes for both queries and mutations
class log_attribute:
    # name = graphene.String(description="Name of the log.")
    administrador=graphene.String()
    tabla=graphene.String()
    accion=graphene.String()
    fecha=graphene.types.datetime.DateTime()
   



class create_log_input(graphene.InputObjectType, log_attribute):
    """Arguments to create a log."""
    pass


class create_log(graphene.Mutation):
    """Mutation to create a log."""
    log = graphene.Field(lambda: log_schema, description="log created by this mutation.")

    class Arguments:
        input = create_log_input(required=True)

    def mutate(self, info, input):
        log=mutation_create(log_model,input,'idlog')

        return create_log(log=log)


class update_log_input(graphene.InputObjectType, log_attribute):
    """Arguments to update a log."""
    idlog = graphene.ID(required=True, description="Global Id of the log.")


class update_log(graphene.Mutation):
    """Update a log."""
    log = graphene.Field(lambda: log_schema, description="log updated by this mutation.")

    class Arguments:
        input = update_log_input(required=True)

    def mutate(self, info, input):
        log=mutation_update(log_model,input,'idlog')
        return update_log(log=log)