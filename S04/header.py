from pathlib import Path

FILENAME = "sequences/RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()
for line in file_contents.splitlines():
    if line.startswith(">"):
        print(line)
        break