'''
*****
****
***
**
*
'''
n = int(input('Enter the max number of characters you want in this pattern'))

for i in range(n):
    for j in range(n-i):
        print('*',end="")
    print()
