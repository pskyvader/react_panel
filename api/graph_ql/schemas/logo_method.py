
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import logo_model
from ..resolver import resolve

# __REPLACE
class logo_schema(SQLAlchemyObjectType):
    class Meta:
        model = logo_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idlogo','titulo','foto','orden']


def resolve_logo( args, info,idlogo, **kwargs ):
    query= resolve(args,info,logo_schema,logo_model,idlogo=idlogo,**kwargs)
    return query.first()

def resolve_all_logo( args, info, **kwargs):
    query= resolve(args,info,logo_schema,logo_model,**kwargs)
    return query



all_logo = SQLAlchemyConnectionField(logo_schema,titulo=graphene.String(),orden=graphene.Int())
logo = graphene.Field(logo_schema,idlogo=graphene.Int(),titulo=graphene.String(),orden=graphene.Int())

# __REPLACE