""" Use a For loop to create a new list containing only positive numbers from the list [-10,-5,0,5,10] """

values = input("Enter list values with +ve & -ve numbers (seperated with space) ")
lst = values.split(' ')
posLst = []
for val in lst:
    if int(val) >=0:
        posLst.append(val)
print(posLst)


