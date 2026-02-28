from pathlib import Path
class Seq:
    def __init__(self,strbases=None):
        self.strbases = strbases
        bases = ["A", "C", "G", "T"]
        if not self.strbases:
            status = "Null"
            self.strbases = "NULL"
        else:
            for i in self.strbases:
                if i in bases:
                    status = "Valid"
                else:
                    status = "Invalid"
                    self.strbases = "ERROR"
        print(f"{status} sequence created")

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return len(self.strbases)

    def count_base(self,base):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            count = 0
        else:
            count = self.strbases.count(base)
        return count

    def count(self):
            gene_dict = ["A","C","T","G"]
            d = {}
            for bases in gene_dict:
                d[bases] = self.strbases.count(bases)
            return d

    def reverse(self):
        if self.strbases == "NULL":
            reverse = "NULL"
        elif self.strbases == "ERROR":
            reverse = "ERROR"
        else:
            reverse = self.strbases[::-1]
        return reverse

    def complement(self):
        comp = ""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            comp = "ERROR"
        else:
            for i in self.strbases:
                if i == "A":
                    comp += "T"
                elif i == "T":
                    comp += "A"
                elif i == "C":
                    comp += "G"
                elif i == "G":
                    comp += "C"
        return comp

    def read_fasta(self,FILENAME):
        FILENAME = "../sequences/" + FILENAME + ".txt"
        file_contents = Path(FILENAME).read_text()
        body = ""
        for line in file_contents.split("\n"):
            if not line.startswith(">"):
                body += line
        return body

