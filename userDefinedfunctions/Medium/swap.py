'''swap two numbers'''

def swapPos(num):
    ''' divides the number in half parts & interchanges their position '''
    size = len(str(num))
    lef = size//2
    rig = size-lef

    p1 = str(num)[0:lef]
    p2 = str(num)[rig:]

    # p1,p2 = p2,p1

    return p2+p1

def swapNums(num1, num2):
    ''' swaps the positions of two numbers which are entered '''
    num2,num1 = num1,num2

    return num1, num2


try:
    ask = int(input("How many numbers do you have? (1or2) "))
    if ask == 1:
        num = int(input("Enter the number "))
        print(f'Number with swapped integers are {swapPos(num)}')

    elif ask == 2:
        num1, num2 = input("Enter the numbers (space seperated) ").split(" ")
        print(f'Swapped numbers are {swapNums(int(num1),int(num2))}')

    else:
        print("Invalid input")
except:
    print("Some error occured! Pls try again") 


'''
OUTPUT:
---------------------------------------------------------------------------
How many numbers do you have? (1or2) 1
Enter the number 1111155555
Number with swapped integers are 5555511111
----------------------------------------------------------------------------
How many numbers do you have? (1or2) 2
Enter the numbers (space seperated) 222222 333333
Swapped numbers are (333333, 222222)
----------------------------------------------------------------------------
How many numbers do you have? (1or2) 8
Invalid input
----------------------------------------------------------------------------
How many numbers do you have? (1or2) ganpatibappa!
Some error occured! Pls try again
'''