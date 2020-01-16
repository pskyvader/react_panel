
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import usuario_model
from ..resolver import resolve
from ..mutator import mutation_create,mutation_update

# __REPLACE__

class usuario_schema(SQLAlchemyObjectType):
    class Meta:
        model = usuario_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idusuario','tipo','nombre','telefono','email','foto','estado','cookie']


def resolve_usuario( args, info,idusuario, **kwargs ):
    query= resolve(args,info,usuario_schema,usuario_model,idusuario=idusuario,**kwargs)
    return query.first()

def resolve_all_usuario( args, info, **kwargs):
    query= resolve(args,info,usuario_schema,usuario_model,**kwargs)
    return query



all_usuario = SQLAlchemyConnectionField(usuario_schema,tipo=graphene.Int(),nombre=graphene.String(),telefono=graphene.String(),email=graphene.String(),estado=graphene.Boolean(),cookie=graphene.String())
usuario = graphene.Field(usuario_schema,idusuario=graphene.Int(),tipo=graphene.Int(),nombre=graphene.String(),telefono=graphene.String(),email=graphene.String(),estado=graphene.Boolean(),cookie=graphene.String())

# __REPLACE__



# Create a generic class to mutualize description of usuario _attributes for both queries and mutations
class usuario_attribute:
    # name = graphene.String(description="Name of the usuario.")
    tipo=graphene.Int()
    nombre=graphene.String()
    telefono=graphene.String()
    email=graphene.String()
    estado=graphene.Boolean()
    cookie=graphene.String()
   



class create_usuario_input(graphene.InputObjectType, usuario_attribute):
    """Arguments to create a usuario."""
    pass


class create_usuario(graphene.Mutation):
    """Mutation to create a usuario."""
    usuario = graphene.Field(lambda: usuario_schema, description="usuario created by this mutation.")

    class Arguments:
        input = create_usuario_input(required=True)

    def mutate(self, info, input):
        usuario=mutation_create(usuario_model,input,'idusuario')

        return create_usuario(usuario=usuario)


class update_usuario_input(graphene.InputObjectType, usuario_attribute):
    """Arguments to update a usuario."""
    idusuario = graphene.ID(required=True, description="Global Id of the usuario.")


class update_usuario(graphene.Mutation):
    """Update a usuario."""
    usuario = graphene.Field(lambda: usuario_schema, description="usuario updated by this mutation.")

    class Arguments:
        input = update_usuario_input(required=True)

    def mutate(self, info, input):
        usuario=mutation_update(usuario_model,input,'idusuario')
        return update_usuario(usuario=usuario)