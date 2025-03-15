''' calculate the result when a number is raised to another number'''

def power(a,b):
    if b == 0:
        return 1
    return a * power(a, b-1)

try:
    base = int(input("Enter base number "))
    pow = int(input("Enter power number "))

    print(f"{base} raised to {pow} is {power(base,pow)}")

except Exception as e:
    print(e)