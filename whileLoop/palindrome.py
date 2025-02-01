""" While loop to check if number is palindrome (eg. 121) """


num = int(input("Enter a number: "))
temp = num
revNum = 0

while temp > 0:
    i = temp % 10
    revNum = (revNum*10)+i
    temp = temp//10

if revNum == num:
    print("Number is palindrome")
else:
    print("Number is not a palindrome")
