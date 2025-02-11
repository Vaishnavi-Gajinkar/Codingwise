""" Add nums given by user """

from functools import reduce

def add_nums(nums_list):
    '''Adds the numbers of list using reduce function'''
    numbers = nums_list
    sum = reduce(lambda x,y : x+y , numbers)

    print(f'Sum of all entered numbers is {sum}')

inp = input("Enter ur numbers seperated by comma ")
nums = inp.split(",")
lst = []
for num in nums:
    lst.append(int(num))

add_nums(lst)