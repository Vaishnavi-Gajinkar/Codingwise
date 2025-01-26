""" Use a For loop to find the factorial of a number (eg.5!) """

num = int(input("Enter a number: "))
mul = 1
if num > 0:
    for i in range(num, 0,-1):
        mul *= i
    print(f'Factorial of {num} is {mul}')
elif num < 0:
    val = abs(num)
    for j in range(val, 0, -1):
        mul *= j
    print(f"Factorial of {num} is -{mul}")
else:
    print("Factorial of 0 is 1.")