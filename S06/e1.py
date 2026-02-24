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
            print("ERROR!")
            self.strbases = "ERROR"



    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


# --- Main program
s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")

