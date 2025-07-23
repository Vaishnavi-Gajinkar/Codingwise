''' wap to implement the Bubble sort algorithm in dsa '''
''' given a list compare and place the largest element at end position
    compare the 2 adjacent elements in each iteration of inner loop '''

def bubbleSort(arr:list):

    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                t = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = t

    return arr

x = [34,66,13,87,9,23,17]
res = bubbleSort(x)
print(res)