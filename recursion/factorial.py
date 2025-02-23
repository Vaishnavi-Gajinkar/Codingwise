''' find the factorial of a number using recursion'''

def facto(num):
    if num == 1:
        return 1
    else:
        return num * facto(num-1)
    
inp = int(input("Enter a number to calc its factorial "))

res = facto(inp)

print(f'Factorial of the number {inp} is {res}')