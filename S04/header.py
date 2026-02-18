from pathlib import Path

FILENAME = "../sequences/RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()

print("First line of the RNU6_269.txt file:")
for line in file_contents.split("\n"):
    if line.startswith(">"):
        print(line)
        break