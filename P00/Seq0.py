def seq_ping():
    return "OK"

def seq_read_fasta(filename):
    from pathlib import Path
    file_contents = Path(filename).read_text()
    body = ""
    for line in file_contents.split("\n"):
        if not line.startswith(">"):
            body += line
    return body

def seq_len(seq):
    return len(seq)

def seq_count_base(seq,base):
    base_count = 0
    for i in seq:
        if i.upper() == base:
            base_count += 1
    return base_count

def seq_count(seq):
    gene_dict = {}
    for i in seq:
        if i not in gene_dict.keys():
            gene_dict[i] = 1
        else:
            gene_dict[i] += 1
    return gene_dict

def seq_reverse(seq,n):
    for i in range(n):
        fragment  = seq[0: (n + 1)]
        reverse = fragment[::-1]
    return fragment, reverse

def seq_complement(seq):
    comp = ""
    for i in seq:
        if i == "A":
            comp += "T"
        elif i == "T":
            comp += "A"
        elif i == "C":
            comp += "G"
        elif i == "G":
            comp += "C"
    return comp