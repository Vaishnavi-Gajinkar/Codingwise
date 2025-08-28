'''check if the first character of a string is vowel'''

def vowelCheck(inp_str):
    ''' checks if string starts with a vowel '''
    if inp_str[0] in ('a','e','i','o','u'):
        return True
    return False

inp = input("Enter a statement: ")
res = vowelCheck(inp)

if res:
    print("First character of string is a vowel")
else:
    print("First character of string is a consonenet")
