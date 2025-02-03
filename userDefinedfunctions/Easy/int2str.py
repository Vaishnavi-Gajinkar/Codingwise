""" Convert a number to a string """

def typeConv(num):
    return num

def toStr(inp):
    return str(inp)
    
        
val = float(input("Enter a number"))
ret = typeConv(toStr(val))                      # function can be passed as a parameter
print(ret, type(ret))
