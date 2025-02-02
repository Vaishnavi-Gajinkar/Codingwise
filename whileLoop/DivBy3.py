""" while loop to count how many numbers in a list [] are divisible by 3 """

lst = list(range(50))
idx = 1
counter = 0
div3 = []

while idx < len(lst):
    if lst[idx] % 3 == 0:
        counter += 1
        div3.append(lst[idx])
    idx += 1

print(f'The below {counter} elements of list are divisible by 3 \n {div3}')
