
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import TABLENAME_model
from ..resolver import resolve
from ..mutator import mutation_create

# __REPLACE__

class TABLENAME_schema(SQLAlchemyObjectType):
    class Meta:
        model = TABLENAME_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idTABLENAME',ONLY_FIELDS]


def resolve_TABLENAME( args, info,idTABLENAME, **kwargs ):
    query= resolve(args,info,TABLENAME_schema,TABLENAME_model,idTABLENAME=idTABLENAME,**kwargs)
    return query.first()

def resolve_all_TABLENAME( args, info, **kwargs):
    query= resolve(args,info,TABLENAME_schema,TABLENAME_model,**kwargs)
    return query



all_TABLENAME = SQLAlchemyConnectionField(TABLENAME_schema,EXTRA_FIELDS)
TABLENAME = graphene.Field(TABLENAME_schema,idTABLENAME=graphene.Int(),EXTRA_FIELDS)

# __REPLACE__