from Seq0 import *

FOLDER = "../sequences/"
gene = "U5"

if __name__ == "__main__":
    base = seq_read_fasta(FOLDER + gene + ".txt")
    print("-----| Exercise 7 |-----")
    print(f"Gene {gene}")
    print(f"Frag: {base[0:21]}")
    print(f"Comp: {seq_complement(base[0:21])}")

