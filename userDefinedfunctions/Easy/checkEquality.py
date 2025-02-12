""" Check if a number is equal to a target value """

def target_checker(vals, target):
    '''Compares target num with all values of list'''
    compare = filter(lambda x:x==target,vals)           # used lambda function
    
    if target in compare:
        print("Target is present in sequence")
    else:
        print("Target is out of sequence")


inp = input("Enter ur numbers seperated by comma ")
nums = inp.split(",")
lst = []
for num in nums:
    lst.append(int(num))

tgt = int(input("Enter target value "))

target_checker(lst, tgt)
