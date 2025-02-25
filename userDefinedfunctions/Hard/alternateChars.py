'''print a string with every alternate character'''

#file = open(r"C:\Users\Lenovo\OneDrive\Documents\PythonPractise\CodingWise\userDefinedfunctions\Hard\fibbo.txt",'r')
file = open("C:\\Users\\Lenovo\\OneDrive\\Documents\\PythonPractise\\CodingWise\\userDefinedfunctions\\Hard\\fibbo.txt",'r')
f = file.read()
print(f)
for ch in f[0::2]:
    print(ch,end=" ")
file.close()
