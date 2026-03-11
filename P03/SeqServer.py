import socket
from P01.Seq1 import Seq
from termcolor import colored

seq_list = ["ATGCGTACGTTAGCTAGCTAGGCTAACGTTGACCTAGGCTAACGT","CGTATGGCCTAGGCTTACGATCGTAGCTAGCTTACGGTACCTAGC","TTAACCGGATGCTAGCTAGGCTAACCGTAGGCTTACGATCGTAGC","GCTTAGCGATCGTACCGGATTAACCGGCTAGCTTACGATGCGTAC","ATGCGATTCGACCTAGGCTAACGTAGCTTACCGGATCGTAGCTAACGTAG"]

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

        # Decode it for converting it into a human-readable string
        msg = msg_raw.decode()
        cmd = msg.strip().split(" ",1)
        command = cmd[0]
        if command == "PING":
            response = "OK!"
        elif command == "GET":
            i = cmd[1]
            response = seq_list[int(i)]
        elif command == "INFO":
            seq = Seq(cmd[1])
            count = seq.count()
            response = f"Sequence: {cmd[1]}\nTotal length: {len(cmd[1])}\n"
            for key,value in count.items():
                perc = (value / len(cmd[1])) * 100
                perc = round(perc,2)
                response += f"{key}: {value} ({perc}%)\n"
        elif command == "COMP":
            seq = Seq(cmd[1])
            response = seq.complement()
        elif command == "REV":
            seq = Seq(cmd[1])
            response = seq.reverse()



        color_msg = colored(f"{command} command","green" )
        print(color_msg)
        cs.send(response.encode())
        print(response)
        cs.close()

