import http.server
import http.client
import json
import termcolor
from urllib.parse import parse_qs, urlparse
import socketserver
from P01.Seq1 import Seq
import jinja2 as j
from pathlib import Path


def read_html_file(filename):
    # Read the HTML file as text
    contents = Path("html/" + filename).read_text()

    # Convert the text into a Jinja template object
    contents = j.Template(contents)

    return contents

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
        json_mode = False
        # Print the request line
        url_path = urlparse(self.path)
        path = url_path.path  # we get it from here
        arguments = parse_qs(url_path.query)
        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        try:
            json_mode = arguments.get('json',[0])[0] =='1'
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

                    contents = read_html_file('listspecies.html').render(
                            species_html=species_html,
                            species_length=len(species_list),
                            limit=limit
                        )
                    if json_mode:
                        contents = {
                            'Error': False,
                            'species_json':species_json,
                            'species_length': len(species_list),
                            'limit': limit
                        }
                except Exception:
                    contents = Path('html/error.html').read_text()
                    if json_mode:
                        contents = {'Error': True}

            elif self.path.startswith('/karyotype'):
                try:
                    species_karyo = arguments.get('species',[None])[0]
                    if not species_karyo:
                        contents = Path('html/error.html').read_text()
                    else:
                        endpoint_karyo = f'/info/assembly/{species_karyo}'
                        species_assembly_json = get_ensembl_file((endpoint_karyo))
                        karyo_list = species_assembly_json.get('karyotype',None)
                        if not karyo_list:
                            contents = Path('html/error.html').read_text()
                        else:
                            karyo_html = ''
                            for ch in karyo_list:
                                karyo_html += f'<li>{ch}</li>'
                            contents = read_html_file('karyotype.html').render(
                                species_karyo=species_karyo,
                                karyo_html=karyo_html
                            )
                            if json_mode:
                                contents = {
                                    'Error': False,
                                    'species_karyo': species_karyo,
                                    'karyo_list': karyo_list
                                }

                except Exception:
                    contents = Path('html/error.html').read_text()
                    if json_mode:
                        contents = {'Error': True}

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

                        contents = read_html_file('chromosome_length.html').render(
                            species_len=species_len,
                            chr=chr,
                            length=length # String indeces must be integers, not str
                        )
                        if json_mode:
                            contents = {
                                'Error': False,
                                'species_len': species_len,
                                'chr': chr,
                                'length': length
                            }
                except Exception:
                    contents = Path('html/error.html').read_text()
                    if json_mode:
                        contents = {'Error': True}

            elif self.path.startswith('/geneLookup'):
                try:
                    gene = arguments.get('gene',[])[0]
                    endpoint = f'/lookup/symbol/homo_sapiens/{gene}'
                    gene_json = get_ensembl_file(endpoint)
                    gene_id = gene_json.get('id','Not found')
                    if not gene_id:
                        contents = Path('html/error.html').read_text()
                    else:
                        contents = read_html_file('gene_lookup.html').render(
                            gene=gene,
                            gene_id=gene_id
                        )
                        if json_mode:
                            contents = {
                                'Error': False,
                                'gene': gene,
                                'gene_id': gene_id
                            }
                except Exception:
                    contents = Path('html/error.html').read_text()
                    if json_mode:
                        contents = {'Error': True}

            elif self.path.startswith('/geneSeq'):
                try:
                    gene = arguments.get('gene', [])[0]
                    endpoint_id = f'/lookup/symbol/homo_sapiens/{gene}'
                    gene_json = get_ensembl_file(endpoint_id)
                    gene_id = gene_json.get('id', None)
                    if not gene_id:
                        contents = Path('html/error.html').read_text()
                        if json_mode:
                            contents = {'Error': True}
                    else:
                        endpoint_seq = f'/sequence/id/{gene_id}'
                        seq = get_ensembl_file(endpoint_seq)
                        seq = seq.get('seq',['Not Found'])
                        formatted_seq = '\n'.join(
                            seq[i:i + 80] for i in range(0, len(seq), 80)
                        )
                        contents = read_html_file('gene_seq.html').render(
                            gene=gene,
                            seq=formatted_seq
                        )
                        if json_mode:
                            contents = {
                                'Error': False,
                                'gene': gene,
                                'seq': seq
                            }

                except Exception:
                    contents = Path('html/error.html').read_text()
                    if json_mode:
                        contents = {'Error': True}

            elif self.path.startswith('/geneInfo'):
                try:
                    gene = arguments.get('gene', [])[0]
                    endpoint_id = f'/lookup/symbol/homo_sapiens/{gene}'
                    gene_json = get_ensembl_file(endpoint_id)
                    gene_id = gene_json.get('id', 'Not Found')
                    start = gene_json.get('start',None)
                    end = gene_json.get('end', None)
                    length = end - start + 1
                    contents = read_html_file('gene_info.html').render(
                        gene=gene,
                        gene_id=gene_id,
                        start=start,
                        end=end,
                        length=length
                    )
                    if json_mode:
                        contents = {
                            'Error': False,
                            'gene': gene,
                            'gene_id': gene_id,
                            'start': start,
                            'end': end,
                            'length': length
                        }

                except Exception:
                    contents = Path('html/error.html').read_text()
                    if json_mode:
                        contents = {'Error': True}

            elif self.path.startswith('/geneCalc'):
                try:
                    gene = arguments.get('gene', [''])[0]
                    endpoint_id = f'/lookup/symbol/homo_sapiens/{gene}'
                    gene_json = get_ensembl_file(endpoint_id)
                    gene_id = gene_json.get('id', [''])
                    endpoint_seq = f'/sequence/id/{gene_id}'
                    seq = get_ensembl_file(endpoint_seq)
                    seq = seq.get('seq', 'Not Found')
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
                    contents = read_html_file('gene_calc.html').render(
                        gene=gene,
                        length=length,
                        perc_html=perc_html
                    )
                    if json_mode:
                        contents = {
                            'Error': False,
                            'gene': gene,
                            'length': length,
                            'perc_html': perc_html
                        }
                except Exception:
                    contents = Path('html/error.html').read_text()
                    if json_mode:
                        contents = {'Error': True}


            elif self.path.startswith('/geneList'):
                try:
                    chromo = arguments.get('chromo',[None])[0]
                    start = int(arguments.get('start',[None])[0])
                    end = int(arguments.get('end',[None])[0])
                    region = f'{chromo}:{start}-{end}'
                    endpoint = f'/overlap/region/human/{region}?feature=gene'
                    overlap_genes_dict = get_ensembl_file(endpoint,True)
                    overlap_html = []
                    for gene in overlap_genes_dict:
                        name = gene.get('external_name')
                        if name:
                            overlap_html.append(name)
                    if not overlap_html:
                        overlap_html = "No genes overlapping this region were found."
                    contents = read_html_file('gene_list.html').render(
                        chromo=chromo,
                        start=start,
                        end=end,
                        overlap_html=overlap_html
                    )
                    if json_mode:
                        contents = {
                            'Error': False,
                            'chromo': chromo,
                            'start': start,
                            'end': end,
                            'overlap_html': overlap_html
                        }
                except Exception:
                    contents = Path('html/error.html').read_text()
                    if json_mode:
                        contents = {'Error': True}
            else:
                contents = Path('html/error.html').read_text()



        except FileNotFoundError:
            contents = Path('html/error.html').read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        if json_mode:
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(contents).encode())
        else:
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(contents.encode()))
            self.end_headers()
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