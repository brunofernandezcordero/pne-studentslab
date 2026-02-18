file_contents = Path(FILENAME).read_text()

FILENAME2 = "sequences/ADA.txt"
complete_ADA = Path(FILENAME2).read_text()

body = ""
for line in complete_ADA.split("\n"):
    if not line.startswith(">"):
        body += line + "\n"

complete_ADA = body

exon_file_split = file_contents.split("\n")
exons = []
exon_base = ''
for line in exon_file_split:
    if line.startswith(">"):
        if exon_base:
            exons.append(exon_base)
            exon_base = ''
        continue
    else:
        exon_base += line

if exon_base:
    exons.append(exon_base)