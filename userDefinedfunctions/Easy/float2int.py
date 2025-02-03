""" Convert a float to integer """

def typeConv(str):
    '''Converts the datatype of input string'''
    def floatEq(str):                           # defining function inside another function
        return float(str)
    
    def intEq(floatVal):                        # defining function inside another function
        return int(floatVal)
    
    floatVal = floatEq(str)
    intVal = intEq(floatVal)
    
    return floatVal, intVal                     # function can return multiple values



inp = input("Enter any value ")
flv,inv = typeConv(inp)
print(f"Integer equivalent of {flv} is {inv}")