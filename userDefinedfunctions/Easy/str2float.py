""" Convert a string to a float """

# print(ord('A'))
# print(chr(49))

def stringChecker(val):
    '''checks if the input string is made up of numbers or letters'''
    for ch in val:
        if ord(ch) > 47 and ord(ch) < 58:
            return True
        else:
            return False
        
inp = input("Enter a value ")
# for ch in inp:
#     print(ord(ch))

if stringChecker(inp):
    print(f'Float equivalent of the input value is {float(inp)}')
else:
    print(f"Entered input cannot be converted to float value")