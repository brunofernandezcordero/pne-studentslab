from pathlib import Path

FILENAME = "../sequences/U5.txt"
file_contents = Path(FILENAME).read_text()

body = ""
for line in file_contents.split("\n"):
    if not line.startswith(">"):
        body += line + "\n"

print("Body of the U5.txt file:")
print(body)
