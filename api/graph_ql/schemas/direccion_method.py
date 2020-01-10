
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import direccion_model
from ..resolver import resolve

# __REPLACE
class direccion_schema(SQLAlchemyObjectType):
    class Meta:
        model = direccion_model
        interfaces = (graphene.relay.Node, )
        only_fields=['iddireccion','idusuario','tipo','titulo','nombre','direccion','idcomuna','telefono','villa','edificio','departamento','condominio','casa','empresa','referencias']


def resolve_direccion( args, info,iddireccion, **kwargs ):
    query= resolve(args,info,direccion_schema,direccion_model,iddireccion=iddireccion,**kwargs)
    return query.first()

def resolve_all_direccion( args, info, **kwargs):
    query= resolve(args,info,direccion_schema,direccion_model,**kwargs)
    return query



all_direccion = SQLAlchemyConnectionField(direccion_schema,idusuario=graphene.Int(),tipo=graphene.Int(),titulo=graphene.String(),nombre=graphene.String(),direccion=graphene.String(),idcomuna=graphene.Int(),telefono=graphene.String(),villa=graphene.String(),edificio=graphene.String(),departamento=graphene.String(),condominio=graphene.String(),casa=graphene.String(),empresa=graphene.String(),referencias=graphene.String())
direccion = graphene.Field(direccion_schema,iddireccion=graphene.Int(),idusuario=graphene.Int(),tipo=graphene.Int(),titulo=graphene.String(),nombre=graphene.String(),direccion=graphene.String(),idcomuna=graphene.Int(),telefono=graphene.String(),villa=graphene.String(),edificio=graphene.String(),departamento=graphene.String(),condominio=graphene.String(),casa=graphene.String(),empresa=graphene.String(),referencias=graphene.String())

# __REPLACE