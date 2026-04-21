import http.client
import json

genes_list = ["FRAT1", "ADA", "FXN", "RNU6_269P", "MIR633", "TTTY4C", "RBMY2YP", "FGFR3", "KDR", "ANK2"]
SERVER = 'rest.ensembl.org'
connection = http.client.HTTPConnection(SERVER)


try:
    for gene in genes_list:
        ENDPOINT = f'/lookup/symbol/homo_sapiens/{gene}'
        PARAMS = '?content-type=application/json'
        URL = SERVER + ENDPOINT + PARAMS
        connection.request("GET",ENDPOINT + PARAMS)
        res = connection.getresponse()
        data = res.read().decode('utf-8')
        response = json.loads(data)
        stable_id = response.get('id','Not Found')
        print(f'{gene:<12}|  {stable_id}')
        connection.close()

except Exception as e:
    print(f'An error occured: {e}')
