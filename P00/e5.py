from Seq0 import *
genes = ["U5","ADA","FRAT1","FXN"]
FOLDER = "../sequences/"

if __name__ == "__main__":
    print("-----| Exercise 5 |-----")
    for gene in genes:
        gene_seq = seq_read_fasta(FOLDER + gene + ".txt")
        print(f"Gene {gene}: {seq_count(gene_seq)}")