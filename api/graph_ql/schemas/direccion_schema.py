
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import direccion_model
from ..resolver import resolve
from ..mutator import mutation_create

# __REPLACE__

class direccion_schema(SQLAlchemyObjectType):
    class Meta:
        model = direccion_model
        interfaces = (graphene.relay.Node, )
        only_fields=['iddireccion','idusuario','tipo','titulo','nombre','direccion','idcomuna','telefono','villa','edificio','departamento','condominio','casa','empresa','referencias']


def resolve_direccion( args, info,iddireccion, **kwargs ):
    query= resolve(args,info,direccion_schema,direccion_model,iddireccion=iddireccion,**kwargs)
    return query.first()

def resolve_all_direccion( args, info, **kwargs):
    query= resolve(args,info,direccion_schema,direccion_model,**kwargs)
    return query



all_direccion = SQLAlchemyConnectionField(direccion_schema,idusuario=graphene.Int(),tipo=graphene.Int(),titulo=graphene.String(),nombre=graphene.String(),direccion=graphene.String(),idcomuna=graphene.Int(),telefono=graphene.String(),villa=graphene.String(),edificio=graphene.String(),departamento=graphene.String(),condominio=graphene.String(),casa=graphene.String(),empresa=graphene.String(),referencias=graphene.String())
direccion = graphene.Field(direccion_schema,iddireccion=graphene.Int(),idusuario=graphene.Int(),tipo=graphene.Int(),titulo=graphene.String(),nombre=graphene.String(),direccion=graphene.String(),idcomuna=graphene.Int(),telefono=graphene.String(),villa=graphene.String(),edificio=graphene.String(),departamento=graphene.String(),condominio=graphene.String(),casa=graphene.String(),empresa=graphene.String(),referencias=graphene.String())

# __REPLACE__



# Create a generic class to mutualize description of direccion _attributes for both queries and mutations
class direccion_attribute:
    # name = graphene.String(description="Name of the direccion.")
    idusuario=graphene.Int()
    tipo=graphene.Int()
    titulo=graphene.String()
    nombre=graphene.String()
    direccion=graphene.String()
    idcomuna=graphene.Int()
    telefono=graphene.String()
    villa=graphene.String()
    edificio=graphene.String()
    departamento=graphene.String()
    condominio=graphene.String()
    casa=graphene.String()
    empresa=graphene.String()
    referencias=graphene.String()
   



class create_direccion_input(graphene.InputObjectType, direccion_attribute):
    """Arguments to create a direccion."""
    pass


class create_direccion(graphene.Mutation):
    """Mutation to create a direccion."""
    direccion = graphene.Field(lambda: direccion_schema, description="direccion created by this mutation.")

    class Arguments:
        input = create_direccion_input(required=True)

    def mutate(self, info, input):
        direccion=mutation_create(direccion_model,iddireccion)

        return create_direccion(direccion=direccion)


class update_direccion_input(graphene.InputObjectType, direccion_attribute):
    """Arguments to update a direccion."""
    iddireccion = graphene.ID(required=True, description="Global Id of the direccion.")


class update_direccion(graphene.Mutation):
    """Update a direccion."""
    direccion = graphene.Field(lambda: direccion_schema, description="direccion updated by this mutation.")

    class Arguments:
        input = update_direccion_input(required=True)

    def mutate(self, info, input):
        direccion=mutation_update(direccion_model,iddireccion)
        return update_direccion(direccion=direccion)