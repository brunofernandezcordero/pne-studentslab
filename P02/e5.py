from P01.Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.1.39" # your IP address
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)
s = Seq()
FRAT1_bases = s.read_fasta("FRAT1")
importing = c.talk("Sending FRAT1 to the server, in fragments of 10 bases...")
print("Sending FRAT1 to the server, in fragments of 10 bases...")
for j in range(5):
    start = j * 10
    end = start + 10
    fragment = FRAT1_bases[start:end]
    print(f"Fragment {j + 1}: {fragment}")
    send_fragment = c.talk(f"Fragment {j + 1}: {fragment}")