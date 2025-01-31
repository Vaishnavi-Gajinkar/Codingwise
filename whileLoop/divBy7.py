""" Write a while loop to find the first number divisible by 7 greater than 50 """

num = 51

while num > 50:
    if(num % 7 != 0):
        num += 1
    else:
        break

print(f'the first num after 50 which is divisible by 7 is {num}')
