'''
54321
4321
321
21
1
'''
n = int(input("Enter number of rows "))
decrmt = n

for i in range(n):
    decrmt = n - i
    for j in range(n-i):
        print(decrmt,end="")
        decrmt -= 1
    decrmt = n
    print()
