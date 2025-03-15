'''
1
12
123
1234

'''

counter = 1
val = int(input("Enter max number of rows req in this pattern "))
for i in range(val):
    for j in range(i+1):
        print(counter,end="")
        counter += 1
    print()
    counter = 1


