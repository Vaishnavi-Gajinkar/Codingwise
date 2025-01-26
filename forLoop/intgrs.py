""" Print all integers from 1 to 10 using for loop """

for num2 in range(1,11,1):                      #hard coding the value
    print(num2)

strt = int(input("Enter start val: "))          #taking values from user
stop = int(input("Enter stop val: "))
for num in range(strt, stop+1):
    print(num)