''' print the fibonacci series upto n numbers '''
''' fibonacci =  1 1 2 3 5 8 '''


def fibo(n):

    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
itrn = 6
print(fibo(itrn))
