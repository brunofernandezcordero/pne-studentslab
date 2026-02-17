from pathlib import Path

FILENAME = "sequences/ADA_EXONS.txt"
file_contents = Path(FILENAME).read_text()

exon_file_split = file_contents.split("\n")
exons = []
for line in exon_file_split:
    exon_base = ""
    if line.startswith(">"):
        exons.append(exon_base)
        continue
    else:
        exon_base+=line
        # Aqui no se porque las bases  se me unen linea  alinea y no por exons
print(exons)