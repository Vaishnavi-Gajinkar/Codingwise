'''check if two numbers are opposite in signs (pos/neg)'''
import random

def signCheck(num1,num2):
    if num1 < 0 and num2 < 0:
        print("Numbers have same signs")
    elif num1 > 0 and num2 > 0:
        print("Numbers have same signs")
    elif num1 < 0 and num2 > 0:
        print("Numbers differ in their sign")
    elif num1 > 0 and num2 < 0:
        print("Numbers differ in their sign")
    else:
        print("Eiter of the numbers are neutral. No sign to compare")

# neg = float("inf")
# pos = float("inf")

val1 = random.choice(range(-500,500))
val2 = random.choice(range(-500,500))

res = signCheck(val1, val2)
print(f"{val1} and {val2} were the randomly generated numbers ")

'''
OUTPUT:
Numbers have same signs
484 and 496 were the randomly generated numbers 
--------------------------------------------------------------------------------------------
Numbers differ in their sign
-388 and 83 were the randomly generated numbers 
--------------------------------------------------------------------------------------------
Numbers have same signs
-341 and -180 were the randomly generated numbers 
--------------------------------------------------------------------------------------------

'''