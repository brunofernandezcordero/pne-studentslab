from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.98" # your IP address
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print("Sending a message to the server")
for i in range(5):
    print(f"Message {i}")
    response = c.talk(f"Message {i}")

    print(f"From Server: \n{response}")

