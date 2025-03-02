""" Check if a given string is empty """
""" Hint: use == or if not string """

file = open(r'C:\Users\Lenovo\OneDrive\Documents\PythonPractise\CodingWise\userDefinedfunctions\Easy\emptyFile.txt', 'w+')
contents = file.read()

if contents != '':
    print('Contents of the file is as below\n',contents)
elif contents == '':
    ask = input("Currently the file is empty. Would you like to type some content in file?")
    if ask.lower() == 'yes' or ask.lower() == 'y':
        contnt = input("Enter your content below\n")
        file.write(contnt)
        print("File updated successfully!")

    reask = input('Would you like to view the contents of the file? ')
    if reask.lower() == 'yes' or reask.lower() == 'y':
        f = open(r'C:\Users\Lenovo\OneDrive\Documents\PythonPractise\CodingWise\userDefinedfunctions\Easy\emptyFile.txt', 'r')
        print(f.read())
        # print('Contents of the file is as below\n',contnt)

file.close()        
print('Program executed successfully!')

# not solved