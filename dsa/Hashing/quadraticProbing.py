''' wap to implement the insertion using quadratic probing '''
''' create a hash table of size 10 '''
''' insert elements of an array in the hash table at its mod10 position '''
''' if there is collision, add the element at (value + collision number²)%10 position in hashtable '''

hashTable = [0 for i in range(10)]                  # initializing hashtable arr with 0s

def hashfunc(val):
    return val%10                                   # calculates mod10 result of the value to insert

def quadraticProbing(val, coll_num):
    return (val + (coll_num**2))%10                 # quadratic probes if collision occurs

def insertion(val, hashTable):
    pos = hashfunc(val)
    if hashTable[pos] == 0:
        hashTable[pos] = val                        # normal insertion without collision
        return
    
    coll_count = 1
    newpos = quadraticProbing(val, coll_count)      # quadratic probing for new position upon collision
    while newpos != pos:
        if hashTable[newpos]==0:
            hashTable[newpos] = val
            return
        else:
            coll_count += 1
            newpos = quadraticProbing(val, coll_count)
    return

def deletion(hashTable, delval):
    if delval in hashTable:
        pos = hashTable.index(delval)
        hashTable[pos] = 0
        return
    print(f"value {delval} does not exist in hashtable")


arr = [10,11,22,33,44,55,62,73,84,95,66]
for val in arr:
    insertion(val,hashTable)
print(hashTable)

deletion(hashTable, 44)                             # deleting an existing element
print(hashTable)
deletion(hashTable, 50)                             # deleting a non-existing element
print(hashTable)

'''
OUTPUT:
[10, 11, 22, 33, 44, 55, 62, 73, 84, 95]
[10, 11, 22, 33, 0, 55, 62, 73, 84, 95]
value 50 does not exist in hashtable
[10, 11, 22, 33, 0, 55, 62, 73, 84, 95]
'''