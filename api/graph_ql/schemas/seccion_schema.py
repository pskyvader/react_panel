
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import seccion_model
from ..resolver import resolve
from ..mutator import mutation_create,mutation_update

# __REPLACE__

class seccion_schema(SQLAlchemyObjectType):
    class Meta:
        model = seccion_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idseccion','idseccioncategoria','tipo','titulo','subtitulo','url','foto','archivo','resumen','descripcion','keywords','metadescripcion','orden','estado','destacado']


def resolve_seccion( args, info,idseccion, **kwargs ):
    query= resolve(args,info,seccion_schema,seccion_model,idseccion=idseccion,**kwargs)
    return query.first()

def resolve_all_seccion( args, info, **kwargs):
    query= resolve(args,info,seccion_schema,seccion_model,**kwargs)
    return query



all_seccion = SQLAlchemyConnectionField(seccion_schema,idseccioncategoria=graphene.String(),tipo=graphene.Int(),titulo=graphene.String(),subtitulo=graphene.String(),url=graphene.String(),resumen=graphene.String(),descripcion=graphene.String(),keywords=graphene.String(),metadescripcion=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean(),destacado=graphene.Boolean())
seccion = graphene.Field(seccion_schema,idseccion=graphene.Int(),idseccioncategoria=graphene.String(),tipo=graphene.Int(),titulo=graphene.String(),subtitulo=graphene.String(),url=graphene.String(),resumen=graphene.String(),descripcion=graphene.String(),keywords=graphene.String(),metadescripcion=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean(),destacado=graphene.Boolean())

# __REPLACE__



# Create a generic class to mutualize description of seccion _attributes for both queries and mutations
class seccion_attribute:
    # name = graphene.String(description="Name of the seccion.")
    idseccioncategoria=graphene.String()
    tipo=graphene.Int()
    titulo=graphene.String()
    subtitulo=graphene.String()
    url=graphene.String()
    resumen=graphene.String()
    descripcion=graphene.String()
    keywords=graphene.String()
    metadescripcion=graphene.String()
    orden=graphene.Int()
    estado=graphene.Boolean()
    destacado=graphene.Boolean()
   



class create_seccion_input(graphene.InputObjectType, seccion_attribute):
    """Arguments to create a seccion."""
    pass


class create_seccion(graphene.Mutation):
    """Mutation to create a seccion."""
    seccion = graphene.Field(lambda: seccion_schema, description="seccion created by this mutation.")

    class Arguments:
        input = create_seccion_input(required=True)

    def mutate(self, info, input):
        seccion=mutation_create(seccion_model,input,'idseccion')

        return create_seccion(seccion=seccion)


class update_seccion_input(graphene.InputObjectType, seccion_attribute):
    """Arguments to update a seccion."""
    idseccion = graphene.ID(required=True, description="Global Id of the seccion.")


class update_seccion(graphene.Mutation):
    """Update a seccion."""
    seccion = graphene.Field(lambda: seccion_schema, description="seccion updated by this mutation.")

    class Arguments:
        input = update_seccion_input(required=True)

    def mutate(self, info, input):
        seccion=mutation_update(seccion_model,input,'idseccion')
        return update_seccion(seccion=seccion)