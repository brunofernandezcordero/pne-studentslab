from Seq0 import seq_read_fasta,seq_len

genes = ["U5","ADA","FRAT1","FXN"]
FOLDER = "../sequences/"

if __name__ == "__main__":
    print("-----| Exercise 3 |-----")
    for gene in genes:
        gene_seq= seq_read_fasta(FOLDER + gene +".txt")
        print(f"Gene {gene} -> Length: {seq_len(gene_seq)}")
