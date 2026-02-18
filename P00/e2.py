from Seq0 import seq_read_fasta


FILE = "U5.txt"
read_file = seq_read_fasta(FILE)


print(f"DNA file: {FILE}")
print("the first 20 bases are:")
print(read_file[0:20])
