""" Iterate through a list [2, 4, 6, 8] and print each element """

lizt = [2,4,6,8]                                                #defining list values explicitly 
for item in lizt:
    print(item, end=' ')

num = int(input("Enter count of element u want to enter: "))    # defining size of list
print("Enter the elements : ")                          
lst = []
for i in range(num):                                            # accepting list elements
    lst.append(input())

print("Elements of your list are: ")

for item in lst:
    print(item, end=' ')