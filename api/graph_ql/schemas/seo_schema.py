from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import seo_model
from ..resolver import resolve
from ..mutator import mutation_create, mutation_update, mutation_delete
from .image_schema import all_image,resolve_all_image

attribute = dict(
    titulo=graphene.String(),
url=graphene.String(),
subtitulo=graphene.String(),
modulo_front=graphene.String(),
modulo_back=graphene.String(),
tipo_modulo=graphene.Int(),
link_menu=graphene.String(),
keywords=graphene.String(),
metadescripcion=graphene.String(),
orden=graphene.Int(),
menu=graphene.Boolean(),
submenu=graphene.Boolean(),
estado=graphene.Boolean()
    )
read_only_attribute = dict(
    
    )
black_list_attribute = dict(
    
    )


class seo_schema(SQLAlchemyObjectType):
    class Meta:
        model = seo_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idseo"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )
    
    
    foto=all_image
    def resolve_foto(self,info, **kwargs):
        return resolve_all_image(self,info,table_name='seo',idparent=self.idseo,field_name='foto',**kwargs)

    banner=all_image
    def resolve_banner(self,info, **kwargs):
        return resolve_all_image(self,info,table_name='seo',idparent=self.idseo,field_name='banner',**kwargs)



def resolve_seo(args, info, idseo, **kwargs):
    query = resolve(
        args, info, seo_schema, seo_model, idseo=idseo, **kwargs
    )
    return query.first()


def resolve_all_seo(args, info, **kwargs):
    query = resolve(args, info, seo_schema, seo_model, **kwargs)
    return query


all_seo = SQLAlchemyConnectionField( seo_schema, sort=graphene.String(), **attribute )
seo = graphene.Field(seo_schema, idseo=graphene.Int(), **attribute)

# Create a generic class to mutualize description of seo _attributes for both queries and mutations
class seo_attribute:
    # name = graphene.String(description="Name of the seo.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(seo_attribute, name, value)


class create_seo_input(graphene.InputObjectType, seo_attribute):
    """Arguments to create a seo."""

    pass


class create_seo(graphene.Mutation):
    """Mutation to create a seo."""

    seo = graphene.Field(
        seo_schema, description="seo created by this mutation."
    )

    class Arguments:
        input = create_seo_input(required=True)

    def mutate(self, info, input):
        seo = mutation_create(seo_model, input, "idseo",info)
        return create_seo(seo=seo)


class update_seo_input(graphene.InputObjectType, seo_attribute):
    """Arguments to update a seo."""

    idseo = graphene.ID(required=True, description="Global Id of the seo.")


class update_seo(graphene.Mutation):
    """Update a seo."""

    seo = graphene.Field(
        seo_schema, description="seo updated by this mutation."
    )

    class Arguments:
        input = update_seo_input(required=True)

    def mutate(self, info, input):
        seo = mutation_update(seo_model, input, "idseo",info)
        return update_seo(seo=seo)


class delete_seo_input(graphene.InputObjectType, seo_attribute):
    """Arguments to delete a seo."""

    idseo = graphene.ID(required=True, description="Global Id of the seo.")


class delete_seo(graphene.Mutation):
    """delete a seo."""

    ok = graphene.Boolean(description="seo deleted correctly.")
    message = graphene.String(description="seo deleted message.")

    class Arguments:
        input = delete_seo_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(seo_model, input, "idseo")
        return delete_seo(ok=ok, message=message)
