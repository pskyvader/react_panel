from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from ..models import log_model
from ..resolver import resolve
from ..mutator import mutation_create, mutation_update, mutation_delete


attribute = dict(
    administrador=graphene.String(),
tabla=graphene.String(),
accion=graphene.String(),
fecha=graphene.types.datetime.DateTime()
    )
read_only_attribute = dict(
    
    )
black_list_attribute = dict(
    
    )


class log_schema(SQLAlchemyObjectType):
    class Meta:
        model = log_model
        interfaces = (graphene.relay.Node,)
        only_fields = (
            ["idlog"] + list(attribute.keys()) + list(read_only_attribute.keys())
        )
    
    


def resolve_log(args, info, idlog, **kwargs):
    query = resolve(
        args, info, log_schema, log_model, idlog=idlog, **kwargs
    )
    return query.first()


def resolve_all_log(args, info, **kwargs):
    query = resolve(args, info, log_schema, log_model, **kwargs)
    return query


all_log = SQLAlchemyConnectionField( log_schema, sort=graphene.String(), **attribute )
log = graphene.Field(log_schema, idlog=graphene.Int(), **attribute)

# Create a generic class to mutualize description of log _attributes for both queries and mutations
class log_attribute:
    # name = graphene.String(description="Name of the log.")
    pass


for name, value in {**attribute, **read_only_attribute, **black_list_attribute}.items():
    setattr(log_attribute, name, value)


class create_log_input(graphene.InputObjectType, log_attribute):
    """Arguments to create a log."""

    pass


class create_log(graphene.Mutation):
    """Mutation to create a log."""

    log = graphene.Field(
        log_schema, description="log created by this mutation."
    )

    class Arguments:
        input = create_log_input(required=True)

    def mutate(self, info, input):
        log = mutation_create(log_model, input, "idlog",info)
        return create_log(log=log)


class update_log_input(graphene.InputObjectType, log_attribute):
    """Arguments to update a log."""

    idlog = graphene.ID(required=True, description="Global Id of the log.")


class update_log(graphene.Mutation):
    """Update a log."""

    log = graphene.Field(
        log_schema, description="log updated by this mutation."
    )

    class Arguments:
        input = update_log_input(required=True)

    def mutate(self, info, input):
        log = mutation_update(log_model, input, "idlog",info)
        return update_log(log=log)


class delete_log_input(graphene.InputObjectType, log_attribute):
    """Arguments to delete a log."""

    idlog = graphene.ID(required=True, description="Global Id of the log.")


class delete_log(graphene.Mutation):
    """delete a log."""

    ok = graphene.Boolean(description="log deleted correctly.")
    message = graphene.String(description="log deleted message.")

    class Arguments:
        input = delete_log_input(required=True)

    def mutate(self, info, input):
        (ok, message) = mutation_delete(log_model, input, "idlog")
        return delete_log(ok=ok, message=message)
