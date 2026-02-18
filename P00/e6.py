from Seq0 import *
FOLDER = "../sequences/"
gene = "U5"

if __name__ == "__main__":
    base = seq_read_fasta(FOLDER + gene + ".txt")
    fragment, reverse = seq_reverse(base,20)
    print("-----| Exercise 6 |-----")
    print(f"Gene {gene}")
    print(f"Fragment: {fragment}")
    print(f"Reverse: {reverse}")