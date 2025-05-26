'''print a string without the first and last character'''

file = open(r'C:\Users\Lenovo\OneDrive\Documents\PythonPractise\CodingWise\userDefinedfunctions\Hard\fibbo.txt','r')
contents = file.read()

for ch in contents: #range(1,len(contents)-1):
    if ch==' ':
        continue
    print(ch,end="")

#not solved