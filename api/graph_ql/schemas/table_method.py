
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import table_model
from ..resolver import resolve

# __REPLACE
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

# __REPLACE