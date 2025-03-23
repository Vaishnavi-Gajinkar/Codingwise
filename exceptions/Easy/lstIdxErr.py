'''use a try-except block to catch an index error in a list'''

try:
    accept = input("Enter elements of list seperated by comma ")

    lizt = accept.split(',')

    for i in range(100):
        print(lizt[i])

except IndexError as ie:
    print('Index error caught,',ie)

finally:
    print("I'm so awesome 😎")
