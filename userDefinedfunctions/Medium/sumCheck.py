'''check if sum of two numbers is greater than 50'''

def sumChecker(*args):
    ''' calcs sum of all entered numbers '''
    sum = 0
    nums = args[0]
        
    return sum(nums)


vals = input("Enter multiple numbers (space seperated) ").split(" ")
res = sumChecker(vals)
print("Sum of all numbers is", res)

# not solved