
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import sitemap_model
from ..resolver import resolve
from ..mutator import mutation_create

# __REPLACE__

class sitemap_schema(SQLAlchemyObjectType):
    class Meta:
        model = sitemap_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idsitemap','idpadre','url','depth','valid','ready']


def resolve_sitemap( args, info,idsitemap, **kwargs ):
    query= resolve(args,info,sitemap_schema,sitemap_model,idsitemap=idsitemap,**kwargs)
    return query.first()

def resolve_all_sitemap( args, info, **kwargs):
    query= resolve(args,info,sitemap_schema,sitemap_model,**kwargs)
    return query



all_sitemap = SQLAlchemyConnectionField(sitemap_schema,idpadre=graphene.Int(),url=graphene.String(),depth=graphene.Int(),valid=graphene.String(),ready=graphene.Boolean())
sitemap = graphene.Field(sitemap_schema,idsitemap=graphene.Int(),idpadre=graphene.Int(),url=graphene.String(),depth=graphene.Int(),valid=graphene.String(),ready=graphene.Boolean())

# __REPLACE__



# Create a generic class to mutualize description of sitemap _attributes for both queries and mutations
class sitemap_attribute:
    # name = graphene.String(description="Name of the sitemap.")
    idpadre=graphene.Int()
    url=graphene.String()
    depth=graphene.Int()
    valid=graphene.String()
    ready=graphene.Boolean()
   



class create_sitemap_input(graphene.InputObjectType, sitemap_attribute):
    """Arguments to create a sitemap."""
    pass


class create_sitemap(graphene.Mutation):
    """Mutation to create a sitemap."""
    sitemap = graphene.Field(lambda: sitemap_schema, description="sitemap created by this mutation.")

    class Arguments:
        input = create_sitemap_input(required=True)

    def mutate(self, info, input):
        sitemap=mutation_create(sitemap_model,idsitemap)

        return create_sitemap(sitemap=sitemap)


class update_sitemap_input(graphene.InputObjectType, sitemap_attribute):
    """Arguments to update a sitemap."""
    idsitemap = graphene.ID(required=True, description="Global Id of the sitemap.")


class update_sitemap(graphene.Mutation):
    """Update a sitemap."""
    sitemap = graphene.Field(lambda: sitemap_schema, description="sitemap updated by this mutation.")

    class Arguments:
        input = update_sitemap_input(required=True)

    def mutate(self, info, input):
        sitemap=mutation_update(sitemap_model,idsitemap)
        return update_sitemap(sitemap=sitemap)