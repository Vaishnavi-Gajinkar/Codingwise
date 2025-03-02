'''reverse the digits of a number (convert to string first)'''

def reverse1(num):
    return int(num[::-1])

# way2
def reverse2(string):
    # rev_num = 
    for ch in string[-1:-1:-1]:
        yield ch



try:
    inp = input("Enter a number ")
    print("Entered number in reverse is read as",reverse1(inp))

    length = len(inp)
    print(length)
    rev2 = reverse2(inp)
    for iter in range(length):
        print(next(rev2),end="")
    
        
except Exception as e:
    print("An error occured!\n",e)

# not solved
