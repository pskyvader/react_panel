from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import producto_model
from ..resolver import resolve
from ..mutator import mutation_create, mutation_update, mutation_delete
from .. import url_object


attribute = dict(
    idproductocategoria=graphene.String(),
    tipo=graphene.Int(),
    titulo=graphene.String(),
    url=graphene.String(),
    codigo=graphene.String(),
    precio=graphene.Int(),
    descuento=graphene.Int(),
    descuento_fecha=graphene.String(),
    stock=graphene.Int(),
    ventas=graphene.Int(),
    resumen=graphene.String(),
    descripcion=graphene.String(),
    keywords=graphene.String(),
    metadescripcion=graphene.String(),
    orden=graphene.Int(),
    estado=graphene.Boolean(),
    destacado=graphene.Boolean()
    )
read_only_attribute = dict(
    foto=graphene.JSONString(),
    archivo=graphene.JSONString()
    )
black_list_attribute = dict(
    
    )


class producto_schema(SQLAlchemyObjectType):
    class Meta:
        model = producto_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idproducto"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )
    
    


def resolve_producto(args, info, idproducto, **kwargs):
    query = resolve(
        args, info, producto_schema, producto_model, idproducto=idproducto, **kwargs
    )
    return query.first()


def resolve_all_producto(args, info, **kwargs):
    query = resolve(args, info, producto_schema, producto_model, **kwargs)
    return query


all_producto = SQLAlchemyConnectionField( producto_schema, sort=graphene.String(), **attribute )
producto = graphene.Field(producto_schema, idproducto=graphene.Int(), **attribute)

# Create a generic class to mutualize description of producto _attributes for both queries and mutations
class producto_attribute:
    # name = graphene.String(description="Name of the producto.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(producto_attribute, name, value)


class create_producto_input(graphene.InputObjectType, producto_attribute):
    """Arguments to create a producto."""

    pass


class create_producto(graphene.Mutation):
    """Mutation to create a producto."""

    producto = graphene.Field(
        producto_schema, description="producto created by this mutation."
    )

    class Arguments:
        input = create_producto_input(required=True)

    def mutate(self, info, input):
        producto = mutation_create(producto_model, input, "idproducto",info)
        return create_producto(producto=producto)


class update_producto_input(graphene.InputObjectType, producto_attribute):
    """Arguments to update a producto."""

    idproducto = graphene.ID(required=True, description="Global Id of the producto.")


class update_producto(graphene.Mutation):
    """Update a producto."""

    producto = graphene.Field(
        producto_schema, description="producto updated by this mutation."
    )

    class Arguments:
        input = update_producto_input(required=True)

    def mutate(self, info, input):
        producto = mutation_update(producto_model, input, "idproducto",info)
        return update_producto(producto=producto)


class delete_producto_input(graphene.InputObjectType, producto_attribute):
    """Arguments to delete a producto."""

    idproducto = graphene.ID(required=True, description="Global Id of the producto.")


class delete_producto(graphene.Mutation):
    """delete a producto."""

    ok = graphene.Boolean(description="producto deleted correctly.")
    message = graphene.String(description="producto deleted message.")

    class Arguments:
        input = delete_producto_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(producto_model, input, "idproducto")
        return delete_producto(ok=ok, message=message)
