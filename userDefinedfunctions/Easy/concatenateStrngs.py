""" Concatenate two strings in interlocking format"""

def string1(str1):
    '''concatenates two strings in interlocking format'''
    for char in str1:
        yield char

def string2(str2):
    '''concatenates two strings in interlocking format'''
    for char in str2:
        yield char

inp1 = input("Enter 1st string ")
inp2 = input("Enter 2nd string ")

first = string1(inp1)
second = string2(inp2)

total_size = len(inp1) + len(inp2)
complete_word = []

for ch in range(1,total_size+1):
    complete_word.append(next(first))
    complete_word.append(next(second))
    print(str(complete_word))

print(f'Combined complete word in interlocking format is \n{complete_word}')

#  not solved