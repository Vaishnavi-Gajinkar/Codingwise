''' wap to implement the hash method using chaining '''
''' create a hash table of size 10 '''
''' insertion elements of a large array in the hash table at its mod10 position '''
''' if there is collision, create a SLL node and link it to that index positon of hashtable '''


hashTable = [[] for i in range(10)]                 # size of hashtable is fixed to 10

def chainHsh(val):
    return (val % 10)                               # returns mod10 result of value

def insertion(hashTable, val):
    position = chainHsh(val)
    hashTable[position].append(val)                 # insertions the value at its hash position

def deletion(hashTable, delval):
    pos = chainHsh(delval)
    for iter in range(len(hashTable[pos])):
        if delval == hashTable[pos][iter]:          # locates and deletes the element from hashtable
            del hashTable[pos][iter]
            break
    else:
        print("Could not find the value to be deleted")
    return

def display(hashTable):
    print("\nChained hashtable looks as below:")
    for i in range(len(hashTable)):             
        if hashTable[i] == []:                      # prints none if the index of hashtable is empty
            print("None",end="")
        else:
            for j in range(len(hashTable[i])):
                print(hashTable[i][j], end=", ")    # prints the value if not empty
        print()



arr = [10,11,22,23,24,62,34,83,94,12,17,18]
for val in arr:
    insertion(hashTable, val)

print(hashTable)

deletion(hashTable, 83)                             # deleting an existing element
print(hashTable)

deletion(hashTable, 15)                             # deleting a non-existing element
print(hashTable)

display(hashTable)

'''
OUTPUT :
[[10], [11], [22, 62, 12], [23, 83], [24, 34, 94], [], [], [17], [18], []]
[[10], [11], [22, 62, 12], [23], [24, 34, 94], [], [], [17], [18], []]
Could not find the value to be deleted
[[10], [11], [22, 62, 12], [23], [24, 34, 94], [], [], [17], [18], []]

Chained hashtable looks as below:
10,
11,
22, 62, 12,
23,
24, 34, 94,
None
None
17,
18,
None
'''