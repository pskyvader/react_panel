
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import mediopago_model
from ..resolver import resolve
from ..mutator import mutation_create,mutation_update

# __REPLACE__

class mediopago_schema(SQLAlchemyObjectType):
    class Meta:
        model = mediopago_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idmediopago','titulo','resumen','descripcion','orden','estado']


def resolve_mediopago( args, info,idmediopago, **kwargs ):
    query= resolve(args,info,mediopago_schema,mediopago_model,idmediopago=idmediopago,**kwargs)
    return query.first()

def resolve_all_mediopago( args, info, **kwargs):
    query= resolve(args,info,mediopago_schema,mediopago_model,**kwargs)
    return query



all_mediopago = SQLAlchemyConnectionField(mediopago_schema,titulo=graphene.String(),resumen=graphene.String(),descripcion=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean())
mediopago = graphene.Field(mediopago_schema,idmediopago=graphene.Int(),titulo=graphene.String(),resumen=graphene.String(),descripcion=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean())

# __REPLACE__



# Create a generic class to mutualize description of mediopago _attributes for both queries and mutations
class mediopago_attribute:
    # name = graphene.String(description="Name of the mediopago.")
    titulo=graphene.String()
    resumen=graphene.String()
    descripcion=graphene.String()
    orden=graphene.Int()
    estado=graphene.Boolean()
   



class create_mediopago_input(graphene.InputObjectType, mediopago_attribute):
    """Arguments to create a mediopago."""
    pass


class create_mediopago(graphene.Mutation):
    """Mutation to create a mediopago."""
    mediopago = graphene.Field(lambda: mediopago_schema, description="mediopago created by this mutation.")

    class Arguments:
        input = create_mediopago_input(required=True)

    def mutate(self, info, input):
        mediopago=mutation_create(mediopago_model,input,'idmediopago')

        return create_mediopago(mediopago=mediopago)


class update_mediopago_input(graphene.InputObjectType, mediopago_attribute):
    """Arguments to update a mediopago."""
    idmediopago = graphene.ID(required=True, description="Global Id of the mediopago.")


class update_mediopago(graphene.Mutation):
    """Update a mediopago."""
    mediopago = graphene.Field(lambda: mediopago_schema, description="mediopago updated by this mutation.")

    class Arguments:
        input = update_mediopago_input(required=True)

    def mutate(self, info, input):
        mediopago=mutation_update(mediopago_model,input,'idmediopago')
        return update_mediopago(mediopago=mediopago)