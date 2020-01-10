
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import igtotal_model
from ..resolver import resolve

# __REPLACE
class igtotal_schema(SQLAlchemyObjectType):
    class Meta:
        model = igtotal_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idigtotal','tag','fecha','cantidad']


def resolve_igtotal( args, info,idigtotal, **kwargs ):
    query= resolve(args,info,igtotal_schema,igtotal_model,idigtotal=idigtotal,**kwargs)
    return query.first()

def resolve_all_igtotal( args, info, **kwargs):
    query= resolve(args,info,igtotal_schema,igtotal_model,**kwargs)
    return query



all_igtotal = SQLAlchemyConnectionField(igtotal_schema,tag=graphene.String(),fecha=graphene.types.datetime.DateTime(),cantidad=graphene.Int())
igtotal = graphene.Field(igtotal_schema,idigtotal=graphene.Int(),tag=graphene.String(),fecha=graphene.types.datetime.DateTime(),cantidad=graphene.Int())

# __REPLACE