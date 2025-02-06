""" Check if two numbers are equal, greater or less """

def comparator(num1, num2):
    '''Compares 2 numbers'''
    def gt(num1, num2):
        '''check if greater'''
        return num1 > num2
    def eq(num1, num2):
        '''checks equality'''
        return num1==num2
    def lt(num1, num2):
        '''checks if lesser'''
        return num1 < num2
    
    if gt(num1,num2): return 'Num1 is greater than Num2'
    elif eq(num1,num2): return 'Num1 and Num2 are equal'
    elif lt(num1,num2): return 'Num1 is lesser than Num2'

num1 = int(input("Enter 1st number "))
num2 = int(input("Enter 2nd number "))

boo = comparator(num1,num2)
print(boo)