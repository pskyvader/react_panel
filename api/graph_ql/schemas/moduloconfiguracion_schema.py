
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import moduloconfiguracion_model
from ..resolver import resolve
from ..mutator import mutation_create

# __REPLACE__

class moduloconfiguracion_schema(SQLAlchemyObjectType):
    class Meta:
        model = moduloconfiguracion_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idmoduloconfiguracion','icono','module','titulo','sub','padre','mostrar','detalle','orden','estado','aside','tipos']


def resolve_moduloconfiguracion( args, info,idmoduloconfiguracion, **kwargs ):
    query= resolve(args,info,moduloconfiguracion_schema,moduloconfiguracion_model,idmoduloconfiguracion=idmoduloconfiguracion,**kwargs)
    return query.first()

def resolve_all_moduloconfiguracion( args, info, **kwargs):
    query= resolve(args,info,moduloconfiguracion_schema,moduloconfiguracion_model,**kwargs)
    return query



all_moduloconfiguracion = SQLAlchemyConnectionField(moduloconfiguracion_schema,icono=graphene.String(),module=graphene.String(),titulo=graphene.String(),sub=graphene.String(),padre=graphene.String(),mostrar=graphene.String(),detalle=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean(),aside=graphene.Boolean(),tipos=graphene.Boolean())
moduloconfiguracion = graphene.Field(moduloconfiguracion_schema,idmoduloconfiguracion=graphene.Int(),icono=graphene.String(),module=graphene.String(),titulo=graphene.String(),sub=graphene.String(),padre=graphene.String(),mostrar=graphene.String(),detalle=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean(),aside=graphene.Boolean(),tipos=graphene.Boolean())

# __REPLACE__



# Create a generic class to mutualize description of moduloconfiguracion _attributes for both queries and mutations
class moduloconfiguracion_attribute:
    # name = graphene.String(description="Name of the moduloconfiguracion.")
    icono=graphene.String()
    module=graphene.String()
    titulo=graphene.String()
    sub=graphene.String()
    padre=graphene.String()
    mostrar=graphene.String()
    detalle=graphene.String()
    orden=graphene.Int()
    estado=graphene.Boolean()
    aside=graphene.Boolean()
    tipos=graphene.Boolean()
   



class create_moduloconfiguracion_input(graphene.InputObjectType, moduloconfiguracion_attribute):
    """Arguments to create a moduloconfiguracion."""
    pass


class create_moduloconfiguracion(graphene.Mutation):
    """Mutation to create a moduloconfiguracion."""
    moduloconfiguracion = graphene.Field(lambda: moduloconfiguracion_schema, description="moduloconfiguracion created by this mutation.")

    class Arguments:
        input = create_moduloconfiguracion_input(required=True)

    def mutate(self, info, input):
        moduloconfiguracion=mutation_create(moduloconfiguracion_model,idmoduloconfiguracion)

        return create_moduloconfiguracion(moduloconfiguracion=moduloconfiguracion)


class update_moduloconfiguracion_input(graphene.InputObjectType, moduloconfiguracion_attribute):
    """Arguments to update a moduloconfiguracion."""
    idmoduloconfiguracion = graphene.ID(required=True, description="Global Id of the moduloconfiguracion.")


class update_moduloconfiguracion(graphene.Mutation):
    """Update a moduloconfiguracion."""
    moduloconfiguracion = graphene.Field(lambda: moduloconfiguracion_schema, description="moduloconfiguracion updated by this mutation.")

    class Arguments:
        input = update_moduloconfiguracion_input(required=True)

    def mutate(self, info, input):
        moduloconfiguracion=mutation_update(moduloconfiguracion_model,idmoduloconfiguracion)
        return update_moduloconfiguracion(moduloconfiguracion=moduloconfiguracion)