'''check if a character exists in a string'''

def charCheck(string, tgt):
    ''' checks if the target character is in the string'''
    if tgt in string:
        return True
    else:
        return False
    
inp = input("Enter a main string - ")
tgt = input("Enter target to check if exists in main string - ")

filter_lst = filter(charCheck(inp,tgt), tgt)

# result = charCheck(inp, tgt)
for val in filter_lst:
    print(val,end=" ")

# not solved