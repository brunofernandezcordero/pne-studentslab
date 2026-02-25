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
                    self.strbases = "INVALID"
        print(f"{status} sequence created")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)