''' reverse the elements of a list using swapping method '''

arr = [int(x) for x in input("Enter values of array (comma seperated) ").split(",")]

i = 0
j = len(arr)-1

while i < j:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    i += 1
    j -= 1
print(arr)

#---- way 2 ------------

for val in range(len(arr)//2):
    t = arr[val]
    arr[val] = arr[len(arr)-1-val]
    arr[len(arr)-1-val] = t

print("Reversing the reversed array again\n",arr)