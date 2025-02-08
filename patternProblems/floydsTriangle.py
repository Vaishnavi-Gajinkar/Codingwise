'''
1
2 3
4 5 6
7 8 9 10
'''

rows = int(input("Enter the numbers of rows you want in this pattern"))
count = 1

for i in range(rows):
    for j in range(i+1):
        print(count,end=" ")
        count += 1
    print()