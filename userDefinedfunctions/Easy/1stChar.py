""" Print first character of a string """

def nth_char(str, n):
    '''returns nth req character of mentioned string'''
    return str[n-1]

def multi_chars(str, lizt):
    '''returns all positional chars req'''
    lst = []
    print(lizt)
    for i in lizt:
        lst.append(str[int(i)-1])
    return lst


sentence = input("Enter ur string ")
ask = input('Would you like to fetch a single char or multiple chars \nType single/multi: ')
if ask.lower() == 'single':
    val = int(input("Enter required position "))
    char_val = nth_char(sentence,val)
    print("Character at mentioned positions is",char_val)
elif ask.lower() == 'multi':
    inp = input('Enter position values seperated by comma ')
    vars = inp.split(',')
    print(vars)
    chars = multi_chars(sentence, vars)
    print("Characters at mentioned positions are",chars)
else:
    print("Invalid input")