import socket

PORT = 8080
IP = '10.8.49.55'

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creating the socket

ls.bind((IP,PORT)) #binding the socket to an adress

ls.listen() #Configurating the socket in listening mode

print("The server is configured")
# Waits for a client to connect

while True:

    print("Waiting for Clients to connect")
    try:
        (cs,client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    else:
        print("A client has connected to the server")

        # Reads message of the client
        # The received message is in raw bytes

        msg_raw = cs.recv(2048)

        # Decode it for converting it into a human-readable stirng
        msg = msg_raw.decode()

        # Print the message received
        print(f"Received Message: {msg}")

        response = "HELLO. I am the Happy Server"
        #Encode the message into bytes
        cs.send(response.encode())
        cs.close()

        ls.close() #Close the socket.

# Send a respone