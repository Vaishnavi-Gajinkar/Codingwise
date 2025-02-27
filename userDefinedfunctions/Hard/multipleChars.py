'''print the first 3 characters of a string n times '''

def repit(word, n):
    '''repeats the first 3 chars of word n times'''
    display = word[0:3]*n
    return display

inp = input('Enter a word ')
count = int(input('Enter the number of times to be repeated '))

print(repit(inp,count))

