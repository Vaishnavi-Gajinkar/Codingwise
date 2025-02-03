""" Check if number is positive or negative """

def checkPosNeg(num):
    ''' Checks parity of entered number'''
    if num > 0:
        return 'Positive'
    elif num < 0:
        return 'Negative'
    else:
        return 'Neutral'

inp = int(input("Enter any number"))
res = checkPosNeg(inp)                      # assigning function to a variable
print("The entered number is",res)