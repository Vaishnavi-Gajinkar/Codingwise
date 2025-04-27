''' sort the elements of a singly linked list '''

class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data

def insAtEnd(head, data):
    newnode = Node(data)

    if head == None:
        head = newnode
        return head
    
    qtr = head
    ftr = qtr.next
    while ftr:
        qtr = qtr.next
        ftr = ftr.next
    qtr.next = newnode
    return head

def sortIt(head):
    ptr = head
    arr = []                                    # empty list to store all elements

    while ptr:
        arr.append(ptr.data)                    # insert all elements of LL
        ptr = ptr.next
    arr.sort()                                  # sort the elements
    # print(arr)

    newptr = None                               # new pointer to create a LL of sorted elements
    for n in range(len(arr)):
        newptr = insAtEnd(newptr, arr[n])       # create nodes of the sorted list elements
    return newptr

def traverse(head):
    qtr = ftr = head
    count = 0
    while qtr:
        count += 1
        qtr = qtr.next
    print(f"Currently there are {count} nodes in the LL")       # displays count of nodes

    while ftr:
        print(ftr.data, end="->")                               # displays unsorted elements
        ftr = ftr.next
    print("None\nAfter Sorting, elements of LL are rearranged as below")

    srt = sortIt(head)                                          # implicit call to create LL of sorted elements
    while srt:
        print(srt.data, end="->")                               # displays sorted elements
        srt = srt.next
    print("None")


# a = Node(10)
# b = Node(20)
# c = Node(30)
# d = Node(40)

# a.next = b
# b.next = c
# c.next = d
# d.next = None

a = None
a = insAtEnd(a,10)
a = insAtEnd(a,20)
a = insAtEnd(a,30)
a = insAtEnd(a,40)

a = insAtEnd(a,65)
a = insAtEnd(a,32)
a = insAtEnd(a,15)
a = insAtEnd(a,43)

traverse(a)