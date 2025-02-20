'''find the absolute difference between two numbers'''

class DiffCalc():

    def absDiff(self, num1, num2):
        self.result = abs(num1-num2)
        return self.result
    
obj1 = DiffCalc()

num1 = int(input("Enter 1st val "))
num2 = int(input("Enter 2nd val "))

res = obj1.absDiff(num1, num2)
print(f'Absolute difference of the above nums is {res}')