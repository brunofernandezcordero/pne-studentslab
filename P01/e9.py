from Seq1 import Seq
print("\n-----| Practice 1, Exercise 9 |------")
# -- Create a Null sequence
s = Seq()

# -- Initialize the null seq with the given file in fasta format
FILENAME = "U5"
s = Seq(s.read_fasta(FILENAME))

if __name__ == '__main__':
    print(f"Sequence: (Length: {s.len()}) {s}...")
    print(f"    Bases: {s.count()}")
    print(f"    Rev: {s.reverse()}...")
    print(f"    Comp: {s.complement()}...")
