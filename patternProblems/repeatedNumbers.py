'''
1
22
333
4444
55555
'''

counter = 1
rows = int(input("Enter the max number of rows needed in this pattern "))

for i in range(rows):
    for j in range(i+1):
        print(counter,end="")
    counter += 1
    print()