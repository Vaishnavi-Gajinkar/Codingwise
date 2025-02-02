""" While loop to print numbers from 1 to 100 but skip numbers divisible by both 2 & 3 """

strt = 1
stop = 100
i = 1
print(f"Numbers between {strt} and {stop} which aren't divisible by both 2 and 3 are as below ")
while i <= stop:
    if i % 2 != 0 and i % 3 != 0:
        print(i, end=",")
    i += 1