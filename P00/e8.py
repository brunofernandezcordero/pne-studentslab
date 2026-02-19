from Seq0 import *

genes = ["U5","ADA","FRAT1","FXN"]
FOLDER = "../sequences/"

if __name__ == "__main__":
    print("-----| Exercise 8 |-----")
    for gene in genes:
        gene_seq = seq_read_fasta(FOLDER + gene + ".txt")
        dict_bases = seq_count(gene_seq)
        max_base = ""
        max_base_count = 0
        for base,count in dict_bases.items():
            if count >= max_base_count:
                max_base = base


        print(f"Gene {gene}: Most Frequent base: {max_base}")

