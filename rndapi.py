#https://teletype.in/@snakeblog/rJnA9jwEX
from http.client import HTTPSConnection
from json import dumps, loads

def get(max):
    token = '2d1c0ee4-7945-49a3-8e39-ae076ce9fde6'

    request_data = {
      'jsonrpc': '2.0',
      'method': 'generateIntegers',
      'params': {
        'apiKey': token,
        'min': 1,
        'max': max,
        'n': 1,
      },
      'id': 1,
    }
    encoded_data = dumps(request_data)

    headers = {
      'Content-Type': 'application/json-rpc',  # Тип запроса
    }
    encoded_headers = dumps(headers)

    connection = HTTPSConnection('api.random.org')
    connection.request('GET', '/json-rpc/1/invoke', encoded_data, headers)

    response = connection.getresponse()
    response_data = loads(response.read().decode())

    return response_data['result']['random']['data'][0]
