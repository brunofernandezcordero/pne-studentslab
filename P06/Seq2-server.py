import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse

seqs = ['ATGCTAGGCTTACGATCGGATCCTAGCTAGGCTAACGTTAGC','CGTTAACGGTAGCTAGCTTACGGAATCCGTTAGGCTAACGTA','TTGACCGTACGATGCTAGGCTTACCGATCGAATGCTAGCTTA',
        'GGCATCGTTAAGCTAGGCTAACGTTAGCTAGCTTACGATCGA','ACGTTAGCTAGGCTTACGATCGTTAACCGGATCTAGCTAGGA']
# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        url_path = urlparse(self.path)
        path = url_path.path  # we get it from here
        arguments = parse_qs(url_path.query)
        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        if self.path == '/':
            contents = Path('html/index.html').read_text()
            self.send_response(200)  # -- Status line: OK!
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()
            self.wfile.write(str.encode(contents))
        elif self.path == '/ping':
            contents = f"""
            <html>
                <body>
                    <h1>PING OK!</h1>
                    <p>The SEQ2 server is running...</p>
                    <a href='/'> Main page </a>
                </body>
            </html>
            """

            self.send_response(200)  # -- Status line: OK!
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()
            self.wfile.write(str.encode(contents))

        elif self.path.startswith('/get'):
            index = int(arguments.get('n',['0'])[0])
            contents = open("html/get.html").read()
            contents = contents.replace("{{index}}", str(index))
            contents = contents.replace("{{sequence}}", seqs[index])
            self.send_response(200)  # -- Status line: OK!
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()
            self.wfile.write(str.encode(contents))

        elif self.path.startswith('/gene'):
            gene = arguments.get('gene',[''])[0]
            gene_txt = open(f'../sequences/{gene}.txt').read()
            contents = open("html/gene.html").read()
            contents = contents.replace("{{gene}}", gene)
            contents = contents.replace("{{gene_txt}}", gene_txt)
            self.send_response(200)  # -- Status line: OK!
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()
            self.wfile.write(str.encode(contents))
        else:
            contents = Path('html/error.html').read_text()
            self.send_response(200)  # -- Status line: OK!
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()
            self.wfile.write(str.encode(contents))
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
