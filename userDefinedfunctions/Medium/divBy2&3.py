'''check if a number is divisible by both 2 & 3 '''

class divCheck:

    def __init__(self,num):
        self.number = num

    def divBy2(self):
        return self.number % 2 == 0

    def divBy3(self):
        return self.number % 3 == 0

    
try:
    val = int(input("Enter a number to check divisibility "))

    dc = divCheck(val)

    if dc.divBy2() and dc.divBy3():
        print("Number is divisible by both 2 & 3")
    elif dc.divBy2():
        print("Number is divisible by 2 only")
    elif dc.divBy3():
        print("Number is divisible by 3 only")
    else:
        print("Number is neither divisible by 2 nor 3")
except:
    print("Some error occured. Please try again.")