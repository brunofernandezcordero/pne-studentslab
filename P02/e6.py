from P01.Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.98" # your IP address
PORT1 = 8080
PORT2 = 8081

# -- Create a client object
c1 = Client(IP, PORT1)
print(c1)
c2 = Client(IP,PORT2)
s = Seq()
FRAT1_bases = s.read_fasta("FRAT1")
importing1 = c1.talk("Sending FRAT1 to the server, in fragments of 10 bases...")
importing2 = c2.talk("Sending FRAT1 to the server, in fragments of 10 bases...")
print("Sending FRAT1 to the server, in fragments of 10 bases...")
for j in range(10):
    start = j * 10
    end = start + 10
    fragment = FRAT1_bases[start:end]
    print(f"Fragment {j + 1}: {fragment}")
    if (j +1) % 2 != 0:
        send_fragment = c1.talk(f"Fragment {j + 1}: {fragment}")
    else:
        send_fragment = c2.talk(f"Fragment {j + 1}: {fragment}")