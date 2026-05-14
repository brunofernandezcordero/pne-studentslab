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
    if data and not data['Error']:
        print(f'The limit established is: {data['limit']}')
        print(f'The database has a total of {data['species_length']} species')
        print(f'The first {limit} species are: {data['species_json']}')
    else:
        print('There was an Error')

    print('-'*30)

    print("\nRequest 2: Information about a species' karyotype")
    species = input('Enter the specie: ')
    data = request(f'/karyotype?species={species}')
    if data and not data['Error']:
        print(f'The species selected is: {species}')
        print(f'The species karyotype is: {data['karyo_list']}')
    else:
        print('There was an Error')

    print('-'*30)


    print("\nRequest 3: Chromosome's Length")
    species = input('Enter the species: ')
    chromosome = input('Enter the chromosome: ')
    data = request(f'/chromosomeLength?species_len={species}&chr={chromosome}')
    if data and not data['Error']:
        print(f'The species and chromosome selected are: {species} - {chromosome}')
        print(f"The chromosome's length is: {data['length']}") #String indices must be integer, not str
    else:
        print('There was an Error')

    print('-'*30)


    print("\nRequest 4: Gene's ID (Human)")
    gene = input('Enter the gene: ')
    data = request(f"/geneLookup?gene={gene}")
    if data and not data['Error']:
        print(f'The gene selected was: {gene}')
        print(f"The gene's ID is: {data['gene_id']}")
    else:
        print('There was an Error')

    print('-'*30)


    print("\nRequest 5: Gene's sequence (Human)")
    gene = input('Enter the gene: ')
    data = request(f"/geneSeq?gene={gene}")
    if data and not data['Error']:
        print(f'The gene selected was {gene}')
        print(f"The gene's sequence is: \n{data['seq']}")
    else:
        print('There was an Error')

    print('-'*30)


    print("\nRequest 6: Gene's Information")
    gene = input('Enter the gene:')
    data = request(f"/geneInfo?gene={gene}")
    if data and not data['Error']:
        print(f'The gene selected was: {gene}')
        print(f"The gene's ID is: {data['gene_id']}")
        print(f"The gene starts at {data['start']} and ends at {data['end']} ")
        print(f"The gene's length is {data['length']}")
    else:
        print('There was an Error')

    print('-'*30)


    print("\nRequest 7: Gene's calculation")
    gene = input('Enter the gene: ')
    data = request(f"/geneCalc?gene={gene}")
    if data and not data['Error']:
        print(f'The gene selected is: {gene}')
        print(f"The gene's length is {data['length']}")
        print(f"The bases percentages are: {data['perc_html']}")
    else:
        print('There was an Error')

    print('-'*30)


    print("\nRequest 8: Gene overlap")
    chr = input('Select the chromosome: ')
    start = input('Select the start: ')
    end = input('Select the end: ')
    data = request(f"/geneList?chromo={chr}&start={int(start)}&end={int(end)}")
    if data and not data['Error']:
        print(f'The chromosome chosen was: {chr}')
        print(f'The start and end chosen were: {start}-{end}')
        print(f'The genes overlapping in this region are: {data['overlap_html']}')
    else:
        print('There was an Error')

    print('-' * 30)
