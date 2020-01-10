
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import configuracion_model
from ..resolver import resolve
from ..mutator import mutation_create

# __REPLACE__

class configuracion_schema(SQLAlchemyObjectType):
    class Meta:
        model = configuracion_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idconfiguracion','variable','valor']


def resolve_configuracion( args, info,idconfiguracion, **kwargs ):
    query= resolve(args,info,configuracion_schema,configuracion_model,idconfiguracion=idconfiguracion,**kwargs)
    return query.first()

def resolve_all_configuracion( args, info, **kwargs):
    query= resolve(args,info,configuracion_schema,configuracion_model,**kwargs)
    return query



all_configuracion = SQLAlchemyConnectionField(configuracion_schema,variable=graphene.String(),valor=graphene.String())
configuracion = graphene.Field(configuracion_schema,idconfiguracion=graphene.Int(),variable=graphene.String(),valor=graphene.String())

# __REPLACE__



# Create a generic class to mutualize description of configuracion _attributes for both queries and mutations
class configuracion_attribute:
    # name = graphene.String(description="Name of the configuracion.")
    variable=graphene.String()
    valor=graphene.String()
   



class create_configuracion_input(graphene.InputObjectType, configuracion_attribute):
    """Arguments to create a configuracion."""
    pass


class create_configuracion(graphene.Mutation):
    """Mutation to create a configuracion."""
    configuracion = graphene.Field(lambda: configuracion_schema, description="configuracion created by this mutation.")

    class Arguments:
        input = create_configuracion_input(required=True)

    def mutate(self, info, input):
        configuracion=mutation_create(configuracion_model,idconfiguracion)

        return create_configuracion(configuracion=configuracion)


class update_configuracion_input(graphene.InputObjectType, configuracion_attribute):
    """Arguments to update a configuracion."""
    idconfiguracion = graphene.ID(required=True, description="Global Id of the configuracion.")


class update_configuracion(graphene.Mutation):
    """Update a configuracion."""
    configuracion = graphene.Field(lambda: configuracion_schema, description="configuracion updated by this mutation.")

    class Arguments:
        input = update_configuracion_input(required=True)

    def mutate(self, info, input):
        configuracion=mutation_update(configuracion_model,idconfiguracion)
        return update_configuracion(configuracion=configuracion)