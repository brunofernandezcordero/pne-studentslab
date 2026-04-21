import http.client
import json

SERVER = 'rest.ensembl.org'
STABLE_ID = 'ENSG00000207552'
gene = 'MIR633'
ENDPOINT = f'/sequence/id/{STABLE_ID}'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINT + PARAMS
connection = http.client.HTTPConnection(SERVER)

try:
    connection.request("GET",ENDPOINT + PARAMS)
    res = connection.getresponse()

    print(f"Server: {SERVER}")
    print(f"URL: {URL}")
    print(f"Response received!: {res.status} {res.reason}")
    print()

    data = res.read().decode('utf-8')
    response = json.loads(data)

    print(f'Gene: {gene}')
    print(f'Description: {response.get('desc')}')
    print(f'Bases: {response.get('seq')}')

    connection.close()

except Exception as e:
    print(f'An error occured: {e}')
