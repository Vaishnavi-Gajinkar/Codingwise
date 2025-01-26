""" Use a for loop to print each character in the string 'Python' """

string = 'Python'                                       #hard coding the value of Python
for ch in string:
    print(ch, end=' ')


word = input("Enter your desired word / sentence: ")    #taking input word or sentence from user
if " " in word:
    arr = word.split(' ')
    print(arr)
else:
    for ch in word:
        print(ch)
