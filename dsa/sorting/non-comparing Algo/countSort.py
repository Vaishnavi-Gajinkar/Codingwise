''' wap to implement the Count sort algorithm in dsa '''
''' in a new array which is greater than our arr_to_sort, mark the number of times the element of that position has appeared.
    traverse from left-right or reverse, in new arr, to display the sorted array elements '''

def countSort(arr:list):
    size = max(arr)                                 # searching the max value element in arr
    dummy_arr = [0]*(size+1)                        # creating a 0s array of size greater than max val
    new_arr = []                                    # arr to store sorted elements

    for val in arr:
        dummy_arr[val] += 1                         # counting number of times a value appeared

    for idx in range(len(dummy_arr)):
        if dummy_arr[idx] != 0:                     # checking if value at that index exists
            num = dummy_arr[idx]
            i = idx
            while num>0:                            
                new_arr.append(i)                   # index position is appended equal to the times it is counted
                num -= 1
    return new_arr


x = [34,66,13,66,87,9,23,34,13,9,34,17,9]
res = countSort(x)

print(res)


''' 
OUTPUT : [9, 9, 9, 13, 13, 17, 23, 34, 34, 34, 66, 66, 87]
'''