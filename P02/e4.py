from P01.Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.98" # your IP address
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)
print(c)
s = Seq()
genes = ["U5","ADA","FRAT1"]
for gene in genes:
    gene_bases = Seq(s.read_fasta(gene))
    importing = c.talk(f"Sending {gene} to the server...")
    print(f"To Server: {importing}")
    send_bases = c.talk(str(gene_bases))
    print(f"To Server: {send_bases}")