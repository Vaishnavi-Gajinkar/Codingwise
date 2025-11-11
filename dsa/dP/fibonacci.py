''' wap to implement the fibbonacci series using dynamic programming '''
''' instead of calling repetitive function calls, save the result in a memory, to reuse '''

def fibo(key, memo={}):                                     # keep a memory as key-val pair in a default dictionary 
    if key <= 1:
        return key                                          # base condition
    elif key in memo:
        return memo[key]                                    # return value if key exist in memory
    else:
        memo[key] = fibo(key-1,memo)+fibo(key-2,memo)       # update memory with the new key-value
        return memo[key]                                    # exit function and return the result of the current key's value 

for i in range(10):
    print(fibo(i),end=',')                                  # calc the fibo value of current key and print as a series

'''
OUTPUT:
0,1,1,2,3,5,8,13,21,34,
'''