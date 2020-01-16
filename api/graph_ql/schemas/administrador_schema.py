
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import administrador_model
from ..resolver import resolve
from ..mutator import mutation_create

# __REPLACE__

class administrador_schema(SQLAlchemyObjectType):
    class Meta:
        model = administrador_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idadministrador','tipo','email','nombre','foto','estado','cookie']


def resolve_administrador( args, info,idadministrador, **kwargs ):
    query= resolve(args,info,administrador_schema,administrador_model,idadministrador=idadministrador,**kwargs)
    return query.first()

def resolve_all_administrador( args, info, **kwargs):
    query= resolve(args,info,administrador_schema,administrador_model,**kwargs)
    return query



all_administrador = SQLAlchemyConnectionField(administrador_schema,tipo=graphene.Int(),email=graphene.String(),nombre=graphene.String(),estado=graphene.Boolean(),cookie=graphene.String())
administrador = graphene.Field(administrador_schema,idadministrador=graphene.Int(),tipo=graphene.Int(),email=graphene.String(),nombre=graphene.String(),estado=graphene.Boolean(),cookie=graphene.String())

# __REPLACE__



# Create a generic class to mutualize description of administrador _attributes for both queries and mutations
class administrador_attribute:
    # name = graphene.String(description="Name of the administrador.")
    tipo=graphene.Int()
    email=graphene.String()
    nombre=graphene.String()
    estado=graphene.Boolean()
    cookie=graphene.String()
   



class create_administrador_input(graphene.InputObjectType, administrador_attribute):
    """Arguments to create a administrador."""
    pass


class create_administrador(graphene.Mutation):
    """Mutation to create a administrador."""
    administrador = graphene.Field(lambda: administrador_schema, description="administrador created by this mutation.")

    class Arguments:
        input = create_administrador_input(required=True)

    def mutate(self, info, input):
        administrador=mutation_create(administrador_model,'idadministrador')

        return create_administrador(administrador=administrador)


class update_administrador_input(graphene.InputObjectType, administrador_attribute):
    """Arguments to update a administrador."""
    idadministrador = graphene.ID(required=True, description="Global Id of the administrador.")


class update_administrador(graphene.Mutation):
    """Update a administrador."""
    administrador = graphene.Field(lambda: administrador_schema, description="administrador updated by this mutation.")

    class Arguments:
        input = update_administrador_input(required=True)

    def mutate(self, info, input):
        administrador=mutation_update(administrador_model,idadministrador)
        return update_administrador(administrador=administrador)