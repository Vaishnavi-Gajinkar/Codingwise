'''check if a number is a multiple of 7 but not 11'''
from functools import reduce

def not7but11(nums):
    '''returns the numbers in list which are divisible by 7 but not by 11'''
    arr = filter(lambda x:(x%7==0)and(x%11!=0),nums)
    return arr

lst = [int(num) for num in input("Enter numbers seperated by comma").split(",")]
print("Below numbers of list are divisible by 7 but not by 11")
print(list(not7but11(lst)))