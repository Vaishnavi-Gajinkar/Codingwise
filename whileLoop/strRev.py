""" Write a while loop to reverse a string (eg. 'world' to 'dlrow')"""

str = 'world'
ch = len(str)-1

while ch >= 0:
    print(str[ch], end="")
    ch -= 1
