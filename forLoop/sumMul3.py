""" Write a For loop to calculate the sum of all numbers divisible by 3 in the range 1-50"""

sum = 0
for num in range(1,51):
    if num % 3 == 0:
        sum += num
        print(num,end=", ")
print("\nThe sum of all numbers divisible by 3 is",sum)
