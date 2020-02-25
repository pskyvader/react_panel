from .schemas import *
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
import sys, inspect

from . import module_object

# Add schemas to list
clsmembers = inspect.getmembers(sys.modules["graph_ql.schemas"])
schema_list = []
for cl in clsmembers:
    if "schema" in cl[0]:
        schema_list.append(cl)


class attributes_query:
    pass


class attributes_mutation:
    pass


types = []

# add schemas properties to query, mutation and types
for title, sc in schema_list:
    title = title[:-7]
    for property, value in vars(sc).items():
        if property in [ title, "resolve_" + title, "all_" + title, "resolve_all_" + title ]:
            setattr(attributes_query, property, value)
        elif property in ["create_" + title, "update_" + title, "delete_" + title]:
            setattr(attributes_mutation, property, value.Field())
        elif "_schema" in property:
            types.append(value)


class Query(graphene.ObjectType, attributes_query):
    node = relay.Node.Field()
    all_module=module_object.all_module
    resolve_all_module=module_object.resolve_all_module
    module=module_object.module
    resolve_module=module_object.resolve_module


class Mutation(graphene.ObjectType, attributes_mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation, types=types)

