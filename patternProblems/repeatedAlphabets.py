'''
A
BB
CCC
DDDD
EEEEE
'''

n = int(input("Enter the max rows you need in this pattern "))
letter = ord("A")

for i in range(n):
    for j in range(i+1):
        print(chr(letter),end="")
    print()
    letter += 1