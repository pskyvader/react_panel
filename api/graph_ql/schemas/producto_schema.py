
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import producto_model
from ..resolver import resolve
from ..mutator import mutation_create,mutation_update

# __REPLACE__

class producto_schema(SQLAlchemyObjectType):
    class Meta:
        model = producto_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idproducto','idproductocategoria','tipo','titulo','url','foto','archivo','codigo','precio','descuento','descuento_fecha','stock','ventas','resumen','descripcion','keywords','metadescripcion','orden','estado','destacado']


def resolve_producto( args, info,idproducto, **kwargs ):
    query= resolve(args,info,producto_schema,producto_model,idproducto=idproducto,**kwargs)
    return query.first()

def resolve_all_producto( args, info, **kwargs):
    query= resolve(args,info,producto_schema,producto_model,**kwargs)
    return query



all_producto = SQLAlchemyConnectionField(producto_schema,idproductocategoria=graphene.String(),tipo=graphene.Int(),titulo=graphene.String(),url=graphene.String(),codigo=graphene.String(),precio=graphene.Int(),descuento=graphene.Int(),descuento_fecha=graphene.String(),stock=graphene.Int(),ventas=graphene.Int(),resumen=graphene.String(),descripcion=graphene.String(),keywords=graphene.String(),metadescripcion=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean(),destacado=graphene.Boolean())
producto = graphene.Field(producto_schema,idproducto=graphene.Int(),idproductocategoria=graphene.String(),tipo=graphene.Int(),titulo=graphene.String(),url=graphene.String(),codigo=graphene.String(),precio=graphene.Int(),descuento=graphene.Int(),descuento_fecha=graphene.String(),stock=graphene.Int(),ventas=graphene.Int(),resumen=graphene.String(),descripcion=graphene.String(),keywords=graphene.String(),metadescripcion=graphene.String(),orden=graphene.Int(),estado=graphene.Boolean(),destacado=graphene.Boolean())

# __REPLACE__



# Create a generic class to mutualize description of producto _attributes for both queries and mutations
class producto_attribute:
    # name = graphene.String(description="Name of the producto.")
    idproductocategoria=graphene.String()
    tipo=graphene.Int()
    titulo=graphene.String()
    url=graphene.String()
    codigo=graphene.String()
    precio=graphene.Int()
    descuento=graphene.Int()
    descuento_fecha=graphene.String()
    stock=graphene.Int()
    ventas=graphene.Int()
    resumen=graphene.String()
    descripcion=graphene.String()
    keywords=graphene.String()
    metadescripcion=graphene.String()
    orden=graphene.Int()
    estado=graphene.Boolean()
    destacado=graphene.Boolean()
   



class create_producto_input(graphene.InputObjectType, producto_attribute):
    """Arguments to create a producto."""
    pass


class create_producto(graphene.Mutation):
    """Mutation to create a producto."""
    producto = graphene.Field(lambda: producto_schema, description="producto created by this mutation.")

    class Arguments:
        input = create_producto_input(required=True)

    def mutate(self, info, input):
        producto=mutation_create(producto_model,input,'idproducto')

        return create_producto(producto=producto)


class update_producto_input(graphene.InputObjectType, producto_attribute):
    """Arguments to update a producto."""
    idproducto = graphene.ID(required=True, description="Global Id of the producto.")


class update_producto(graphene.Mutation):
    """Update a producto."""
    producto = graphene.Field(lambda: producto_schema, description="producto updated by this mutation.")

    class Arguments:
        input = update_producto_input(required=True)

    def mutate(self, info, input):
        producto=mutation_update(producto_model,input,'idproducto')
        return update_producto(producto=producto)