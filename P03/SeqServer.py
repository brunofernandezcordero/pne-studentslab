from P01.Seq1 import Seq
from P02.Client0 import Client
import socket
from termcolor import colored

IP = "212.128.255.84"
PORT = 8080
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creating the socket

ls.bind((IP,PORT)) #binding the socket to an adress

ls.listen() #Configurating the socket in listening mode

print("SEQ Server configured")
# Waits for a client to connect

while True:

    print("Waiting for Clients...")
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
        if msg.upper() == "PING":
            response = "OK!"
            # Print the message received
            color_msg = colored(msg + "command","green")
            print(f"{color_msg}")
            print("OK!")

            #Encode the message into bytes
            cs.send(response.encode())
            cs.close()

        ls.close() #Close the socket.
