''' wap to implement the hashing using linear probing '''
''' create a hash table of size 10 '''
''' insert elements of an array in the hash table at its mod10 position '''
''' if there is collision, add the element at (value + collision number)%10 position in hashtable '''

hashTable = [0 for i in range(10)]                          # initializing hashtable arr with 0s

def hashVal(value):
    return value%10                                         # calculates mod10 result of the value to insert

def linearProbe(value, coll_count):
    return (value + coll_count)%10                          # linear probes if collision occurs

def insertion(hashTable, value):
    position = hashVal(value)
    if hashTable[position]==0:
        hashTable[position] = value                         # normal insertion without collision
        return
    
    coll_count = 1                                          # linear probing for new position upon collision
    newposition = position+1
    while newposition != position:
        newposition = linearProbe(value, coll_count)
        if hashTable[newposition]==0:
            hashTable[newposition] = value
            return
        coll_count = coll_count+1



arr = [10,11,22,33,44,55,66,77,20,36,57]
for val in arr:
    insertion(hashTable, val)

print(hashTable)

'''
OUTPUT:
[10, 11, 22, 33, 44, 55, 66, 77, 20, 36]

'''

# 57 is not added as size of arr > 10