from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import sitemap_model
from ..resolver import resolve,Url
from ..mutator import mutation_create, mutation_update, mutation_delete


attribute = dict(
    idpadre=graphene.Int(),
    url=graphene.String(),
    depth=graphene.Int(),
    valid=graphene.String(),
    ready=graphene.Boolean()
    )
read_only_attribute = dict(
    
    )
black_list_attribute = dict(
    
    )


class sitemap_schema(SQLAlchemyObjectType):
    class Meta:
        model = sitemap_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idsitemap"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )
    
    


def resolve_sitemap(args, info, idsitemap, **kwargs):
    query = resolve(
        args, info, sitemap_schema, sitemap_model, idsitemap=idsitemap, **kwargs
    )
    return query.first()


def resolve_all_sitemap(args, info, **kwargs):
    query = resolve(args, info, sitemap_schema, sitemap_model, **kwargs)
    return query


all_sitemap = SQLAlchemyConnectionField( sitemap_schema, sort=graphene.String() , **attribute )
sitemap = graphene.Field(sitemap_schema, idsitemap=graphene.Int() , **attribute)

# Create a generic class to mutualize description of sitemap _attributes for both queries and mutations
class sitemap_attribute:
    # name = graphene.String(description="Name of the sitemap.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(sitemap_attribute, name, value)


class create_sitemap_input(graphene.InputObjectType, sitemap_attribute):
    """Arguments to create a sitemap."""

    pass


class create_sitemap(graphene.Mutation):
    """Mutation to create a sitemap."""

    sitemap = graphene.Field(
        sitemap_schema, description="sitemap created by this mutation."
    )

    class Arguments:
        input = create_sitemap_input(required=True)

    def mutate(self, info, input):
        sitemap = mutation_create(sitemap_model, input, "idsitemap",info)
        return create_sitemap(sitemap=sitemap)


class update_sitemap_input(graphene.InputObjectType, sitemap_attribute):
    """Arguments to update a sitemap."""

    idsitemap = graphene.ID(required=True, description="Global Id of the sitemap.")


class update_sitemap(graphene.Mutation):
    """Update a sitemap."""

    sitemap = graphene.Field(
        sitemap_schema, description="sitemap updated by this mutation."
    )

    class Arguments:
        input = update_sitemap_input(required=True)

    def mutate(self, info, input):
        sitemap = mutation_update(sitemap_model, input, "idsitemap",info)
        return update_sitemap(sitemap=sitemap)


class delete_sitemap_input(graphene.InputObjectType, sitemap_attribute):
    """Arguments to delete a sitemap."""

    idsitemap = graphene.ID(required=True, description="Global Id of the sitemap.")


class delete_sitemap(graphene.Mutation):
    """delete a sitemap."""

    ok = graphene.Boolean(description="sitemap deleted correctly.")
    message = graphene.String(description="sitemap deleted message.")

    class Arguments:
        input = delete_sitemap_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(sitemap_model, input, "idsitemap")
        return delete_sitemap(ok=ok, message=message)
