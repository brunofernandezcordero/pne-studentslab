from P02.Client0 import Client
from P01.Seq1 import Seq
print(f"-----| Practice 3, Exercise 7 |------")
IP = "192.168.1.39" # your IP address
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)

# PING
print("\n* Testing PING...")
c.ping()

# GET
print("\n* Testing GET...")
for i in range(5):
    response = c.talk(f"GET {i}")
    print(f"GET {i}: {response}")

# INFO
print("\n* Testing INFO...")
response = c.talk("INFO ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
print(response)

# COMP
seq = "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"
print("* Testing COMP...")
print(f"COMP {seq}")
response = c.talk(f"COMP {seq}")
print(response)

# REV
print("\n* Testing REV...")
print(f"REV {seq}")
response = c.talk(f"REV {seq}")
print(response)

# GENE
print("\n* Testing GENE")
s = Seq()
genes = ["U5","ADA","FRAT1","FXN",'RNU6_269P']
for gene in genes:
    response = c.talk(f'Get {gene}')
    print(f'{gene}: {response}')

