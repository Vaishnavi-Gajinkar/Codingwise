""" While loop to find the largest number in a list [11,42,15,60] """

lst = [11,120,42,15,60]
size = len(lst)
largest = 0
idx = 0
while idx < size:
    if lst[idx] > largest:
        largest = lst[idx]
    idx += 1
print(f'largest element of list is {largest}')
