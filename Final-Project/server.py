import http.server
import http.client
import json
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import socketserver
from P01.Seq1 import Seq


def get_ensembl_file(endpoint,overlap=None):
    SERVER = 'rest.ensembl.org'
    connection = http.client.HTTPConnection(SERVER)
    ENDPOINT = endpoint
    PARAMS = '?content-type=application/json'
    if overlap:
        PARAMS = '&content-type=application/json'
    connection.request("GET", ENDPOINT + PARAMS)
    res = connection.getresponse()
    data = res.read().decode('utf-8')
    response = json.loads(data)
    connection.close()
    return response

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Print the request line
        url_path = urlparse(self.path)
        path = url_path.path  # we get it from here
        arguments = parse_qs(url_path.query)
        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        try:
            if self.path == '/':
                with open('html/index.html', 'r') as f:
                    contents = f.read()

            elif self.path.startswith('/listSpecies'):
                try:
                    limit = arguments.get('limit',[None])[0]
                    endpoint_sp = '/info/species'
                    species_json1 = get_ensembl_file(endpoint_sp)
                    species_list = species_json1.get('species',[])
                    species_json = [sp['display_name'] for sp in species_list]
                    if limit:
                        species_json = species_json[: int(limit)]
                    species_html = ''
                    for sp in species_json:
                        species_html += f'<li>{sp}</li>'

                    contents = f"""
                    <!DOCTYPE html>
                    <html lang="en" dir="ltr">
                      <head>
                        <meta charset="utf-8">
                        <title>List of Species</title>
                      </head>
                      <body style="background-color: lightblue;">
                        <h1>Species</h1>
                        <a href="/">Main Page</a>
                        <p>The total number of species in ensembl is: {len(species_list)}</p>
                        <p> The limit you have selected is: {limit}</p>
                        <p> The names of the species are: 
                            <ul> {species_html} </ul>
                      </body>
                    </html>
                    """
                except Exception:
                    contents = Path('html/error.html').read_text()

            elif self.path.startswith('/karyotype'):
                try:
                    species_karyo = arguments.get('species',[None])[0]
                    if not species_karyo:
                        contents = Path('html/error.html').read_text()
                    else:
                        endpoint_karyo = f'/info/assembly/{species_karyo}'
                        species_assembly_json = get_ensembl_file((endpoint_karyo))
                        karyo_list = species_assembly_json.get('karyotype',[])
                        karyo_html = ''
                        for ch in karyo_list:
                            karyo_html += f'<li>{ch}</li>'
                        contents =  f"""
                        <!DOCTYPE html>
                        <html lang="en" dir="ltr">
                          <head>
                            <meta charset="utf-8">
                            <title>List of Chromosomes</title>
                          </head>
                          <body style="background-color: lightblue;">
                            <h1>Species' Chromosomes</h1>
                            <a href="/">Main Page</a>
                            <p> The species you have selected is: {species_karyo}
                            <p> The names of the chromosomes are: 
                                <ul> {karyo_html} </ul>
                          </body>
                        </html>
                        """

                except Exception:
                    contents = Path('html/error.html').read_text()

            elif self.path.startswith('/chromosomeLength'):
                try:
                    species_len = arguments.get('species_len',[None])[0]
                    chr = arguments.get('chr',[None])[0]
                    if not species_len or not chr:
                        contents = Path('html/error.html').read_text()
                    else:
                        endpoint_len = f'/info/assembly/{species_len}'
                        species_assembly_json = get_ensembl_file((endpoint_len))
                        chr_dicts = species_assembly_json.get('top_level_region', [])
                        length = 'The chromosome was not found'
                        for c in chr_dicts:
                            if chr == c['name']:
                                length = c['length']
                                break

                        contents = f"""
                            <!DOCTYPE html>
                            <html lang="en" dir="ltr">
                              <head>
                                <meta charset="utf-8">
                                <title>Chromosome's Length</title>
                              </head>
                              <body style="background-color: lightblue;">
                                <h1>Chromosome's Length</h1>
                                <a href="/">Main Page</a>
                                <p> The species you have selected is: {species_len}
                                <p> The chromosome you have selected is: {chr} <p/>
                                <p> The length of the chromosome is: {length} </p>
                              </body>
                            </html>
                            """
                except Exception:
                    contents = Path('html/error.html').read_text()

            elif self.path.startswith('/geneLookup'):
                try:
                    gene = arguments.get('gene',[])[0]
                    endpoint = f'/lookup/symbol/homo_sapiens/{gene}'
                    gene_json = get_ensembl_file(endpoint)
                    gene_id = gene_json.get('id',['Not Found'])
                    contents = f"""
                    <!DOCTYPE html>
                    <html lang="en" dir="ltr">
                      <head>
                        <meta charset="utf-8">
                        <title>Human Gene's Stable Identifier (id)</title>
                      </head>
                      <body style="background-color: lightblue;">
                        <h1>Huma Gene's Stable Identifier (id)</h1>
                        <a href="/">Main Page</a>
                        <p> The gene  you have selected is: {gene} </p>
                        <p> The gene's stable identifier is : {gene_id} </p>
                      </body>
                    </html>
                    """
                except Exception:
                    contents = Path('html/error.html').read_text()

            elif self.path.startswith('/geneSeq'):
                try:
                    gene = arguments.get('gene', [])[0]
                    endpoint_id = f'/lookup/symbol/homo_sapiens/{gene}'
                    gene_json = get_ensembl_file(endpoint_id)
                    gene_id = gene_json.get('id', ['Not Found'])
                    endpoint_seq = f'/sequence/id/{gene_id}'
                    seq = get_ensembl_file(endpoint_seq)
                    seq = seq.get('seq',['Not Found'])
                    contents = f"""
                    <!DOCTYPE html>
                    <html lang="en" dir="ltr">
                      <head>
                        <meta charset="utf-8">
                        <title>Human Gene's Stable Identifier (id)</title>
                      </head>
                      <body style="background-color: lightblue;">
                        <h1>Huma Gene's Stable Identifier (id)</h1>
                        <a href="/">Main Page</a>
                        <p> The gene  you have selected is: {gene} </p>
                        <p> The gene's sequence is : {seq} </p>
                      </body>
                    </html>
                    """

                except Exception:
                    contents = Path('html/error.html').read_text()

            elif self.path.startswith('/geneInfo'):
                try:
                    gene = arguments.get('gene', [])[0]
                    endpoint_id = f'/lookup/symbol/homo_sapiens/{gene}'
                    gene_json = get_ensembl_file(endpoint_id)
                    gene_id = gene_json.get('id', ['Not Found'])
                    start = gene_json.get('start',None)
                    end = gene_json.get('end', None)
                    length = end - start + 1
                    name = gene_json.get('assembly_name','Not found')
                    contents = f"""
                    <!DOCTYPE html>
                    <html lang="en" dir="ltr">
                      <head>
                        <meta charset="utf-8">
                        <title>Gene's Basic Information</title>
                      </head>
                      <body style="background-color: lightblue;">
                        <h1>Gene's Basic Information</h1>
                        <a href="/">Main Page</a>
                        <p> The gene  you have selected is: {gene} </p>
                        <p> The gene's id is : {gene_id} </p>
                        <p> The gene's start is: {start}</p>
                        <p> The gene's end is: {end}</p>
                        <p> The gene's length is: {length} </p>
                      </body>
                    </html>
                    """

                except Exception:
                    contents = Path('html/error.html').read_text()

            elif self.path.startswith('/geneCalc'):
                try:
                    gene = arguments.get('gene', [''])[0]
                    endpoint_id = f'/lookup/symbol/homo_sapiens/{gene}'
                    gene_json = get_ensembl_file(endpoint_id)
                    gene_id = gene_json.get('id', [''])
                    endpoint_seq = f'/sequence/id/{gene_id}'
                    seq = get_ensembl_file(endpoint_seq)
                    seq = seq.get('seq', ['Not Found'])
                    length = len(seq)
                    s_seq = Seq(seq)
                    dict_count = s_seq.count()
                    if length > 0:
                        percentages = {base: (count / length) * 100 for base, count in dict_count.items()}
                    else:
                        percentages = {}
                    perc_html = ''
                    for base, perc in percentages.items():
                        perc_html += f'\n{base}: {perc:.2f}%'
                    contents = f"""
                    <!DOCTYPE html>
                    <html lang="en" dir="ltr">
                      <head>
                        <meta charset="utf-8">
                        <title>Gene's Calculations</title>
                      </head>
                      <body style="background-color: lightblue;">
                        <h1>Gene's Calculations</h1>
                        <a href="/">Main Page</a>
                        <p> The gene  you have selected is: {gene} </p>
                        <p> The gene's length is: {length} </p>
                        <p> The bases percentages are: {perc_html}</p>
                      </body>
                    </html>
                    """
                except Exception:
                    contents = Path('html/error.html').read_text()

            elif self.path.startswith('/geneList'):
                try:
                    chromo = arguments.get('chromo',[])[0]
                    start = int(arguments.get('start',[])[0])
                    end = int(arguments.get('end',[])[0])
                    region = f'{chromo}:{start}-{end}'
                    endpoint = f'/overlap/region/human/{region}?feature=gene'
                    overlap_genes_dict = get_ensembl_file(endpoint,True)
                    overlap_html = set()
                    for gene in overlap_genes_dict:
                        name = gene.get('external_name')
                        if name:
                            overlap_html.add(name)
                    contents = f"""
                    <!DOCTYPE html>
                    <html lang="en" dir="ltr">
                      <head>
                        <meta charset="utf-8">
                        <title>Gene's Overlapping</title>
                      </head>
                      <body style="background-color: lightblue;">
                        <h1>Gene's Overlapping</h1>
                        <a href="/">Main Page</a>
                        <p> The chromosome you have selected is: {chromo} </p>
                        <p> The start coordinate is: {start} </p>
                        <p> The end coordinate is: {end}</p>
                        <p> The genes that overlap in this region are/is:</p>
                        <p> {overlap_html} </p>
                      </body>
                    </html>
                    """
                except Exception:
                    contents = Path('html/error.html').read_text()
            else:
                contents = Path('html/error.html').read_text()



        except FileNotFoundError:
            contents = Path('html/error.html').read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()