""" 
[1,2,3,4,5] 
take input from user and match with computer's choice
"""

import random
numlizt = [1,2,3,4,5]
userNum = int(input('Enter a number from 1-5'))
compNum = random.choice(numlizt)

if numlizt == compNum:
    print("Number Matches")

elif numlizt != compNum:
    print("Try again")

else:
    print("Invalid input")