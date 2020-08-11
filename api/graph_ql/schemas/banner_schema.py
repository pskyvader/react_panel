from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import banner_model
from ..resolver import resolve
from ..mutator import mutation_create, mutation_update, mutation_delete
from .image_schema import all_image,resolve_all_image

attribute = dict(
    tipo=graphene.Int(),
titulo=graphene.String(),
texto1=graphene.String(),
texto2=graphene.String(),
texto3=graphene.String(),
texto=graphene.String(),
link=graphene.String(),
orden=graphene.Int(),
estado=graphene.Boolean()
    )
read_only_attribute = dict(
    
    )
black_list_attribute = dict(
    
    )


class banner_schema(SQLAlchemyObjectType):
    class Meta:
        model = banner_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idbanner"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )
    
    
    foto=all_image
    def resolve_foto(self,info, **kwargs):
        return resolve_all_image(self,info,table_name='banner',idparent=self.idbanner,field_name='foto',**kwargs)



def resolve_banner(args, info, idbanner, **kwargs):
    query = resolve(
        args, info, banner_schema, banner_model, idbanner=idbanner, **kwargs
    )
    return query.first()


def resolve_all_banner(args, info, **kwargs):
    query = resolve(args, info, banner_schema, banner_model, **kwargs)
    return query


all_banner = SQLAlchemyConnectionField( banner_schema, sort=graphene.String(), **attribute )
banner = graphene.Field(banner_schema, idbanner=graphene.Int(), **attribute)

# Create a generic class to mutualize description of banner _attributes for both queries and mutations
class banner_attribute:
    # name = graphene.String(description="Name of the banner.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(banner_attribute, name, value)


class create_banner_input(graphene.InputObjectType, banner_attribute):
    """Arguments to create a banner."""

    pass


class create_banner(graphene.Mutation):
    """Mutation to create a banner."""

    banner = graphene.Field(
        banner_schema, description="banner created by this mutation."
    )

    class Arguments:
        input = create_banner_input(required=True)

    def mutate(self, info, input):
        banner = mutation_create(banner_model, input, "idbanner",info)
        return create_banner(banner=banner)


class update_banner_input(graphene.InputObjectType, banner_attribute):
    """Arguments to update a banner."""

    idbanner = graphene.ID(required=True, description="Global Id of the banner.")


class update_banner(graphene.Mutation):
    """Update a banner."""

    banner = graphene.Field(
        banner_schema, description="banner updated by this mutation."
    )

    class Arguments:
        input = update_banner_input(required=True)

    def mutate(self, info, input):
        banner = mutation_update(banner_model, input, "idbanner",info)
        return update_banner(banner=banner)


class delete_banner_input(graphene.InputObjectType, banner_attribute):
    """Arguments to delete a banner."""

    idbanner = graphene.ID(required=True, description="Global Id of the banner.")


class delete_banner(graphene.Mutation):
    """delete a banner."""

    ok = graphene.Boolean(description="banner deleted correctly.")
    message = graphene.String(description="banner deleted message.")

    class Arguments:
        input = delete_banner_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(banner_model, input, "idbanner")
        return delete_banner(ok=ok, message=message)
