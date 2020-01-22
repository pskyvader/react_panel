from .schemas import *
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField


import sys, inspect
clsmembers = inspect.getmembers(sys.modules['graph_ql.schemas'])

schema_list=[]
for cl in clsmembers:
    if 'schema' in cl[0]:
        schema_list.append(cl)



class attributes_query:
    pass

class attributes_mutation:
    pass

for title,sc in schema_list:
    title=title[:-7]
    for property, value in vars(sc).items():
        if property==title:
            setattr(attributes_query, property, value)
        elif property=='resolve_'+title:
            setattr(attributes_query, 'resolve_'+title, value)
        elif property=='all_'+title:
            setattr(attributes_query, 'all_'+title, value)
        elif property=='resolve_all_'+title:
            setattr(attributes_query, 'resolve_all_'+title, value)
        elif property=='create_'+title:
            setattr(attributes_mutation, 'create_'+title, value.Field())
        elif property=='update_'+title:
            setattr(attributes_mutation, 'update_'+title, value.Field())
        elif property=='delete_'+title:
            setattr(attributes_mutation, 'delete_'+title, value.Field())

        

class Query(graphene.ObjectType,attributes_query):
    node = relay.Node.Field()


    
class Mutation(graphene.ObjectType,attributes_mutation):
    pass
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    

# __TYPES__
    
schema = graphene.Schema(query=Query,mutation=Mutation)
# __TYPES__
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    