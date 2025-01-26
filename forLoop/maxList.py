""" Write a For loop to find the largest number in the list [23,1,45,34,7] """

lst = [23,1,45,34,7]
max = 0
for i in lst:
    if i >= max:
        max = i
print(f'{max} is the largest number in the list.')
