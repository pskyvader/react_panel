from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import administrador_model
from ..resolver import resolve
from ..mutator import mutation_create, mutation_update, mutation_delete
from .. import url_object
from . import image_schema


attribute = dict(
    tipo=graphene.Int(),
    email=graphene.String(),
    nombre=graphene.String(),
    estado=graphene.Boolean(),
    cookie=graphene.String()
    )
read_only_attribute = dict(
    # foto=graphene.JSONString()
    )
black_list_attribute = dict(
    password=graphene.String()
    )


class administrador_schema(SQLAlchemyObjectType):
    class Meta:
        model = administrador_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idadministrador"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )
    
    foto=image_schema.all_image

    def resolve_foto(parent,info, **kwargs):
        return image_schema.resolve_all_image(parent,info,table_name='administrador',idparent=parent.idadministrador,field_name='foto',**kwargs)
    
    


def resolve_administrador(args, info, idadministrador, **kwargs):
    query = resolve(
        args, info, administrador_schema, administrador_model, idadministrador=idadministrador, **kwargs
    )
    return query.first()


def resolve_all_administrador(args, info, **kwargs):
    query = resolve(args, info, administrador_schema, administrador_model, **kwargs)
    return query


all_administrador = SQLAlchemyConnectionField( administrador_schema, sort=graphene.String(), **attribute )
administrador = graphene.Field(administrador_schema, idadministrador=graphene.Int(), **attribute)

# Create a generic class to mutualize description of administrador _attributes for both queries and mutations
class administrador_attribute:
    # name = graphene.String(description="Name of the administrador.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(administrador_attribute, name, value)


class create_administrador_input(graphene.InputObjectType, administrador_attribute):
    """Arguments to create a administrador."""

    pass


class create_administrador(graphene.Mutation):
    """Mutation to create a administrador."""

    administrador = graphene.Field(
        administrador_schema, description="administrador created by this mutation."
    )

    class Arguments:
        input = create_administrador_input(required=True)

    def mutate(self, info, input):
        administrador = mutation_create(administrador_model, input, "idadministrador",info)
        return create_administrador(administrador=administrador)


class update_administrador_input(graphene.InputObjectType, administrador_attribute):
    """Arguments to update a administrador."""

    idadministrador = graphene.ID(required=True, description="Global Id of the administrador.")


class update_administrador(graphene.Mutation):
    """Update a administrador."""

    administrador = graphene.Field(
        administrador_schema, description="administrador updated by this mutation."
    )

    class Arguments:
        input = update_administrador_input(required=True)

    def mutate(self, info, input):
        administrador = mutation_update(administrador_model, input, "idadministrador",info)
        return update_administrador(administrador=administrador)


class delete_administrador_input(graphene.InputObjectType, administrador_attribute):
    """Arguments to delete a administrador."""

    idadministrador = graphene.ID(required=True, description="Global Id of the administrador.")


class delete_administrador(graphene.Mutation):
    """delete a administrador."""

    ok = graphene.Boolean(description="administrador deleted correctly.")
    message = graphene.String(description="administrador deleted message.")

    class Arguments:
        input = delete_administrador_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(administrador_model, input, "idadministrador")
        return delete_administrador(ok=ok, message=message)
