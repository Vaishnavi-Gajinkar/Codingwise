""" Write a For loop to count how many elements in list are greater than 2.0 """

lst = [1.5,2.3,3.1,4.0]
cnt = 0
for val in lst:
    if val > 2.0:
        cnt += 1
print(f'{cnt} values in list are greater than 2.0 ')