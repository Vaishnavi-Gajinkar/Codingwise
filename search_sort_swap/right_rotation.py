''' implement right roation in an array for n times '''

arr = [int(val) for val in input("Enter elements of array (comma seperated) ").split(",")]
n = int(input("How many times do you want to rotate right? "))

# --- way 1 -----
arrcpy = arr
for iter in range(1,n+1):
    t = arrcpy[-1]                                         # grab the last element
    moves = len(arr)-1                                  # size-1 elements need to move automatically
    while moves > 0:                                    # move the elements from index 0 till secondlast
        arrcpy[moves] = arrcpy[moves-1]                   
        moves -= 1
    arrcpy[0] = t                                          # insert last element in 0th position
    print(f'Result after rotating {iter} times:',arrcpy)


# --- way 2 -----

def right_rot(lst:list, times:int):
    for i in range(times):
        lastElem = lst.pop()
        lst.insert(0,lastElem)

lst = arr

right_rot(lst,n)
print('\n',lst)

# OUTPUT:
'''
Enter elements of array (comma seperated) 1,2,3,4,5,6,7,8,9
How many times do you want to rotate right? 5
Result after rotating 1 times: [9, 1, 2, 3, 4, 5, 6, 7, 8]
Result after rotating 2 times: [8, 9, 1, 2, 3, 4, 5, 6, 7]
Result after rotating 3 times: [7, 8, 9, 1, 2, 3, 4, 5, 6]
Result after rotating 4 times: [6, 7, 8, 9, 1, 2, 3, 4, 5]
Result after rotating 5 times: [5, 6, 7, 8, 9, 1, 2, 3, 4]

 [9, 1, 2, 3, 4, 5, 6, 7, 8]
'''