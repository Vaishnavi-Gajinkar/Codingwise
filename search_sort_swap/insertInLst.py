''' Insert an element in list at a specific position using Append function (not insert)'''

lst = [10,20,30,40,50,60,70,80,90,100]
print(lst)
num = int(input("Which number do u want to add? "))
pos = int(input("At which position? "))

lst.append(num)
for i in range(len(lst)-1,pos,-1):
    lst[i] = lst[i-1]
lst[pos] = num

print(lst)

# Output
'''
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Which number do u want to add? 35
At which position? 3
[10, 20, 30, 35, 40, 50, 60, 70, 80, 90, 100]

PS C:\Users\Lenovo\OneDrive\Documents\PythonPractise> & C:/Users/Lenovo/AppData/Local/Programs/Python/Python313/python.exe c:/Users/Lenovo/OneDrive/Documents/PythonPractise/CodingWise/search_sort_swap/insertInLst.py
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Which number do u want to add? 5
At which position? 0
[5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

PS C:\Users\Lenovo\OneDrive\Documents\PythonPractise> & C:/Users/Lenovo/AppData/Local/Programs/Python/Python313/python.exe c:/Users/Lenovo/OneDrive/Documents/PythonPractise/CodingWise/search_sort_swap/insertInLst.py     
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Which number do u want to add? 105
At which position? 10
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 105]
'''