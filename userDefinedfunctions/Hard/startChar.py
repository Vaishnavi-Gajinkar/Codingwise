'''check if a string starts with a specific character '''

class begining:
    def __init__ (self, word):
        self.word = word

    def strtWth(self,bigi):
        self.bigi = bigi

        if self.word.startswith(self.bigi):
            return True
        else:
            return False
        
ask = input("Enter input word/string/number ")
strt = input("Enter any character ")
obj1 = begining(ask)

result = obj1.strtWth(strt)

if result:
    print("Great. String starts with that char ")
else:
    print("incorrect")