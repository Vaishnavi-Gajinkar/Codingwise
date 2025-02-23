''' Find the sum of digits of a number using recursion '''


def addition(num):
    # total = 0
    if num == 0:
        return 0
    else:
        return num%10 + addition(num//10)

n = 12345
print(addition(n))