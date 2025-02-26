'''print the middle character of a string (both odd/even length)'''

file = open(r'C:\Users\Lenovo\OneDrive\Documents\PythonPractise\CodingWise\userDefinedfunctions\Hard\fibbo.txt','r')

words = file.read()
# print(type(words))
cleaned_str = words.replace(".","")
cleaned_str = cleaned_str.replace(",","")
cleaned_str = cleaned_str.replace("/","")
# cleaned_str = cleaned_str.replace("\","")
lst = [word for word in cleaned_str.split(" ")]
print(lst)

str_mid = []
print("Middle characters of words in above list are:")

for string in lst:
    if len(string) == 0:
        pass
    elif len(string) == 1:
        str_mid.append(string)
    elif len(string)%2 == 0:
        mid = len(string)//2
        str_mid.append(string[mid-1]+string[mid])
    else:
        mid = (len(string)//2)
        str_mid.append(string[mid])
print(str_mid)