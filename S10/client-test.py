from P02.Client0 import Client

IP = "212.128.255.98" # your IP address
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
response = c.talk("Testing!!")
print(f"Response: \n{response}")