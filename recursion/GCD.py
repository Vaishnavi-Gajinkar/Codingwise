''' calculate the greatest number which divides two numbers completely '''

def gcd(num1, num2):
    if num2 == 0:
        return num1
    print(num1,num2)
    return gcd(num2, num1%num2)

try:
    val1 = int(input("Enter val 1 "))
    val2 = int(input("Enter val 2 "))

    res = gcd(val1,val2)
    print(f"GCD of the entered numbers {val1} and {val2} is {res}")
    
except TypeError:
    print("Incorrect inputs entered ")
