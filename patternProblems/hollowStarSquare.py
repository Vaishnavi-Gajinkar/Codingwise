'''
* * * *
*     *
*     *
* * * *
'''
side = int(input("Enter the number of chars on edge of the square "))

for i in range(side):
    for j in range(side):
        if i == 0 or i == side-1:
            print("* ",end="")
        if j == 0 or j == side-1:
            print("*")
    print()

# not solved