""" Print 'hello world' in upper case """

def upperCase(str):
    '''modifies case of string to upper'''
    for ch in str:
        yield ch.upper()


inp = input("Enter a string in lower case ")

upper = upperCase(inp)
for val in inp:
    print(next(upper))
