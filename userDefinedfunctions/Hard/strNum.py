'''print a number as a string, repeated as many times as its value'''
'''hint: use string multiplication'''

class TypeConv:
    def strToInt(self, str):
        return int(str)
    
    def intToStr(self, num):
        return str(num)
    
inp = int(input("Enter a number "))

obj1 = TypeConv()

val = obj1.intToStr(inp)

# way1
print(val*inp)

# way2 
for iter in range(inp):
    print(val,end=" ")
