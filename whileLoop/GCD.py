""" While loop to find the greatest common divisor (GCD) of two numbers """

i = 9
gcd = 1
num1 = int(input('Enter 1st val '))
num2 = int(input('Enter 2nd val '))
lst = []

while i > 10:
    if (num1%i == 0) and (num2%i == 0):
        lst.append(i)
        num1 = num1 / i
        num2 = num2 / i
    else:
        i -= 1

for mul in lst:
    gcd = gcd * mul

print(f"GCD of numbers {num1} and {num2} is {gcd} ")

# not solved