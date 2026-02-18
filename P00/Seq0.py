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

def seq_count_bases(seq,base):
