from P02.Client0 import Client

IP = "212.128.255.98" # your IP address
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print("Sending a message to the server")
for i in range(5):

    print(f"To Server: Message {i}")
    response = c.talk(f"Message {i}")

    print(f"From Server: {response}")
