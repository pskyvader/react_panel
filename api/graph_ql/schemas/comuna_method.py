
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import comuna_model
from ..resolver import resolve

# __REPLACE
class comuna_schema(SQLAlchemyObjectType):
    class Meta:
        model = comuna_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idcomuna','idregion','titulo','precio','orden','estado']


def resolve_comuna( args, info,idcomuna, **kwargs ):
    query= resolve(args,info,comuna_schema,comuna_model,idcomuna=idcomuna,**kwargs)
    return query.first()

def resolve_all_comuna( args, info, **kwargs):
    query= resolve(args,info,comuna_schema,comuna_model,**kwargs)
    return query



all_comuna = SQLAlchemyConnectionField(comuna_schema,idregion=graphene.Int(),titulo=graphene.String(),precio=graphene.Int(),orden=graphene.Int(),estado=graphene.Boolean())
comuna = graphene.Field(comuna_schema,idcomuna=graphene.Int(),idregion=graphene.Int(),titulo=graphene.String(),precio=graphene.Int(),orden=graphene.Int(),estado=graphene.Boolean())

# __REPLACE