'''
ABCDE
ABCD
ABC
AB
A
'''
n = int(input("Enter number of lines "))

for i in range(n):
    var = 65
    for j in range(n-i):
        print(chr(var),end="")
        var += 1
    print()
