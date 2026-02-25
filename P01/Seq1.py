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
            count = 0
            for i in base:
                if i.upper() == base:
                    count += 1
        return count