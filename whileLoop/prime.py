""" While loop to find all prime numbers between 1 and 50"""


strt = 1
stop = 50
lst = []

while strt <= stop:
    num = strt
    i = 1
    while i <= num:
        if num % i == 0:
            if i != 1 and i != num:
                lst.append(num)
                break
            else:
        i += 1
    strt += 1
print(f"Prime numbers between {strt} and {stop} are",lst)