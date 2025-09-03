'''check if a number is between 100 & 200 but not divisible by 5'''

# from functools import 

def divisibilityChk(lst):
    '''returns a list of numbers not divisible by 5'''
    res = filter(lambda x:(x%5!=0), lst)    
    return list(res)

def generateList(start, stop):
    '''creates a list of numbers'''
    for i in range(start, stop):
        yield i



inp = int(input("Enter a number between 100 & 200 "))
arrLeft = arrRight = []



val = generateList(100, inp)

for num in range(100,inp):
    arrLeft.append(next(val))

firsthalf = divisibilityChk(arrLeft)



val = generateList(inp, 200)

for num in range(inp,200):
    arrRight.append(next(val))

nexthalf = divisibilityChk(arrRight)


print("Numbers between 100 & 200 which are not divisible by 5 are:")
print(firsthalf,"\n", nexthalf)

'''
OUTPUT:
Enter a number between 100 & 200 150
Numbers between 100 & 200 which are not divisible by 5 are:
[101, 102, 103, 104, 106, 107, 108, 109, 111, 112, 113, 114, 116, 117, 118, 119, 121, 122, 123, 124, 126, 127, 128, 129, 131, 132, 133, 134, 136, 137, 138, 139, 141, 142, 143, 144, 146, 147, 148, 149] 
 [101, 102, 103, 104, 106, 107, 108, 109, 111, 112, 113, 114, 116, 117, 118, 119, 121, 122, 123, 124, 126, 127, 128, 129, 131, 132, 133, 134, 136, 137, 138, 139, 141, 142, 143, 144, 146, 147, 148, 149, 151, 152, 153, 154, 156, 157, 158, 159, 161, 162, 163, 164, 166, 167, 168, 169, 171, 172, 173, 174, 176, 177, 178, 179, 181, 182, 183, 184, 186, 187, 188, 189, 191, 192, 193, 194, 196, 197, 198, 199]

'''