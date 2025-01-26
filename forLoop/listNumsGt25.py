""" Use a for loop to check if a list contains numbers greater than 25 """

nums = input("Enter list elements seperated by comma: ")
lst = nums.split(",")
flag = 0

for val in lst:
    if int(val) > 25:
        print(val, end=" ")
        flag = 1
if flag == 1:
    print("\nYes the list contains elements greater than 25 ")
else:
    print("All list elements are less than 25 ")