''' '''

def tribonacci(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

for i in range(10):
    print(tribonacci(i),end=" ")