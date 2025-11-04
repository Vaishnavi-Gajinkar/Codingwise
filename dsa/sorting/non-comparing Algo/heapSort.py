''' wap to implement the Heap sort algorithm in dsa '''
''' add all arr elements in a complete binary tree format (L-R-L-R) '''
''' swap positions of last node with root node '''
''' pop the last leaf node '''
''' heapify the new structure '''
''' traverse L-R in tree and display the elements '''

def heapify(arr, arr_len, parent_idx):
    largest = parent_idx
    left_child_idx = 2*parent_idx+1
    right_child_idx = 2*parent_idx+2

    if left_child_idx < arr_len:
        if arr[left_child_idx] > arr[largest]:
            largest = left_child_idx
    if right_child_idx < arr_len:
        if arr[right_child_idx] > arr[largest]:
            largest = right_child_idx

    if largest != parent_idx:
        temp = arr[largest]
        arr[largest] = arr[parent_idx]
        arr[parent_idx] = temp

        heapify(arr, arr_len, largest)

def buildHeap(arr):
    current_idx = len(arr)
    total_parents = (current_idx-1)//2

    for parent in range(total_parents, -1, -1):
        heapify(arr, current_idx, parent)

def heapSort(arr):
    new_arr = []
    last_idx = len(arr)
    
    for idx in range(last_idx):
        # arr[0], arr[last_idx-1] = arr[last_idx-1], arr[0]
        temp = arr[0]                                                      # swap last node value with root node
        arr[0] = arr[last_idx-1]
        arr[last_idx-1] = temp
        
        popped_val = arr.pop()                                              # pop the last node
        new_arr.insert(0, popped_val)                                       # insert the last value in new arr
        
        buildHeap(arr)                                                      # heapify the new structure
    print(arr)



arr = [10,15,31,26,71,40,28,55]
buildHeap(arr)
print(arr)
heapSort(arr)
