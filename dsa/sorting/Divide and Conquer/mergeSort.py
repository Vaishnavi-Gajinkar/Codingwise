''' wap to implement the Merge sort algorithm in dsa '''
''' floor divide the arr into 2 parts, left elements in left sub-arr, right elements in right sub-arr. merge the leaves of tree by sorting elements on the fly '''

def mergeSort(arr:list):
    if len(arr)==0 or len(arr)==1:                          # handling leaf arrays
        return arr
    else:
        mid = len(arr)//2                                   # integer split the array
        left = []
        right = []

        for i in range(mid):
            left.append(arr[i])                             # collect left side elements
        for j in range(mid,len(arr)):
            right.append(arr[j])                            # collect right side elements
        
        sort_left = mergeSort(left)                         # recursively calling function to split in half
        sort_right = mergeSort(right)
        sorted_arr = []
        i = 0
        j = 0
        while i<len(sort_left) and j<len(sort_right):       # comparing leaf node values of left & right subarrays
            if sort_left[i] < sort_right[j]:
                sorted_arr.append(sort_left[i])             # adding the lower value from left subarray
                i += 1
            else:
                sorted_arr.append(sort_right[j])            # adding the lower value from right subarray
                j += 1

        while i < len(sort_left):
            sorted_arr.append(sort_left[i])                 # appending all remaining values from left sub-arr
            i += 1
        while j < len(sort_right):
            sorted_arr.append(sort_right[j])                # appending all remaining values from right sub-arr
            j += 1

        return sorted_arr
    
x = [34,66,13,87,9,23,17]
res = mergeSort(x)

print(res)


'''
OUTPUT : 
[9, 13, 17, 23, 34, 66, 87]

'''