""" Add two complex values """

def checkSign(comp):
    '''checks the sign of real and imaginary part'''
    
    if comp.startswith('-'):
        if comp.count('-') > 1:
            var = comp.replace('-','',1)
            clean = var.replace('j','')
            lst = clean.split('-')
            new_lst = [-int(val) for val in lst]
            return tuple(new_lst)
        else:
            var = comp.replace('-','')
            clean = var.replace('j','')
            lst = clean.split('+')
            new_lst = [int(val) for val in lst]
            return -new_lst[0], new_lst[1]
    else:
        if comp.count('-') != 1:
            clean = comp.replace('j','')
            lst = clean.split('+')
            new_lst = [int(val) for val in lst]
            return new_lst[0], new_lst[1]
        else:
            clean = comp.replace('j','')
            lst = clean.split('-')
            new_lst = [int(val) for val in lst]
            return new_lst[0], -new_lst[1]



num1 = input("Enter 1st complex num (in a+jb format) ")
num2 = input("Enter 2nd complex num (in a+jb format) ")

r1,i1 = checkSign(num1)
r2,i2 = checkSign(num2)

real = r1+r2
imgry = i1+i2

if imgry>0:
    print(f'{real}+j{imgry}')
else:
    print(f'{real}-j{abs(imgry)}')
