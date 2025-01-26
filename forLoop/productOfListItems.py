""" Write a for loop to calculate the product of numbers in a list [1,3,5,7] """

lst = [1,3,5,7]
prod = 1
for val in lst:
    prod *= val
print("Product of all elements of list is",prod)

nums = input("Enter elements of a list seperated by comma ")
lizt = nums.split(',')
flag = 0
prod = 1
for val in lizt:
    if type(val) == "<class 'int'>":
        prod *= int(val)
    else:
        print("Non-numeric list item found")
        flag = 1
        break
if flag == 0:
    print("Product of all elements of list is",prod)
else:
    print("Product cannot be calculated")