from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import image_model
from ..resolver import resolve,Url
from ..mutator import mutation_create, mutation_update, mutation_delete


attribute = dict(
    table_name=graphene.String(),
    field_name=graphene.String(),
    idparent=graphene.Int(),
    name=graphene.String(),
    extension=graphene.String(),
    orden=graphene.Int(),
    estado=graphene.Boolean(),
    portada=graphene.Boolean()
    )
read_only_attribute = dict(
    
    )
black_list_attribute = dict(
    
    )


class image_schema(SQLAlchemyObjectType):
    class Meta:
        model = image_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idimage"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )
    
    
    url = graphene.List(Url)

    def resolve_url(parent, info):
        import inspect
        # print(inspect.getmembers(info, lambda a:not(inspect.isroutine(a))))

        print(info.operation.selection_set.selections[0])
        recorte={'width':None,'height':None,'format':None,'regenerate':None}
        

        print(info.operation.selection_set.selections[0].arguments)
        for argument in info.operation.selection_set.selections[0].arguments:
            if argument.name.value in recorte:
                recorte[argument.name.value]=argument.value.value

        return [Url(parent,recorte)]


def resolve_image(args, info, idimage, **kwargs):
    query = resolve(
        args, info, image_schema, image_model, idimage=idimage, **kwargs
    )
    return query.first()


def resolve_all_image(args, info, **kwargs):
    query = resolve(args, info, image_schema, image_model, **kwargs)
    return query


all_image = SQLAlchemyConnectionField( image_schema, sort=graphene.String() , width=graphene.String(), height=graphene.String(), format=graphene.String(), regenerate=graphene.Boolean(), **attribute )
image = graphene.Field(image_schema, idimage=graphene.Int() , width=graphene.String(), height=graphene.String(), format=graphene.String(), regenerate=graphene.Boolean(), **attribute)

# Create a generic class to mutualize description of image _attributes for both queries and mutations
class image_attribute:
    # name = graphene.String(description="Name of the image.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(image_attribute, name, value)


class create_image_input(graphene.InputObjectType, image_attribute):
    """Arguments to create a image."""

    pass


class create_image(graphene.Mutation):
    """Mutation to create a image."""

    image = graphene.Field(
        image_schema, description="image created by this mutation."
    )

    class Arguments:
        input = create_image_input(required=True)

    def mutate(self, info, input):
        image = mutation_create(image_model, input, "idimage",info)
        return create_image(image=image)


class update_image_input(graphene.InputObjectType, image_attribute):
    """Arguments to update a image."""

    idimage = graphene.ID(required=True, description="Global Id of the image.")


class update_image(graphene.Mutation):
    """Update a image."""

    image = graphene.Field(
        image_schema, description="image updated by this mutation."
    )

    class Arguments:
        input = update_image_input(required=True)

    def mutate(self, info, input):
        image = mutation_update(image_model, input, "idimage",info)
        return update_image(image=image)


class delete_image_input(graphene.InputObjectType, image_attribute):
    """Arguments to delete a image."""

    idimage = graphene.ID(required=True, description="Global Id of the image.")


class delete_image(graphene.Mutation):
    """delete a image."""

    ok = graphene.Boolean(description="image deleted correctly.")
    message = graphene.String(description="image deleted message.")

    class Arguments:
        input = delete_image_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(image_model, input, "idimage")
        return delete_image(ok=ok, message=message)
