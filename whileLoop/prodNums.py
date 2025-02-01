""" Write a while loop to calculate the product of numbers in the list [2,4,6] """


lst = [2,4,6]
prod = 1
num = 0

while num < len(lst):
    prod *= lst[num]
    num += 1

print(f'Product of all elements of the list is {prod}')

# -------- Alternate way-------------- #
# i = 1
# product = [result for num in lst i*num]