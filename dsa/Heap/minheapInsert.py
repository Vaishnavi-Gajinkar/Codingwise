''' wap to implement the min heap ds by adding elements 1-by-1 '''
''' add nodes in a complete binary tree format (L-R-L-R) compare each added node with it parent until root. swap positions if added node is lt parent '''
''' traverse L-R in tree and display the elements '''

def minheapInsert(arr:list, val):
    arr.append(val)                                         # adding new array value to the list
    current = len(arr)-1                                    # current points to size of constructed tree minus root (i.e. last position filled in the complete BT)

    while current > 0:                                      # checking ptr is not on root node as it has no parents to calc further
        parent = (current-1)//2                             # formula to calc position of parent node wrt to pos of new node's position

        if arr[current] < arr[parent]:                      # comparing current's val to parent to check whether swapping needed
            temp = arr[current]
            arr[current] = arr[parent]
            arr[parent] = temp
            current = parent
        else:
            break                                           # no swapping needed as new node val is greater than parent node
    
    print(arr)                                              # printing all nodes of tree after adding new val, scanning from left-right
    return

arr = []
minheapInsert(arr, 5)
minheapInsert(arr, 9)
minheapInsert(arr, 4)
minheapInsert(arr, 14)
minheapInsert(arr, 21)
minheapInsert(arr, 28)
minheapInsert(arr, 19)
minheapInsert(arr, 31)
minheapInsert(arr, 44)
minheapInsert(arr, 37)


'''
OUTPUT :
[5]
[5, 9]
[4, 9, 5]
[4, 9, 5, 14]
[4, 9, 5, 14, 21]
[4, 9, 5, 14, 21, 28]
[4, 9, 5, 14, 21, 28, 19]
[4, 9, 5, 14, 21, 28, 19, 31]
[4, 9, 5, 14, 21, 28, 19, 31, 44]
[4, 9, 5, 14, 21, 28, 19, 31, 44, 37]
'''