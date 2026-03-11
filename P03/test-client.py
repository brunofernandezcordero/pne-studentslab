from P02.Client0 import Client
from P01.Seq1 import Seq
print(f"-----| Practice 3, Exercise 7 |------")
IP = "212.128.255.84" # your IP address
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)

# PING
print("* Testing PING...")
c.ping()

# GET
print("* Testing GET...")
c.talk("GET 0") # hacerlo con bucle
c.talk("GET 1")
c.talk("GET 2")
c.talk("GET 3")
c.talk("GET 4")

# INFO
print("* Testing INFO...")
c.talk("INFO ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")

# COMP
print("* Testing COMP...")
c.talk("REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")

# GENE
s = Seq()
genes = ["U5","ADA","FRAT1",""]

for gene in genes:
    gene_bases = s.read_fasta(gene)
