""" While loop to check if number is palindrome (eg. 121) """

inp = input("Enter a string or integer ")
try:
# if type(inp) == "<class 'int'>":
    num = int(inp)
    temp = num
    revNum = 0

    while temp > 0:
        i = temp % 10
        revNum = (revNum*10)+i
        temp = temp//10

    if revNum == num:
        print("Number is palindrome")
    else:
        print("Number is not a palindrome")

except:
    # type(inp) == "<class 'str'>":
    temp = inp
    size = len(temp)-1
    revStr = ""

    while size >=0:
        revStr += temp[size]
        size -= 1

    if revStr == temp:
        print("String is palindrome")
    else:
        print("String is not a palindrome")

# else:
#     print("Invalid Input")