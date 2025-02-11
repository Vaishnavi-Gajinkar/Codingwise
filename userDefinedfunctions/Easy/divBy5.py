""" Check if a number is divisible by 5 """

def divBy5(num_list):
    ''' Returns all numbers divisible by 5 '''
    numbers = filter(lambda x:x%5==0, num_list)
    print(list(numbers))

inp = input("Enter ur numbers seperated by comma ")
nums = inp.split(",")
lst = []
for num in nums:
    lst.append(int(num))

divBy5(lst)
