'''find the sum of the digits of a 3 digit number'''

from functools import reduce

def numToList(num):
    '''breaks down the number and converts it to integer list '''
    number = num
    lst = []
    for val in range(len(str(num))):
        lst.append(int(number%10))
        number /= 10
    print(lst)
    return lst

def addishan(num):
    '''adding the digits of a number'''
    lizt = numToList(num)
    zum = reduce(lambda x,y : x+y, lizt)
    return zum

num = int(input("Enter a number to calculate sum of its digits "))

result = addishan(num)
print(f'Sum of digits of the number {num} is {result}')