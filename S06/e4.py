
class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        self.strbases = strbases

    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

def generate_seqs(pattern,n):
    seq_list = []
    for i in range(1,n+1):
        seq_list.append(Seq(pattern * i ))
    return seq_list

from termcolor import colored

def print_seqs(seq_list, color):
    for j, i in enumerate(seq_list):
        text = f"Sequence {j}: (Length: {i.len()}) {i}"
        print(colored(text, color,attrs=['reverse']))

seq_list1 = (generate_seqs("A", 3))
seq_list2 = (generate_seqs("AC", 5))

print("List 1:")
print_seqs(seq_list1,'blue')

print()
print("List 2:")
print_seqs(seq_list2,'red')
