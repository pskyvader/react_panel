
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import table_model
from ..resolver import resolve
from ..mutator import mutation_create,mutation_update

# __REPLACE__

class table_schema(SQLAlchemyObjectType):
    class Meta:
        model = table_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idtable','tablename','idname','fields','truncate']


def resolve_table( args, info,idtable, **kwargs ):
    query= resolve(args,info,table_schema,table_model,idtable=idtable,**kwargs)
    return query.first()

def resolve_all_table( args, info, **kwargs):
    query= resolve(args,info,table_schema,table_model,**kwargs)
    return query



all_table = SQLAlchemyConnectionField(table_schema,tablename=graphene.String(),idname=graphene.String(),fields=graphene.String(),truncate=graphene.Boolean())
table = graphene.Field(table_schema,idtable=graphene.Int(),tablename=graphene.String(),idname=graphene.String(),fields=graphene.String(),truncate=graphene.Boolean())

# __REPLACE__



# Create a generic class to mutualize description of table _attributes for both queries and mutations
class table_attribute:
    # name = graphene.String(description="Name of the table.")
    tablename=graphene.String()
    idname=graphene.String()
    fields=graphene.String()
    truncate=graphene.Boolean()
   



class create_table_input(graphene.InputObjectType, table_attribute):
    """Arguments to create a table."""
    pass


class create_table(graphene.Mutation):
    """Mutation to create a table."""
    table = graphene.Field(lambda: table_schema, description="table created by this mutation.")

    class Arguments:
        input = create_table_input(required=True)

    def mutate(self, info, input):
        table=mutation_create(table_model,input,'idtable')

        return create_table(table=table)


class update_table_input(graphene.InputObjectType, table_attribute):
    """Arguments to update a table."""
    idtable = graphene.ID(required=True, description="Global Id of the table.")


class update_table(graphene.Mutation):
    """Update a table."""
    table = graphene.Field(lambda: table_schema, description="table updated by this mutation.")

    class Arguments:
        input = update_table_input(required=True)

    def mutate(self, info, input):
        table=mutation_update(table_model,input,'idtable')
        return update_table(table=table)