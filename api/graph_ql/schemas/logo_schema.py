
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import logo_model
from ..resolver import resolve
from ..mutator import mutation_create

# __REPLACE__

class logo_schema(SQLAlchemyObjectType):
    class Meta:
        model = logo_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idlogo','titulo','foto','orden']


def resolve_logo( args, info,idlogo, **kwargs ):
    query= resolve(args,info,logo_schema,logo_model,idlogo=idlogo,**kwargs)
    return query.first()

def resolve_all_logo( args, info, **kwargs):
    query= resolve(args,info,logo_schema,logo_model,**kwargs)
    return query



all_logo = SQLAlchemyConnectionField(logo_schema,titulo=graphene.String(),orden=graphene.Int())
logo = graphene.Field(logo_schema,idlogo=graphene.Int(),titulo=graphene.String(),orden=graphene.Int())

# __REPLACE__



# Create a generic class to mutualize description of logo _attributes for both queries and mutations
class logo_attribute:
    # name = graphene.String(description="Name of the logo.")
    titulo=graphene.String()
    orden=graphene.Int()
   



class create_logo_input(graphene.InputObjectType, logo_attribute):
    """Arguments to create a logo."""
    pass


class create_logo(graphene.Mutation):
    """Mutation to create a logo."""
    logo = graphene.Field(lambda: logo_schema, description="logo created by this mutation.")

    class Arguments:
        input = create_logo_input(required=True)

    def mutate(self, info, input):
        logo=mutation_create(logo_model,idlogo)

        return create_logo(logo=logo)


class update_logo_input(graphene.InputObjectType, logo_attribute):
    """Arguments to update a logo."""
    idlogo = graphene.ID(required=True, description="Global Id of the logo.")


class update_logo(graphene.Mutation):
    """Update a logo."""
    logo = graphene.Field(lambda: logo_schema, description="logo updated by this mutation.")

    class Arguments:
        input = update_logo_input(required=True)

    def mutate(self, info, input):
        logo=mutation_update(logo_model,idlogo)
        return update_logo(logo=logo)