""" Use a for loop to print numbers from 1 to 100, but skip numbers divisible by both 3 & 5"""

for i in range(1,101):
    if i%3==0 or i%5==0:
        continue
    else:
        print(i, end=", ")

