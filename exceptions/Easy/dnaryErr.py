''' catch a Key-error while accessing a dictionary '''

try:
    dnary = {1:'a',2:'b',3:'c',4:'d',5:'e'}

    print(f'Accessing an existing key',dnary[3])

    print(f'Accessing a non-existing key',dnary[6])

except KeyError as ke:
    print('Key error caught,',ke)

finally:
    print('finally done with this prog coding 😎')