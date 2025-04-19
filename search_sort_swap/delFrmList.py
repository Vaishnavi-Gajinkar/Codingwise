''' Delete an element at a specific position from list using default Pop function (not delete)'''

lst = [10,20,30,40,50,60,70,80,90,100]
print(lst)
pos = int(input("At which position is the number which u want to delete? "))


try:
    elemnt = lst[pos]
    while pos < len(lst)-1:
        lst[pos] = lst[pos+1]
        pos += 1
    lst[pos] = elemnt
    lst.pop()
    print(lst)
except Exception as e:
    print("No element exists at specified position")