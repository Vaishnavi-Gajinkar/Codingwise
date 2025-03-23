'''Handle missing file error while reading a file'''

try:
    with open(r'C:\Users\Lenovo\OneDrive\Documents\PythonPractise\CodingWise\recursion\fibonacci.txt','r') as file:
        print(file)
    
except FileNotFoundError as fnfe:
    print('File not found error caught,',fnfe)

finally:
    print('Whevf, that was some intense level coding now!🫥')