'''check if sum of two numbers is greater than 50'''

import numpy as np 

def sumChecker(*args):
    ''' calcs sum of all entered numbers '''
    sum = 0
    nums = np.array(args[0], dtype="int")
        
    return np.sum(nums)


try:
    vals = input("Enter multiple numbers (space seperated) ").split(" ")
    res = sumChecker(vals)
    if res > 50:
        print("Sum of all numbers is", res,"which is greater than 50")
    else:
        print("Sum of numbers is",res, "and it does not exceed 50")
except:
    print("Some error occured. Pleej try again.")

'''
OUTPUT: 
Enter multiple numbers (space seperated) 1 2 3 4 5
Sum of numbers does not exceed 50
-------------------------------------------------------------------
Enter multiple numbers (space seperated) 10 20 30 40 50
Sum of all numbers is 150 which is greater than 50
-------------------------------------------------------------------
Enter multiple numbers (space seperated) 1 2 3 a
Some error occured. Pleej try again.
'''