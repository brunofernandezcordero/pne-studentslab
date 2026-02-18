from Seq0 import seq_read_fasta
FOLDER = "../sequences/"
FILE = "U5.txt"

if __name__ == "__main__":
    base = seq_read_fasta(FOLDER + FILE)
    print(f"DNA file: {FILE}")
    print("the first 20 bases are:")
    print(base[0:20])

print(len('AAAAAAAAACAAAAATCAACT'))