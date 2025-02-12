""" Find the squares till a given number """

def sqOnum(num):
    '''generates squares of each number'''
    for i in range(1,num+1):
        yield (i*i)
    
inp = int(input("Enter the number till which you want to see the squares "))

val = sqOnum(inp)

print(next(val))
print(next(val))
print(next(val))
print(next(val))
print(next(val))
print(next(val))
print(next(val))
print(next(val))
print(next(val))