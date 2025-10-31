''' wap to implement the max heap using an array '''
''' add nodes in a complete binary tree format (L-R-L-R) compare each added node with it parent until root. swap positions if added node is gt parent '''
''' traverse L-R in tree and display the elements '''

# def node(val):                                                    # not req as not implementing in linked list format
#     val = val
#     left = None
#     right = None

def insertIntoMaxHeap(arr:list, val):
    arr.append(val)                                                 # adding new array value to the list
    current = len(arr)-1                                            # current points to size of constructed tree minus root (i.e. last position filled in the complete BT)

    while current > 0:                                              # ptr is not on root node as it has no parents to calc further
        parent = (current-1)//2                                     # formula to calc position of parent node wrt to pos of new node's position

        if arr[current] > arr[parent]:                              # comparing current's val to parent to check whether swapping needed
            temp = arr[current]
            arr[current] = arr[parent]
            arr[parent] = temp
            current = parent
        else:
            break                                                   # no swapping needed as new node val is lesser than parent node
    print(arr)                                                      # printing all nodes of tree scanning from left-right

    return

arr = []
insertIntoMaxHeap(arr, 5)
insertIntoMaxHeap(arr, 9)
insertIntoMaxHeap(arr, 4)
insertIntoMaxHeap(arr, 14)
insertIntoMaxHeap(arr, 21)
insertIntoMaxHeap(arr, 28)
insertIntoMaxHeap(arr, 19)
insertIntoMaxHeap(arr, 31)
insertIntoMaxHeap(arr, 44)
insertIntoMaxHeap(arr, 37)


''' OUTPUT :
[5]
[9, 5]
[9, 5, 4]
[14, 9, 4, 5]
[21, 14, 4, 5, 9]
[28, 14, 21, 5, 9, 4]
[28, 14, 21, 5, 9, 4, 19]
[31, 28, 21, 14, 9, 4, 19, 5]
[44, 31, 21, 28, 9, 4, 19, 5, 14]
[44, 37, 21, 28, 31, 4, 19, 5, 14, 9]
'''