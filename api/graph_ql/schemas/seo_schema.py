
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import seo_model
from ..resolver import resolve
from ..mutator import mutation_create,mutation_update

# __REPLACE__

class seo_schema(SQLAlchemyObjectType):
    class Meta:
        model = seo_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idseo','titulo','url','subtitulo','foto','banner','modulo_front','modulo_back','tipo_modulo','link_menu','keywords','metadescripcion','orden','menu','submenu','estado']


def resolve_seo( args, info,idseo, **kwargs ):
    query= resolve(args,info,seo_schema,seo_model,idseo=idseo,**kwargs)
    return query.first()

def resolve_all_seo( args, info, **kwargs):
    query= resolve(args,info,seo_schema,seo_model,**kwargs)
    return query



all_seo = SQLAlchemyConnectionField(seo_schema,titulo=graphene.String(),url=graphene.String(),subtitulo=graphene.String(),modulo_front=graphene.String(),modulo_back=graphene.String(),tipo_modulo=graphene.Int(),link_menu=graphene.String(),keywords=graphene.String(),metadescripcion=graphene.String(),orden=graphene.Int(),menu=graphene.Boolean(),submenu=graphene.Boolean(),estado=graphene.Boolean())
seo = graphene.Field(seo_schema,idseo=graphene.Int(),titulo=graphene.String(),url=graphene.String(),subtitulo=graphene.String(),modulo_front=graphene.String(),modulo_back=graphene.String(),tipo_modulo=graphene.Int(),link_menu=graphene.String(),keywords=graphene.String(),metadescripcion=graphene.String(),orden=graphene.Int(),menu=graphene.Boolean(),submenu=graphene.Boolean(),estado=graphene.Boolean())

# __REPLACE__



# Create a generic class to mutualize description of seo _attributes for both queries and mutations
class seo_attribute:
    # name = graphene.String(description="Name of the seo.")
    titulo=graphene.String()
    url=graphene.String()
    subtitulo=graphene.String()
    modulo_front=graphene.String()
    modulo_back=graphene.String()
    tipo_modulo=graphene.Int()
    link_menu=graphene.String()
    keywords=graphene.String()
    metadescripcion=graphene.String()
    orden=graphene.Int()
    menu=graphene.Boolean()
    submenu=graphene.Boolean()
    estado=graphene.Boolean()
   



class create_seo_input(graphene.InputObjectType, seo_attribute):
    """Arguments to create a seo."""
    pass


class create_seo(graphene.Mutation):
    """Mutation to create a seo."""
    seo = graphene.Field(lambda: seo_schema, description="seo created by this mutation.")

    class Arguments:
        input = create_seo_input(required=True)

    def mutate(self, info, input):
        seo=mutation_create(seo_model,input,'idseo')

        return create_seo(seo=seo)


class update_seo_input(graphene.InputObjectType, seo_attribute):
    """Arguments to update a seo."""
    idseo = graphene.ID(required=True, description="Global Id of the seo.")


class update_seo(graphene.Mutation):
    """Update a seo."""
    seo = graphene.Field(lambda: seo_schema, description="seo updated by this mutation.")

    class Arguments:
        input = update_seo_input(required=True)

    def mutate(self, info, input):
        seo=mutation_update(seo_model,input,'idseo')
        return update_seo(seo=seo)