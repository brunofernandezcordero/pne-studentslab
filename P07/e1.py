import http.client
import json

SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/ping'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINT + PARAMS



connection = http.client.HTTPConnection(SERVER)

try:
    connection.request("GET",ENDPOINT + PARAMS)
    res = connection.getresponse()
    print(f'Response received: {res.status} {res.reason}')

    print()
    print(f'Server: {SERVER}')
    print(f'URL: {URL}')


    data = res.read().decode('utf-8')
    response = json.loads(data)


    if response.get('ping') ==1:
        print('PING OK! The database is running!')

    else:
        print('Database not running')
    connection.close()
except Exception as e:
    print(f'An error occured: {e}')
