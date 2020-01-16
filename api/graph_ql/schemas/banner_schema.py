
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import banner_model
from ..resolver import resolve
from ..mutator import mutation_create,mutation_update

# __REPLACE__

class banner_schema(SQLAlchemyObjectType):
    class Meta:
        model = banner_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idbanner','tipo','titulo','texto1','texto2','texto3','texto','link','foto','orden','estado']


def resolve_banner( args, info,idbanner, **kwargs ):
    query= resolve(args,info,banner_schema,banner_model,idbanner=idbanner,**kwargs)
    return query.first()

def resolve_all_banner( args, info, **kwargs):
    query= resolve(args,info,banner_schema,banner_model,**kwargs)
    return query



all_banner = SQLAlchemyConnectionField(banner_schema,tipo=graphene.Int(),titulo=graphene.String(),texto1=graphene.String(),texto2=graphene.String(),texto3=graphene.String(),texto=graphene.String(),link=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean())
banner = graphene.Field(banner_schema,idbanner=graphene.Int(),tipo=graphene.Int(),titulo=graphene.String(),texto1=graphene.String(),texto2=graphene.String(),texto3=graphene.String(),texto=graphene.String(),link=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean())

# __REPLACE__



# Create a generic class to mutualize description of banner _attributes for both queries and mutations
class banner_attribute:
    # name = graphene.String(description="Name of the banner.")
    tipo=graphene.Int()
    titulo=graphene.String()
    texto1=graphene.String()
    texto2=graphene.String()
    texto3=graphene.String()
    texto=graphene.String()
    link=graphene.String()
    orden=graphene.Int()
    estado=graphene.Boolean()
   



class create_banner_input(graphene.InputObjectType, banner_attribute):
    """Arguments to create a banner."""
    pass


class create_banner(graphene.Mutation):
    """Mutation to create a banner."""
    banner = graphene.Field(lambda: banner_schema, description="banner created by this mutation.")

    class Arguments:
        input = create_banner_input(required=True)

    def mutate(self, info, input):
        banner=mutation_create(banner_model,input,'idbanner')

        return create_banner(banner=banner)


class update_banner_input(graphene.InputObjectType, banner_attribute):
    """Arguments to update a banner."""
    idbanner = graphene.ID(required=True, description="Global Id of the banner.")


class update_banner(graphene.Mutation):
    """Update a banner."""
    banner = graphene.Field(lambda: banner_schema, description="banner updated by this mutation.")

    class Arguments:
        input = update_banner_input(required=True)

    def mutate(self, info, input):
        banner=mutation_update(banner_model,input,'idbanner')
        return update_banner(banner=banner)