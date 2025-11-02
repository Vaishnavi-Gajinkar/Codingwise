''' wap to delete a node from heap '''
''' in the prebuilt heap structure, swap the value of the position of to be deleted with the last element of heap '''
''' pop the last node from heap '''
''' heapify the remaining elements of heap '''

def heapify(arr:list, arr_len:int, parent_idx):
    largest = parent_idx
    left_child_idx = 2*parent_idx+1
    right_child_idx = 2*parent_idx+2

    if left_child_idx < arr_len and arr[left_child_idx] > arr[largest]:
        largest = left_child_idx

    if right_child_idx < arr_len and arr[right_child_idx] > arr[largest]:
        largest = right_child_idx

    if largest != parent_idx:
        arr[largest] , arr[parent_idx] = arr[parent_idx] , arr[largest]
        heapify(arr, arr_len, largest)

def buildHeap(arr:list):
    count_nodes = len(arr)
    parents = (count_nodes -1)//2

    for parent in range(parents,-1,-1):
        heapify(arr, count_nodes, parent)

def deletion(arr, val):
    arr_len = len(arr)
    if val in arr:
        ele_pos = arr.index(val)                                        # find index of the element to be deleted
        
        temp = arr[ele_pos]                                             # swap the element with last element of array
        arr[ele_pos] = arr[arr_len-1]
        arr[arr_len-1] = temp

        arr.pop()                                                       # delete the last element
        buildHeap(arr)                                                  # rebuild max heap with existing elements
    else:
        print("Invalid element to delete")



arr = [10,15,31,26,71,40,28,55]

buildHeap(arr)

print(arr)

deletion(arr, 31)                                                       # deleting existing element

print(arr)

deletion(arr, 22)                                                       # deleting non-existing element

'''
OUTPUT :
[71, 55, 40, 26, 15, 31, 28, 10]
[71, 55, 40, 26, 15, 10, 28]
Invalid element to delete
'''