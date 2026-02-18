from Seq0 import seq_read_fasta
FOLDER = "../sequences/"
FILE = "U5.txt"
filename = FOLDER + FILE
base = seq_read_fasta(filename)


print(f"DNA file: {FILE}")
print("the first 20 bases are:")
print(base[0:20])
