''' count the number of digits in a number '''

class Digi:
    def __init__(self,num):
        self.num = num
    
    def counnt(self):
        counter = 0
        str_eq = str(self.num)
        for dig in str_eq:
            counter += 1
        print(f'there are {counter} digits in ur number {self.num}')

inp = int(input("Enter a number "))

d = Digi(inp)
d.counnt()