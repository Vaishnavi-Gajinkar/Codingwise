""" Write a while loop to calculate the sum of numbers from 1 to 10 """

nums = 1
sum = 0

while nums <= 10:
    sum += nums
    if nums < 10 and sum < 10:
        print(f'Sum till 0{nums} is 0{sum}')
    elif nums < 10:
        print(f'Sum till 0{nums} is {sum}')
    else:
        print(f'Sum till {nums} is {sum}')
    nums += 1
