'''reverse a string'''

def str_rev(string, rev_str):
    ''' reversing a string using recursion '''

    if len(string) == 0:
        return rev_str
    rev_str = rev_str + string[-1]
    # print(rev_str)
    return str_rev(string[:-1], rev_str)



text = input("Enter any string: ")
reversed_str = ""
reverse = str_rev(text, reversed_str)
print("string reversed by recursion", reverse)


# ---------- alternate way ----------------
print("\nstring reversed simply")
print(text[::-1])



'''
OUTPUT :
Enter any string: recusrsionisconfusion
string reversed by recursion noisufnocsinoisrsucer

string reversed simply
noisufnocsinoisrsucer
'''