""" While loop to calculate sum of digits of a number (eg. 123 -> 6) """


num = int(input("Enter a number "))
sum = 0
last_fig = 0

print(f'Sum of digits of the number {num} is ',end="")

while num > 0:
    last_fig = num % 10 
    sum += last_fig
    num = num//10
print(sum)