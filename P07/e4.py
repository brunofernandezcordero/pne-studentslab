import http.client
import json
from P01.Seq1 import Seq

def get_gene_id(gene):
    SERVER = 'rest.ensembl.org'
    connection = http.client.HTTPConnection(SERVER)

    try:
        ENDPOINT = f'/lookup/symbol/homo_sapiens/{gene}'
        PARAMS = '?content-type=application/json'
        connection.request("GET", ENDPOINT + PARAMS)
        res = connection.getresponse()
        data = res.read().decode('utf-8')
        response = json.loads(data)
        stable_id = response.get('id', 'Not Found')
        connection.close()
        return stable_id

    except Exception as e:
        print(f'An error occured: {e}')


gene = input('Write the gene here:')
SERVER = 'rest.ensembl.org'
STABLE_ID = get_gene_id(gene)
ENDPOINT = f'/sequence/id/{STABLE_ID}'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINT + PARAMS
connection = http.client.HTTPConnection(SERVER)

try:
    connection.request("GET",ENDPOINT + PARAMS)
    res = connection.getresponse()

    print(f"\nServer: {SERVER}")
    print(f"URL: {URL}")
    print(f"Response received!: {res.status} {res.reason}")
    print()

    data = res.read().decode('utf-8')
    response = json.loads(data)
    n_bases = response.get('seq')
    bases = Seq(response.get('seq'))

    print(f'Gene: {gene}')
    print(f'Description: {response.get('desc')}')
    count = bases.count()
    most_fr_base = ''
    most_fr_count = 0
    for key, value in count.items():
        perc = (value / len(n_bases)) *  100
        perc = round(perc, 2)
        print(f'{key}: {value}  ({perc})')
        if value > most_fr_count:
            most_fr_base = key
    print(f'Most frequent base: {most_fr_base}')

    connection.close()

except Exception as e:
    print(f'An error occured: {e}')
