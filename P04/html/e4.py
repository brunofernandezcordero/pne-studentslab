import socket
from termcolor import colored


# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # -- Split the request messages into lines
    lines = req.split('\n')

    # -- The request line is the first
    req_line = lines[0]



    print("Request line: ", end="")
    parts = req_line.strip().split()
    base = None
    if len(parts) >= 2:
        path = parts[1]

        if path == '/favicon.ico':
            body = ""
        else:
            path_parts = path.split('/')

            if len(path_parts) >= 3:
                base = path_parts[2]
    try:
        if base =='A':
            print(f'Base {base}')
            with open('../P04/html/info/A.html', 'r') as f:
                body = f.read()
        elif base == 'C':
            print(f'Base {base}')
            with open('../P04/html/info/C.html', 'r') as f:
                body = f.read()
        elif base == 'G':
            print(f'Base {base}')
            with open('../P04/html/info/G.html', 'r') as f:
                body = f.read()
        elif base == 'T':
            print(f'Base {base}')
            with open('../P04/html/info/T.html', 'r') as f:
                body = f.read()
    except FileNotFoundError:
        body = "404 Not Found"





    # -- Generate the response message
    # It has the following lines
    # Status line
    # header
    # blank line
    # Body (content to send)

    # This new contents are written in HTML language

    # -- Status line: We respond that everything is ok (200 code)
    status_line = "HTTP/1.1 200 OK\n"

    # -- Add the Content-Type header
    header = "Content-Type: text/html\n"

    # -- Add the Content-Length
    header += f"Content-Length: {len(body)}\n"

    # -- Build the message by joining together all the parts
    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())


# -------------- MAIN PROGRAM
# ------ Configure the server
# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Setup up the socket's IP and PORT
ls.bind((IP, PORT))

# -- Become a listening socket
ls.listen()

print("Green server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped!")
        ls.close()
        exit()
    else:

        # Service the client

        process_client(cs)

        # -- Close the socket
        cs.close()
