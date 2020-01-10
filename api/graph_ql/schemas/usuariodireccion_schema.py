
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import usuariodireccion_model
from ..resolver import resolve
from ..mutator import mutation_create

# __REPLACE__

class usuariodireccion_schema(SQLAlchemyObjectType):
    class Meta:
        model = usuariodireccion_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idusuariodireccion','idusuario','tipo','titulo','nombre','direccion','idcomuna','telefono','villa','edificio','departamento','condominio','casa','empresa','referencias']


def resolve_usuariodireccion( args, info,idusuariodireccion, **kwargs ):
    query= resolve(args,info,usuariodireccion_schema,usuariodireccion_model,idusuariodireccion=idusuariodireccion,**kwargs)
    return query.first()

def resolve_all_usuariodireccion( args, info, **kwargs):
    query= resolve(args,info,usuariodireccion_schema,usuariodireccion_model,**kwargs)
    return query



all_usuariodireccion = SQLAlchemyConnectionField(usuariodireccion_schema,idusuario=graphene.Int(),tipo=graphene.Int(),titulo=graphene.String(),nombre=graphene.String(),direccion=graphene.String(),idcomuna=graphene.Int(),telefono=graphene.String(),villa=graphene.String(),edificio=graphene.String(),departamento=graphene.String(),condominio=graphene.String(),casa=graphene.String(),empresa=graphene.String(),referencias=graphene.String())
usuariodireccion = graphene.Field(usuariodireccion_schema,idusuariodireccion=graphene.Int(),idusuario=graphene.Int(),tipo=graphene.Int(),titulo=graphene.String(),nombre=graphene.String(),direccion=graphene.String(),idcomuna=graphene.Int(),telefono=graphene.String(),villa=graphene.String(),edificio=graphene.String(),departamento=graphene.String(),condominio=graphene.String(),casa=graphene.String(),empresa=graphene.String(),referencias=graphene.String())

# __REPLACE__



# Create a generic class to mutualize description of usuariodireccion _attributes for both queries and mutations
class usuariodireccion_attribute:
    # name = graphene.String(description="Name of the usuariodireccion.")
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
   



class create_usuariodireccion_input(graphene.InputObjectType, usuariodireccion_attribute):
    """Arguments to create a usuariodireccion."""
    pass


class create_usuariodireccion(graphene.Mutation):
    """Mutation to create a usuariodireccion."""
    usuariodireccion = graphene.Field(lambda: usuariodireccion_schema, description="usuariodireccion created by this mutation.")

    class Arguments:
        input = create_usuariodireccion_input(required=True)

    def mutate(self, info, input):
        usuariodireccion=mutation_create(usuariodireccion_model,idusuariodireccion)

        return create_usuariodireccion(usuariodireccion=usuariodireccion)


class update_usuariodireccion_input(graphene.InputObjectType, usuariodireccion_attribute):
    """Arguments to update a usuariodireccion."""
    idusuariodireccion = graphene.ID(required=True, description="Global Id of the usuariodireccion.")


class update_usuariodireccion(graphene.Mutation):
    """Update a usuariodireccion."""
    usuariodireccion = graphene.Field(lambda: usuariodireccion_schema, description="usuariodireccion updated by this mutation.")

    class Arguments:
        input = update_usuariodireccion_input(required=True)

    def mutate(self, info, input):
        usuariodireccion=mutation_update(usuariodireccion_model,idusuariodireccion)
        return update_usuariodireccion(usuariodireccion=usuariodireccion)