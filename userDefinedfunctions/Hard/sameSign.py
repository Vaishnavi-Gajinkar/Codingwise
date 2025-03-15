'''check if two numbers have the same sign '''

class signCheck:
    # def __init__(self, num1, num2):
            
    def negSplit(self, num):
        self.num = abs(int(num))
        return (0-self.num)

    def negpos(self,num1,num2):
        self.num1 = int(num1)
        self.num2 = int(num2)

        if abs(self.num1) == abs(self.num2):
            if self.num1 > 0 and self.num2 > 0:
                return print('Numbers have same sign')
            elif self.num1 > 0 and self.num2 < 0:
                return print('Numbers are different in sign')
            elif self.num1 < 0 and self.num2 > 0:
                return print('Numbers differ in sign')
        else:
            return print('Numbers are entirely different')
        
try:
    val1 = input("Enter 1st val ")
    val2 = input("Enter 2nd val ")
    
    val1_sign = val1
    val2_sign = val2
    obj1 = signCheck()

    if val1.startswith("-"):
        val1_sign = obj1.negSplit(val1)
    if val2.startswith("-"):
        val2_sign = obj1.negSplit(val2)
    
    obj1.negpos(val1_sign,val2_sign)

except Exception as e:
    print(e)

