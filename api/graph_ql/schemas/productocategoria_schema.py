from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
import graphene
from ..models import productocategoria_model
from ..resolver import resolve
from ..mutator import mutation_create,mutation_update,mutation_delete



attribute=dict(
    idpadre=graphene.String(),
    tipo=graphene.Int(),
    titulo=graphene.String(),
    url=graphene.String(),
    descuento=graphene.Int(),
    descuento_fecha=graphene.String(),
    resumen=graphene.String(),
    descripcion=graphene.String(),
    keywords=graphene.String(),
    metadescripcion=graphene.String(),
    orden=graphene.Int(),
    estado=graphene.Boolean(),
    destacado=graphene.Boolean()
)
read_only_attribute=dict(
    foto=graphene.JSONString()
)
black_list_attribute=dict(
    
)


class productocategoria_schema(SQLAlchemyObjectType):
    class Meta:
        model = productocategoria_model
        interfaces = (graphene.relay.Node, )
        only_fields=['idproductocategoria']+list(attribute.keys())+list(read_only_attribute.keys())

def resolve_productocategoria( args, info,idproductocategoria, **kwargs ):
    query= resolve(args,info,productocategoria_schema,productocategoria_model,idproductocategoria=idproductocategoria,**kwargs)
    return query.first()

def resolve_all_productocategoria( args, info, **kwargs):
    query= resolve(args,info,productocategoria_schema,productocategoria_model,**kwargs)
    return query

all_productocategoria = SQLAlchemyConnectionField(productocategoria_schema,sort=graphene.String(),**attribute)
productocategoria = graphene.Field(productocategoria_schema,idproductocategoria=graphene.Int(),**attribute)

# Create a generic class to mutualize description of productocategoria _attributes for both queries and mutations
class productocategoria_attribute:
    # name = graphene.String(description="Name of the productocategoria.")
    pass
for name, value in {**attribute , **read_only_attribute,**black_list_attribute}.items():
    setattr(productocategoria_attribute, name, value)

class create_productocategoria_input(graphene.InputObjectType, productocategoria_attribute):
    """Arguments to create a productocategoria."""
    pass

class create_productocategoria(graphene.Mutation):
    """Mutation to create a productocategoria."""
    productocategoria = graphene.Field(lambda: productocategoria_schema, description="productocategoria created by this mutation.")

    class Arguments:
        input = create_productocategoria_input(required=True)

    def mutate(self, info, input):
        productocategoria=mutation_create(productocategoria_model,input,'idproductocategoria')
        return create_productocategoria(productocategoria=productocategoria)

class update_productocategoria_input(graphene.InputObjectType, productocategoria_attribute):
    """Arguments to update a productocategoria."""
    idproductocategoria = graphene.ID(required=True, description="Global Id of the productocategoria.")

class update_productocategoria(graphene.Mutation):
    """Update a productocategoria."""
    productocategoria = graphene.Field(lambda: productocategoria_schema, description="productocategoria updated by this mutation.")

    class Arguments:
        input = update_productocategoria_input(required=True)

    def mutate(self, info, input):
        productocategoria=mutation_update(productocategoria_model,input,'idproductocategoria')
        return update_productocategoria(productocategoria=productocategoria)


class delete_productocategoria_input(graphene.InputObjectType, productocategoria_attribute):
    """Arguments to delete a productocategoria."""
    idproductocategoria = graphene.ID(required=True, description="Global Id of the productocategoria.")

class delete_productocategoria(graphene.Mutation):
    """delete a productocategoria."""
    ok=graphene.Boolean(description="productocategoria deleted correctly.")
    message=graphene.String(description="productocategoria deleted message.")

    class Arguments:
        input = delete_productocategoria_input(required=True)

    def mutate(self, info, input):
        (ok,message)=mutation_delete(productocategoria_model,input,'idproductocategoria')
        return delete_productocategoria(ok=ok,message=message)
