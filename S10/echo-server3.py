import socket
from termcolor import colored
PORT = 8080
IP = '212.128.255.98'

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creating the socket
ls.bind((IP, PORT))  # binding the socket to an address
ls.listen()  # Configurating the socket in listening mode

print("The server is configured")
connection = 0
client_list = []
while True:
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")
        break

    else:
        connection += 1
        print(f"CONNECTION {connection} Client IP,PORT: {client_ip_port}")
        client_list.append(client_ip_port)
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        color_msg = colored(msg,"green")

        print(f"Received Message: {color_msg}")

        response = f"ECHO: {msg}"
        cs.send(response.encode())

        if len(client_list) == 5:
            for j,i in enumerate(client_list):
                print(f"Client {j}: {i}")
            break

        cs.close()  # close only the client socket

ls.close()  # close the server socket when exiting