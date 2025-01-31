""" Write a while loop to print all odd numbers between 1 and 20 """

num = 1

while num <= 20:
    if num % 2 != 0:
        print(num, end=",")
    num += 1

