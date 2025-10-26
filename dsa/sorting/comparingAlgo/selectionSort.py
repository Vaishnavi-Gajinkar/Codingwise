''' wap to implement the Selection sort algorithm in dsa '''
''' traversing from left to right in array, check the most eligible value for the current position '''

def selectionSort(arr):
    for i in range(len(arr)):                                          # checking eligible value for i th position
        min_val_elemt_in_right_section = i
        for j in range(i+1,len(arr)):                                  # j starts 1 idx next to i
            if (arr[min_val_elemt_in_right_section] > arr[j]):         # check all j side elements for least value
                min_val_elemt_in_right_section = j

        t = arr[i]                                                     # swap the i th idx element with at least value found in right section
        arr[i] = arr[min_val_elemt_in_right_section]
        arr[min_val_elemt_in_right_section] = t
    
    return arr


x = [34,66,13,87,9,23,17]
res = selectionSort(x)
print(res)