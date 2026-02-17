from pathlib import Path

FILENAME = "sequences/ADA_EXONS.txt"
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

# Ahora tengo la lista exons con cada base sequence de cada exon en order

max_cord = 44652852
exon_number = 0
print(f"{'Exon'}     | {'Long.'}     | {'Start'}     |{'End:'}")
print('-'*50)
for exon in exons:
    exon_number += 1
    start_index = complete_ADA.find(exon)
    if start_index == -1:
        print(f"Exon {exon_number} not found!")
        continue
         # Me sale que ninguno es encontrado en el ADA compelto. Lo he comprobado manualmente y tampoco me encuentra los primeros exons
    length = len(exon)

    start_coord = max_cord - start_index
    end_coord = start_coord - (length -1 )
    print(f"{exon_number}     | {length}     | {start_coord}     | {end_coord}      ")



