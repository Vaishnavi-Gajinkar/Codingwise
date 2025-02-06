""" Check if a number is between 10 and 50 """


def btwness():
    return 'Number is in range'

def range(tgt, start=0, end=999):               # default parameters
    if tgt >= start and tgt <= end:
        return btwness()                        # defining one function inside another
    else:
        return 'Target not in range'
    
start = int(input('Enter start of range '))
stop = int(input('Enter end of range '))
target = int(input('Enter target value '))

result = range(target, start, stop)
print(result)


