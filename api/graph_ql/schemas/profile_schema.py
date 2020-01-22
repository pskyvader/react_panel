from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import profile_model
from ..resolver import resolve
from ..mutator import mutation_create, mutation_update, mutation_delete


attribute = dict(
    tipo=graphene.Int(),
    titulo=graphene.String(),
    orden=graphene.Int(),
    estado=graphene.Boolean()
    )
read_only_attribute = dict(
    
    )
black_list_attribute = dict(
    
    )


class profile_schema(SQLAlchemyObjectType):
    class Meta:
        model = profile_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idprofile"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )
    
    


def resolve_profile(args, info, idprofile, **kwargs):
    query = resolve(
        args, info, profile_schema, profile_model, idprofile=idprofile, **kwargs
    )
    return query.first()


def resolve_all_profile(args, info, **kwargs):
    query = resolve(args, info, profile_schema, profile_model, **kwargs)
    return query


all_profile = SQLAlchemyConnectionField( profile_schema, sort=graphene.String() , **attribute )
profile = graphene.Field(profile_schema, idprofile=graphene.Int() , **attribute)

# Create a generic class to mutualize description of profile _attributes for both queries and mutations
class profile_attribute:
    # name = graphene.String(description="Name of the profile.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(profile_attribute, name, value)


class create_profile_input(graphene.InputObjectType, profile_attribute):
    """Arguments to create a profile."""

    pass


class create_profile(graphene.Mutation):
    """Mutation to create a profile."""

    profile = graphene.Field(
        profile_schema, description="profile created by this mutation."
    )

    class Arguments:
        input = create_profile_input(required=True)

    def mutate(self, info, input):
        profile = mutation_create(profile_model, input, "idprofile",info)
        return create_profile(profile=profile)


class update_profile_input(graphene.InputObjectType, profile_attribute):
    """Arguments to update a profile."""

    idprofile = graphene.ID(required=True, description="Global Id of the profile.")


class update_profile(graphene.Mutation):
    """Update a profile."""

    profile = graphene.Field(
        profile_schema, description="profile updated by this mutation."
    )

    class Arguments:
        input = update_profile_input(required=True)

    def mutate(self, info, input):
        profile = mutation_update(profile_model, input, "idprofile",info)
        return update_profile(profile=profile)


class delete_profile_input(graphene.InputObjectType, profile_attribute):
    """Arguments to delete a profile."""

    idprofile = graphene.ID(required=True, description="Global Id of the profile.")


class delete_profile(graphene.Mutation):
    """delete a profile."""

    ok = graphene.Boolean(description="profile deleted correctly.")
    message = graphene.String(description="profile deleted message.")

    class Arguments:
        input = delete_profile_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(profile_model, input, "idprofile")
        return delete_profile(ok=ok, message=message)
