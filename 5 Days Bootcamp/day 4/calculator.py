""" Simple Calculator """

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
oprtr = int(input(""" Please enter the number corresponding to the operation you want to perform.
                  1. Addition
                  2. Subtraction
                  3. Multiplication
                  4. Division
                """))

if oprtr == 1:
    print(num1+num2)
elif oprtr == 2:
    print(num1-num2)
elif oprtr == 3:
    print(num1*num2)
elif oprtr == 4:
    print(num1/num2)
else:
    print("Invalid Input")    