''' wap to implement the Quick sort algorithm in dsa '''
''' select 1st element of arr as pivot. divide the arr into 2 parts, left elements < pivot, right elements > pivot. merge the leaves of tree '''

def quickSort(arr:list):
    if len(arr)==0 or len(arr)==1:                  # handling leaf nodes
        return arr
    else:
        left_arr = []
        right_arr = []
        pivot = arr[0]
        for i in arr[1:]:
            if i < pivot:
                left_arr.append(i)                  # collecting elements less than pivot in left sub-array
            elif i > pivot:
                right_arr.append(i)                 # collecting elements greater than pivot in right sub-array
        left = quickSort(left_arr)        
        right = quickSort(right_arr)                # recursively calling sub-arrays

    return [*left,pivot,*right]                     # returning all elements concatenated in list format


x = [34,66,13,66,87,9,23,17]
res = quickSort(x)

print(res)


''' OUTPUT :
[9, 13, 17, 23, 34, 66, 87]

'''