from Seq0 import *

genes = ["U5","ADA","FRAT1","FXN"]
FOLDER = "../sequences/"

if __name__ == "__main__":
    print("-----| Exercise 4 |-----")
    for gene in genes:
        gene_seq = seq_read_fasta(FOLDER + gene + ".txt")
        print(f"\nGene {gene}")
        print(f"   A: {seq_count_base(gene_seq,"A")}")
        print(f"   C: {seq_count_base(gene_seq, "C")}")
        print(f"   T: {seq_count_base(gene_seq, "T")}")
        print(f"   G: {seq_count_base(gene_seq, "G")}")