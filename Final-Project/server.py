import http.server
import json
import termcolor
import socketserver

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
                # Remove '/info/' from path
                limit = arguments.get('gene',['0'])[0]
                filename = f'html/{path}.html'  # "html/a.html"
                contents =
            else:
                with open('html/error.html', 'r') as f:
                    contents = f.read()

        except FileNotFoundError:
            with open('html/error.html', 'r') as f:
                contents = f.read()

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