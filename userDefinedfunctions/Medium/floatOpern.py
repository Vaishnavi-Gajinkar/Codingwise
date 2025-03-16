'''two floating point numbers calculator with decimal accuracy'''


class MulDiv:
    def __init__(self, num1, num2, accuracy):
        self.a = num1
        self.b = num2
        self.acurcy = accuracy

    def addi(self):
        return self.a + self.b

    def subs(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b
    
    def divi(self):
        return self.a / self.b

val1 = float(input("val1 "))
val2 = float(input("val2 "))
accr = int(input("what decimal accuracy would you like the result till? "))

obj = MulDiv(val1, val2, accr)
add_res = obj.addi()
sub_res = obj.subs()
mul_res = obj.mult()
div_res = obj.divi()

print(f'''\nAddition of the two numbers with {accr} decimal accuracy is {round(add_res,accr)}
Subtraction of the two numbers with {accr} decimal accuracy is {sub_res:.{accr}f}
Multiplication of the two numbers with {accr} decimal accuracy is {mul_res:.{accr}f}
Division of the two numbers with {accr} decimal accuracy is {round(div_res,accr)}   \n''')