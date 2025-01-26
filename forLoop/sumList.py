""" Write a for loop to calculate the sum of the numbers [1,2,3,4,5] """

lst = [1,2,3,4,5]                                                   # defining explicit array values
sum = 0
for item in lst:
    sum = sum + item
print("Sum of list is",sum)

size = int(input("Enter count of elements to be entered "))         # accepting size of array that will be entered
print("Enter numeric elements in array to add-up.")
lzt = []
sum = 0
for i in range(size):
    lzt.append(int(input()))                                        # accepting the values from user
for val in lzt:
    sum += val
print(f'Sum of entered array values is {sum}')