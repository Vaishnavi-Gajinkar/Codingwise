''' find the factorial of a number using recursion'''

def facto(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * facto(num-1)
    
inp = int(input("How many elements' factorial would you want to see in sequence ? "))

for i in range(inp+1):
    print(f'Factorial of {i} is {facto(i)}')