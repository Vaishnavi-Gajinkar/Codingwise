""" Find the largest of two numbers """

arr = input("Enter all your numbers seperated by comma ")

lst = [int(x) for x in arr.split(",")]                      # list comprehension

large = 0

for val in lst:
    if val > large:
        large = val

print("largest element of the list is ",large)