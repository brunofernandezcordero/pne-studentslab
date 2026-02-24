class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        self.strbases = strbases
        bases = ["A","C","G","T"]
        for i in self.strbases:
            if i in bases:
                base = True
            else:
                base = False
        if base:
            print("New sequence created!")
        else:
            print("INCORRECT sequence detected!")
            self.strbases = "ERROR!"

    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


def print_seqs(seq_list):
    j = 0
    for i in seq_list:
        print(f"Sequence {j}: (Length: {i.len()}) {i}")
        j += 1

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print(print_seqs(seq_list))