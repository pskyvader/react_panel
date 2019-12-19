import core.format
import json
from graphene import ObjectType, Field, ID, Schema

def init(environ):
    data_return={}
    data={}
    if environ["REQUEST_METHOD"] == "POST":
        length = int(environ.get("CONTENT_LENGTH", 0))
        buffer = environ["wsgi.input"].read(length)
        buffer=buffer.decode("utf-8") 
        buffer=json.loads(buffer)
        query_string=buffer['query']
        variable_string=buffer['variables']
        schema = Schema(query=Query)
        result = schema.execute(query_string, variables=variable_string)
        data={'data':dict(result.data)}

    data_return["status"] = "200 OK"
    data_return["response_body"] = data
    data_return["headers"] = []
    return data_return


class Query(ObjectType):
    def resolve_logo(self, args, context, info):
        print(self,args,context,info)
        return f"asdf"