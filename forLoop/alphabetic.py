""" Use a for loop to check if all characters in string are alphabetic """

# print(ord('a'),ord('z'),ord('A'),ord('Z'))

str1 = input("Enter a string: ")
flag = 0
for ch in str1:
    if (ord(ch)>90 and ord(ch)<97) or ord(ch)<65 or ord(ch)>122:
        print(f'Non alphabetic character "{ch}" found in string')
        flag = 1
        break
if flag == 0:
    print("All chars of string are alphabetic")