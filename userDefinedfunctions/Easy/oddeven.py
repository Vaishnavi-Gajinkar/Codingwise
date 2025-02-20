""" Check if a number is odd or even """

class OddEve():
    def odd(self):
        return f'Number is odd'
    
    def even(self):
        return f'Number is even'


call = OddEve()
try:
    num = int(input("Enter a number "))
    if num % 2 != 0:
        print(call.odd())
    else:
        print(call.even())
except:
    print("Invalid number! Pls try again.")
finally:
    print("Program ended successfully")