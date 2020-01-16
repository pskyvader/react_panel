from graphql.error import format_error
from .schema import schema

from graphql_server import (HttpQueryError, default_format_error, encode_execution_results, json_encode, load_json_body, run_http_query)
from urllib.parse import parse_qsl
import http.client
import json


def init(environ):
    data_return = {'headers':[]}
    data = {}
    status_code=200
    if environ["REQUEST_METHOD"] == "POST":
        print('parse')
        data  = parse_body(environ)
        print('run query')
        execution_results, params = run_http_query( schema, 'post', data)
        print('encode results')
        result, status_code = encode_execution_results( execution_results, format_error=default_format_error,is_batch=False, encode=json_encode)
        result=json.loads(result)
        
        if 'data' in result and 'errors' not in result:
            data = {"data": result['data']}
        else:
            data = {'errors':[format_error(e) for e in result['errors']]}
        print('fin')

    data_return["status"] = '{} {}'.format(status_code, http.client.responses[status_code])
    data_return["response_body"] = data
    try:
        pass
    except Exception as e:
        error_message='Error {}'.format(e)
        status_code=getattr(e, 'status_code', 500)
        data_return["status"] =  '{} {}'.format(status_code, http.client.responses[status_code])
        data_return["response_body"] = {'errors':[error_message]}

    return data_return



def parse_body(environ):
    try:
        content_length = int(environ.get("CONTENT_LENGTH", 0))
    except ValueError as e:
        print('can\'t parse content_length "{}" (ValueError {})'
              .format(environ.get('CONTENT_LENGTH'), e))
        return {}
    content_type = environ['CONTENT_TYPE'].split(';')
    body = environ['wsgi.input'].read(content_length)
    
    if content_type[0] == 'application/graphql':
        return {'query': body.decode('utf8')}
    if content_type[0] in ('application/json', 'text/plain'):
        return load_json_body(body.decode('utf8'))
    if content_type[0] == 'application/x-www-form-urlencoded':
        return dict(parse_qsl(body.decode('utf8')))
    else:
        raise HttpQueryError(
            400,
            'Content of type "{}" is not supported.'.format(content_type[0])
        )