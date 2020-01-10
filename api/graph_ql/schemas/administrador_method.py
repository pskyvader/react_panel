
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import administrador_model
from ..resolver import resolve

# __REPLACE
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

# __REPLACE


# Create a generic class to mutualize description of administrador _attributes for both queries and mutations
class administrador_attribute:
    name = graphene.String(description="Name of the administrador.")
    height = graphene.String(description="Height of the administrador.")
    mass = graphene.String(description="Mass of the administrador.")
    hair_color = graphene.String(description="Hair color of the administrador.")
    skin_color = graphene.String(description="Skin color of the administrador.")
    eye_color = graphene.String(description="Eye color of the administrador.")
    birth_year = graphene.String(description="Birth year of the administrador.")
    gender = graphene.String(description="Gender of the administrador.")
    planet_id = graphene.ID(description="Global Id of the planet from which the administrador comes from.")
    url = graphene.String(description="URL of the administrador in the Star Wars API.")



class create_administrador_input(graphene.InputObjectType, administrador_attribute):
    """Arguments to create a administrador."""
    pass


class create_administrador(graphene.Mutation):
    """Mutation to create a administrador."""
    administrador = graphene.Field(lambda: administrador_schema, description="administrador created by this mutation.")

    class Arguments:
        input = create_administrador_input(required=True)

    def mutate(self, info, input):
        administrador=mutation_create()

        return create_administrador(administrador=administrador)


class update_administrador_input(graphene.InputObjectType, administrador_attribute):
    """Arguments to update a administrador."""
    id = graphene.ID(required=True, description="Global Id of the administrador.")


class update_administrador(graphene.Mutation):
    """Update a administrador."""
    administrador = graphene.Field(lambda: administrador, description="administrador updated by this mutation.")

    class Arguments:
        input = update_administrador_input(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        administrador = db_session.query(administrador_model).filter_by(id=data['id'])
        administrador.update(data)
        db_session.commit()
        administrador = db_session.query(administrador_model).filter_by(id=data['id']).first()

        return update_administrador(administrador=administrador)