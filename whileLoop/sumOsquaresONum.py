""" While loop to calculate the sum of squares of numbers from 1 to 20 """

stop = int(input("Enter stop value "))
counter = 1
sum = 0

while counter <= stop:
    sum += (counter**2)
    counter += 1
    
print(f'Sum of Squares of all values between 1 and {stop} is {sum}')