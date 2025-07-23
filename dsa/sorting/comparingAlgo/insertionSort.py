''' wap to implement the insertion sort algorithm '''
''' split the array in 2 parts and add elements from 2nd to 1st part in correct sorted position '''

def insertionSort(arr:list):

    for i in range(1,len(arr)):                     # handling right split array
        val = arr[i]
        j = i-1
        while j>=0 and val<arr[j]:               # sorting the left array wrt new element (pivot)
            arr[j+1] = arr[j]                       # move the larger element right
            j -= 1
        arr[j+1] = val                           # j halts on the value lesser than pivot. increment j and then add pivot
    return arr

x = [34,66,13,87,9,23,17]
res = insertionSort(x)
print(res)