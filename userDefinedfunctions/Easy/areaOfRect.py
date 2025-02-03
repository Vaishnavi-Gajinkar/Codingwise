""" Calculate the area of rectangle """

def areaCalc(len=100, wdth=200):                    # default arguments
    ''' Calculates the area of rectangle'''
    return(len*wdth)


len = float(input("Enter the exact height of rectangle "))
base = float(input("Enter the exact width of rectangle "))

area = areaCalc(len,base)
print(f'The area of rectangle with height {len} and width {base} is {area}sq.units')
