from pathlib import Path

FILENAME = "sequences/ADA.txt"
file_contents = Path(FILENAME).read_text()

body = ""
for line in file_contents.split("\n"):
    if not line.startswith(">"):
        body += line

print("The total number of bases in the ADA.txt head is:", len(body))
