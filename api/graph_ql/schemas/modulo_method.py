
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import modulo_model
from ..resolver import resolve

# __REPLACE
class modulo_schema(SQLAlchemyObjectType):
    class Meta:
        model = modulo_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idmodulo','idmoduloconfiguracion','tipo','titulo','menu','mostrar','detalle','recortes','orden','estado','aside','hijos']


def resolve_modulo( args, info,idmodulo, **kwargs ):
    query= resolve(args,info,modulo_schema,modulo_model,idmodulo=idmodulo,**kwargs)
    return query.first()

def resolve_all_modulo( args, info, **kwargs):
    query= resolve(args,info,modulo_schema,modulo_model,**kwargs)
    return query



all_modulo = SQLAlchemyConnectionField(modulo_schema,idmoduloconfiguracion=graphene.Int(),tipo=graphene.Int(),titulo=graphene.String(),menu=graphene.String(),mostrar=graphene.String(),detalle=graphene.String(),recortes=graphene.String(),orden=graphene.Int(),estado=graphene.String(),aside=graphene.Boolean(),hijos=graphene.Boolean())
modulo = graphene.Field(modulo_schema,idmodulo=graphene.Int(),idmoduloconfiguracion=graphene.Int(),tipo=graphene.Int(),titulo=graphene.String(),menu=graphene.String(),mostrar=graphene.String(),detalle=graphene.String(),recortes=graphene.String(),orden=graphene.Int(),estado=graphene.String(),aside=graphene.Boolean(),hijos=graphene.Boolean())

# __REPLACE