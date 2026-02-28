from Seq1 import Seq
print("\n-----| Practice 1, Exercise 10 |------")
s = Seq()

genes = ["U5","ADA","FRAT1","FXN"]
for gene in genes:
    gene_bases = Seq(s.read_fasta(gene))
    gene_dict = gene_bases.count()
    highest_base = None
    highest_count = float("-inf")  # safe starting value

    for base, count in gene_dict.items():
        if count > highest_count:
            highest_count = count
            highest_base = base
    print(f"Gene {gene}: Most frequente base: {highest_base}")