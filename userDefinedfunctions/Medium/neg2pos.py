'''convert a number to a positive value'''

def negToPos(num):
    if num < 0:
        return abs(num)
    return num

try:
    val = 0

    while val != 'q':
        val = int(input("Enter a positive/negative number (type q to quit) "))
        print("Absolute value of this number is", negToPos(val))

except:
    print("program ended successfully")

'''
OUTPUT:
Enter a positive/negative number (type q to quit) 321654987
Absolute value of this number is 321654987
Enter a positive/negative number (type q to quit) 0
Absolute value of this number is 0
Enter a positive/negative number (type q to quit) -789456132
Absolute value of this number is 789456132
Enter a positive/negative number (type q to quit) q
program ended successfully
'''