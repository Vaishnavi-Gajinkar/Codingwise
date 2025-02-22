'''find the average of three numbers '''

from functools import reduce


def averg(tup):
    size = len(tup)
    total = reduce(lambda x,y : x+y , tup)                  # advance function
    return total/size

lst = [int(num) for num in input("Enter the numbers seperated by comma ").split(',')]

print(f'Average of all these numbers is {averg(lst)}')
