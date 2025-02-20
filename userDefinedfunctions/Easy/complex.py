""" Add two complex values """

class Add():
    def seperate(self,complex):
        self.number = complex.split("+")

    def real(self,*args):
        self.val = sum(args)
        return self.val
    
    def img(self,*imgrys):
        self.imgaginary = sum(imgrys)
        return self.imgaginary
    
obj = Add()

num1 = input("Enter 1st complex num (in a+jb format) ")
num2 = input("Enter 2nd complex num (in a+jb format) ")

number1 = (num1.split('+')) or (num1.split('-'))
number2 = (num2.split('+')) or (num2.split('-'))

print(number1, number2)

# not solved 