'''
*         *
**       **
***     ***
****   ****
***** *****
***** *****
****   ****
***     ***
**       **
*         *
'''

rows = int(input("Enter the max rows you need in this pattern "))
n = rows

for i in range(rows):
    if i < n/2:
        for j in range(i+1):
            print("*",end="")
        for k in range((n//2-j)*2):
            print(" ",end="")
        for l in range(i+1):
            print("*",end="")
        print()
    else:
        for j in range(n-i):
            print("*",end="")
        for k in range((n//2-j)*2):
            print(" ",end="")
        for l in range(n-i):
            print("*",end="")
        print()
