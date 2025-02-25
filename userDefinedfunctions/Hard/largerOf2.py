'''find the larger of two numbers without using IF '''

def sort(nums):
    lst = list(sorted(nums))
    return lst[0], lst[-1]


inp = input("Enter your numbers (seperated by a space) ")
nums = inp.split(" ")
numeric_lst = [int(x) for x in nums]          # list comprehension to convert str elements of list to int
smallest, largest = sort(numeric_lst)

print(f'Smallest num of list is {smallest}\nLargest num of list is {largest}')