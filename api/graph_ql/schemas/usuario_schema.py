from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import usuario_model
from ..resolver import resolve
from ..mutator import mutation_create, mutation_update, mutation_delete
from .image_schema import all_image,resolve_all_image

attribute = dict(
    tipo=graphene.Int(),
    nombre=graphene.String(),
    telefono=graphene.String(),
    email=graphene.String(),
    estado=graphene.Boolean(),
    cookie=graphene.String()
    )
read_only_attribute = dict(
    
    )
black_list_attribute = dict(
    password=graphene.String()
    )


class usuario_schema(SQLAlchemyObjectType):
    class Meta:
        model = usuario_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idusuario"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )
    
    
    foto=all_image
    def resolve_foto(parent,info, **kwargs):
        return resolve_all_image(parent,info,table_name='usuario',idparent=parent.idusuario,field_name='foto',**kwargs)



def resolve_usuario(args, info, idusuario, **kwargs):
    query = resolve(
        args, info, usuario_schema, usuario_model, idusuario=idusuario, **kwargs
    )
    return query.first()


def resolve_all_usuario(args, info, **kwargs):
    query = resolve(args, info, usuario_schema, usuario_model, **kwargs)
    return query


all_usuario = SQLAlchemyConnectionField( usuario_schema, sort=graphene.String(), **attribute )
usuario = graphene.Field(usuario_schema, idusuario=graphene.Int(), **attribute)

# Create a generic class to mutualize description of usuario _attributes for both queries and mutations
class usuario_attribute:
    # name = graphene.String(description="Name of the usuario.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(usuario_attribute, name, value)


class create_usuario_input(graphene.InputObjectType, usuario_attribute):
    """Arguments to create a usuario."""

    pass


class create_usuario(graphene.Mutation):
    """Mutation to create a usuario."""

    usuario = graphene.Field(
        usuario_schema, description="usuario created by this mutation."
    )

    class Arguments:
        input = create_usuario_input(required=True)

    def mutate(self, info, input):
        usuario = mutation_create(usuario_model, input, "idusuario",info)
        return create_usuario(usuario=usuario)


class update_usuario_input(graphene.InputObjectType, usuario_attribute):
    """Arguments to update a usuario."""

    idusuario = graphene.ID(required=True, description="Global Id of the usuario.")


class update_usuario(graphene.Mutation):
    """Update a usuario."""

    usuario = graphene.Field(
        usuario_schema, description="usuario updated by this mutation."
    )

    class Arguments:
        input = update_usuario_input(required=True)

    def mutate(self, info, input):
        usuario = mutation_update(usuario_model, input, "idusuario",info)
        return update_usuario(usuario=usuario)


class delete_usuario_input(graphene.InputObjectType, usuario_attribute):
    """Arguments to delete a usuario."""

    idusuario = graphene.ID(required=True, description="Global Id of the usuario.")


class delete_usuario(graphene.Mutation):
    """delete a usuario."""

    ok = graphene.Boolean(description="usuario deleted correctly.")
    message = graphene.String(description="usuario deleted message.")

    class Arguments:
        input = delete_usuario_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(usuario_model, input, "idusuario")
        return delete_usuario(ok=ok, message=message)
