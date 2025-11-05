''' wap to implement the hash method using chaining '''
''' create a hash table of size 10 '''
''' insert elements of a large array in the hash table at its mod10 position '''
''' if there is collision, create a SLL node and link it to that index positon of hashtable '''


hashTable = [[] for i in range(10)]                 # size of hashtable is fixed to 10

def chainHsh(val):
    return (val % 10)                               # returns mod10 result of value

def insert(hashTable, val):
    position = chainHsh(val)
    hashTable[position].append(val)                 # inserts the value at its hash position



arr = [10,11,22,23,24,62,34,83,94,12,17,18]
for val in arr:
    insert(hashTable, val)

print(hashTable)


'''
OUTPUT :
[[10], [11], [22, 62, 12], [23, 83], [24, 34, 94], [], [], [17], [18], []]
'''