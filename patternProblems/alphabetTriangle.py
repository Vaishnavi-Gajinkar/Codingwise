'''
A
AB
ABC
ABCD
ABCDE
'''
print(chr(65))

strt = 65
stop = input("Enter last character you wish to see in this pattern")
end = ord(stop)

for i in range(strt, end+1):
    for j in range(i,end-i):
        print(chr(i),end="")
    print()

# not solved