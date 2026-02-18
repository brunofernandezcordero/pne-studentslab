from Seq0 import *

genes = ["U5","ADA","FRAT1","FXN"]
FOLDER = "../sequences/"

if __name__ == "__main__":
    print("-----| Exercise 8 |-----")
    for gene in genes:
        gene_seq = seq_read_fasta(FOLDER + gene + ".txt")
        dict_bases = seq_count(gene_seq)
        for base,count in dict_bases.items():
