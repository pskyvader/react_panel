
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import galeria_model
from ..resolver import resolve
from ..mutator import mutation_create

# __REPLACE__

class galeria_schema(SQLAlchemyObjectType):
    class Meta:
        model = galeria_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idgaleria','tipo','titulo','url','subtitulo','foto','resumen','keywords','metadescripcion','orden','estado']


def resolve_galeria( args, info,idgaleria, **kwargs ):
    query= resolve(args,info,galeria_schema,galeria_model,idgaleria=idgaleria,**kwargs)
    return query.first()

def resolve_all_galeria( args, info, **kwargs):
    query= resolve(args,info,galeria_schema,galeria_model,**kwargs)
    return query



all_galeria = SQLAlchemyConnectionField(galeria_schema,tipo=graphene.Int(),titulo=graphene.String(),url=graphene.String(),subtitulo=graphene.String(),resumen=graphene.String(),keywords=graphene.String(),metadescripcion=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean())
galeria = graphene.Field(galeria_schema,idgaleria=graphene.Int(),tipo=graphene.Int(),titulo=graphene.String(),url=graphene.String(),subtitulo=graphene.String(),resumen=graphene.String(),keywords=graphene.String(),metadescripcion=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean())

# __REPLACE__



# Create a generic class to mutualize description of galeria _attributes for both queries and mutations
class galeria_attribute:
    # name = graphene.String(description="Name of the galeria.")
    tipo=graphene.Int()
    titulo=graphene.String()
    url=graphene.String()
    subtitulo=graphene.String()
    resumen=graphene.String()
    keywords=graphene.String()
    metadescripcion=graphene.String()
    orden=graphene.Int()
    estado=graphene.Boolean()
   



class create_galeria_input(graphene.InputObjectType, galeria_attribute):
    """Arguments to create a galeria."""
    pass


class create_galeria(graphene.Mutation):
    """Mutation to create a galeria."""
    galeria = graphene.Field(lambda: galeria_schema, description="galeria created by this mutation.")

    class Arguments:
        input = create_galeria_input(required=True)

    def mutate(self, info, input):
        galeria=mutation_create(galeria_model,idgaleria)

        return create_galeria(galeria=galeria)


class update_galeria_input(graphene.InputObjectType, galeria_attribute):
    """Arguments to update a galeria."""
    idgaleria = graphene.ID(required=True, description="Global Id of the galeria.")


class update_galeria(graphene.Mutation):
    """Update a galeria."""
    galeria = graphene.Field(lambda: galeria_schema, description="galeria updated by this mutation.")

    class Arguments:
        input = update_galeria_input(required=True)

    def mutate(self, info, input):
        galeria=mutation_update(galeria_model,idgaleria)
        return update_galeria(galeria=galeria)