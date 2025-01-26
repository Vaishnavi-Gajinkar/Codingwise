""" Write a for loop to print all even numbers between 1 & 20 """

for num in range(1,21):                 # checking even by remainder value
    if num % 2 == 0:
        print(num,end=" ")
print(type(num))

for val in range(2,21,2):               # incrementing for value in steps of 2
    print(val, end=" ")


