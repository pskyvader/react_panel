
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import seccioncategoria_model
from ..resolver import resolve
from ..mutator import mutation_create,mutation_update

class seccioncategoria_schema(SQLAlchemyObjectType):
    class Meta:
        model = seccioncategoria_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idseccioncategoria','idpadre','tipo','titulo','url','foto','resumen','descripcion','keywords','metadescripcion','orden','estado','destacado']

def resolve_seccioncategoria( args, info,idseccioncategoria, **kwargs ):
    query= resolve(args,info,seccioncategoria_schema,seccioncategoria_model,idseccioncategoria=idseccioncategoria,**kwargs)
    return query.first()

def resolve_all_seccioncategoria( args, info, **kwargs):
    query= resolve(args,info,seccioncategoria_schema,seccioncategoria_model,**kwargs)
    return query

all_seccioncategoria = SQLAlchemyConnectionField(seccioncategoria_schema,sort=graphene.String(),idpadre=graphene.String(),tipo=graphene.Int(),titulo=graphene.String(),url=graphene.String(),resumen=graphene.String(),descripcion=graphene.String(),keywords=graphene.String(),metadescripcion=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean(),destacado=graphene.Boolean())
seccioncategoria = graphene.Field(seccioncategoria_schema,idseccioncategoria=graphene.Int(),idpadre=graphene.String(),tipo=graphene.Int(),titulo=graphene.String(),url=graphene.String(),resumen=graphene.String(),descripcion=graphene.String(),keywords=graphene.String(),metadescripcion=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean(),destacado=graphene.Boolean())

# Create a generic class to mutualize description of seccioncategoria _attributes for both queries and mutations
class seccioncategoria_attribute:
    # name = graphene.String(description="Name of the seccioncategoria.")
    idpadre=graphene.String()
    tipo=graphene.Int()
    titulo=graphene.String()
    url=graphene.String()
    resumen=graphene.String()
    descripcion=graphene.String()
    keywords=graphene.String()
    metadescripcion=graphene.String()
    orden=graphene.Int()
    estado=graphene.Boolean()
    destacado=graphene.Boolean()
   

class create_seccioncategoria_input(graphene.InputObjectType, seccioncategoria_attribute):
    """Arguments to create a seccioncategoria."""
    pass

class create_seccioncategoria(graphene.Mutation):
    """Mutation to create a seccioncategoria."""
    seccioncategoria = graphene.Field(lambda: seccioncategoria_schema, description="seccioncategoria created by this mutation.")

    class Arguments:
        input = create_seccioncategoria_input(required=True)

    def mutate(self, info, input):
        seccioncategoria=mutation_create(seccioncategoria_model,input,'idseccioncategoria')
        return create_seccioncategoria(seccioncategoria=seccioncategoria)

class update_seccioncategoria_input(graphene.InputObjectType, seccioncategoria_attribute):
    """Arguments to update a seccioncategoria."""
    idseccioncategoria = graphene.ID(required=True, description="Global Id of the seccioncategoria.")

class update_seccioncategoria(graphene.Mutation):
    """Update a seccioncategoria."""
    seccioncategoria = graphene.Field(lambda: seccioncategoria_schema, description="seccioncategoria updated by this mutation.")

    class Arguments:
        input = update_seccioncategoria_input(required=True)

    def mutate(self, info, input):
        seccioncategoria=mutation_update(seccioncategoria_model,input,'idseccioncategoria')
        return update_seccioncategoria(seccioncategoria=seccioncategoria)