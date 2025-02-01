""" While loop to generate and print all Armstrong numbers between 1 & 1000 """


till = 1000
i = 1

print('Armstrong numbers between 1 - 1000 are')

while i <= till:
    num = i
    sum = 0
    while num > 0:
        last_dgt = num % 10
        sum += (last_dgt ** 3)        
        num = num // 10
    if sum == i:
        print(i, end=",")
    i += 1
