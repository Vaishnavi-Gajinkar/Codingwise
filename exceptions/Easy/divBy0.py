'''wap to handle division by zero error'''

try:
    val = int(input("Enter a number "))

    res = 1000 / val

    print(f'result of the calculation is {res}')

except ZeroDivisionError:
    print(ZeroDivisionError)

finally:
    print('Program ended successfully ')


# Output :
'''
Enter a number 5
result of the calculation is 200.0
Program ended successfully

Enter a number 0
<class 'ZeroDivisionError'>
Program ended successfully
'''