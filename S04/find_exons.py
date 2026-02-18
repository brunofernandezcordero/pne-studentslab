from pathlib import Path

FILENAME = "../sequences/ADA_EXONS.txt"
file_contents = Path(FILENAME).read_text() # file contents con todos los exons

FILENAME2 = "../sequences/ADA.txt"
complete_ADA = Path(FILENAME2).read_text()

body = ""
for line in complete_ADA.split("\n"):
    line.replace(" ","")
    if not line.startswith(">"):
        body += line
complete_ADA = body
#Ahora tengo la secuencia del gen ADA completo, sin saltos de linea ni espacios


exon_file_split = file_contents.split("\n")
exons = []
exon_base = ''
for line in exon_file_split:
    if line.startswith(">"):
        if exon_base: # Añado los exons conseguidos antes de empezar a mirar el siguiente
            exons.append(exon_base)
            exon_base = ''
        continue
    else:
        exon_base += line

if exon_base:
        exons.append(exon_base)
#Para el ultimo addition ya que no hay un > despues y no entraria al primer if



max_cord = 44652852 #posicion inicial (reversa)
exon_number = 0
print(f" {'Exon'}          | {'Long.'}          | {'Start'}          |{'End:'}          ")
print('-'*50)
for exon in exons:
    exon_number += 1
    start_index = complete_ADA.find(exon)
    length = len(exon)
    start_coord = max_cord - start_index
    end_coord = start_coord - (length -1 )
    print(f" {exon_number}          | {length}          | {start_coord}        | {end_coord}          ")
# Confusion on start and end coordinate



