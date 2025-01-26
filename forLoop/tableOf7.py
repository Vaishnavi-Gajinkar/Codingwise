""" Use a for loop to print the multiplication table of 7 upto 10 times """ 

for j in range(1,11):
    # for j in range(1,11):
    print(f'7 * {j} = {7*j}')

mul = int(input("\nEnter the number for which you want to see a table: "))
print('Multiplication table for ',mul)
for i in range(1,11):
    print(f'{mul}*{i}={mul*i}')