import http.client
import json

SERVER = 'localhost'
PORT = 8080

def request(ENDPOINT):
    try:
        conn = http.client.HTTPConnection(SERVER,PORT)
        if '?' in ENDPOINT:
            ENDPOINT += '&json=1'
        else:
            ENDPOINT += '?json=1'
        conn.request('GET',ENDPOINT)
        res = conn.getresponse()
        if res.status == 200:
            data = res.read().decode('utf-8')
            return json.loads(data)
        else:
            print(f'HTTP ERROR: {res.status}')
            return None

    except Exception as e:
        print(f'An error has occured: {e}')

if __name__ == '__main__':
    print('-'*30)
    print('         REST API CLIENT         ')
    print('-'*30)

    print('\nRequest 1: List of species in database')
    limit = int(input('Enter the limit desired: '))
    data = request(f'/listSpecies?limit={limit}')
    if data:
        print(f'The limit established is: {data['limit']}')
        print(f'The database has a total of {data['species_length']} species')
        print(f'The first {limit} species are: {data['species_json']}')

    # Temrminar ultimas request igual que la primera