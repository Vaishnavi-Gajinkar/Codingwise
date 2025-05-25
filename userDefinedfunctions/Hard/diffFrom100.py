'''calculate the difference between a number and 100, if the number is greater than 100'''

import random

def diffCalc(num):
    if num < 100:
        return 100-num
    else:
        return abs(num-100)
    
val = random.choice(range(1,200))
res = diffCalc(val)
print(f"Difference of number {val} from 100 is {res}")

'''
OUTPUT:
Difference of number 112 from 100 is 12
-------------------------------------------------------------------------------------------------
Difference of number 62 from 100 is 38
-------------------------------------------------------------------------------------------------
Difference of number 181 from 100 is 81
-------------------------------------------------------------------------------------------------
Difference of number 20 from 100 is 80
'''