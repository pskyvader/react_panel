
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import usuariodireccion_model
from ..resolver import resolve

# __REPLACE
class usuariodireccion_schema(SQLAlchemyObjectType):
    class Meta:
        model = usuariodireccion_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idusuariodireccion','idusuario','tipo','titulo','nombre','direccion','idcomuna','telefono','villa','edificio','departamento','condominio','casa','empresa','referencias']


def resolve_usuariodireccion( args, info,idusuariodireccion, **kwargs ):
    query= resolve(args,info,usuariodireccion_schema,usuariodireccion_model,idusuariodireccion=idusuariodireccion,**kwargs)
    return query.first()

def resolve_all_usuariodireccion( args, info, **kwargs):
    query= resolve(args,info,usuariodireccion_schema,usuariodireccion_model,**kwargs)
    return query



all_usuariodireccion = SQLAlchemyConnectionField(usuariodireccion_schema,idusuario=graphene.Int(),tipo=graphene.Int(),titulo=graphene.String(),nombre=graphene.String(),direccion=graphene.String(),idcomuna=graphene.Int(),telefono=graphene.String(),villa=graphene.String(),edificio=graphene.String(),departamento=graphene.String(),condominio=graphene.String(),casa=graphene.String(),empresa=graphene.String(),referencias=graphene.String())
usuariodireccion = graphene.Field(usuariodireccion_schema,idusuariodireccion=graphene.Int(),idusuario=graphene.Int(),tipo=graphene.Int(),titulo=graphene.String(),nombre=graphene.String(),direccion=graphene.String(),idcomuna=graphene.Int(),telefono=graphene.String(),villa=graphene.String(),edificio=graphene.String(),departamento=graphene.String(),condominio=graphene.String(),casa=graphene.String(),empresa=graphene.String(),referencias=graphene.String())

# __REPLACE