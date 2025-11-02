''' wap to create a max heap using an array '''
''' add all arr elements in a complete binary tree format (L-R-L-R) compare each added node with it parent until root.'''
''' swap positions if current node value is greater than its parent '''
''' traverse L-R in tree and display the elements '''

def heapify(arr:list, arr_len:int, parent_idx):
    largest = parent_idx                                                # assume parent has largest node value 
    left_child_idx = 2 * parent_idx + 1
    right_child_idx = 2 * parent_idx + 2

    if left_child_idx < arr_len:                                        # check if left child exists
        if arr[left_child_idx] > arr[largest]:                          # check if left child value is gt parent
            largest = left_child_idx                                    # update largest to left child idx

    if right_child_idx < arr_len:                                       # check if right child exists
        if arr[right_child_idx] > arr[largest]:                         # check if right child value is gt parent
            largest = right_child_idx                                   # update largest to right child idx

    if largest != parent_idx:                                           # new largest value found in child
        temp = arr[parent_idx]                                          # swap node values so higher value becomes parent
        arr[parent_idx] = arr[largest]
        arr[largest] = temp

        heapify(arr, arr_len, largest)                                  # recursively iterate till root

def build_heap(arr):
    arr_len = len(arr)
    tot_parents = (arr_len -1 )//2                                      # calc total parent nodes in array
    
    for parent_num in range(tot_parents,-1,-1):                         # heapify each parent node
            heapify(arr, arr_len, parent_num)


arr = [10,15,31,26,71,40,28,55]
build_heap(arr)
print(arr)


'''
OUTPUT : 
[71, 55, 40, 26, 15, 31, 28, 10]
'''