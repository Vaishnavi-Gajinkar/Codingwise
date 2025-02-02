""" Write a while loop to find the factorial of a number """

num = int(input("Enter a number to check its factorial "))
idx = 0
facto = 1

while idx <= num:
    if idx == 0:
        facto *= 1
    else:
        facto *= idx
    idx += 1

print(f'factorial of {num} is {facto}')

