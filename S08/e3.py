import socket

# SERVER IP, PORT
PORT = 8081
IP = "212.128.255.82" # it depends on the machine the server is running

while True:
    # First, create the socket
    # We will always use these parameters: AF_INET y SOCK_STREAM
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send data. No strings can be sent, only bytes
    # It necesary to encode the string into bytes
    s.send(str.encode("HELLO FROM THE CLIENT!!!"))

    # Closing the socket
    s.close()
