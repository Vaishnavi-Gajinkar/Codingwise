''' delete the duplicate nodes of a linked list'''

class Node:
    data = None
    next = None

    def __init__(self,data):
        self.data = data

def insAtEnd(head, data):
    newnode = Node(data)

    if head == None:
        head = newnode
        return head
    
    ptr = head
    while ptr.next:
        ptr = ptr.next
    ptr.next = newnode
    return head

def removeDups(head):
    ptr = head
    arr = []

    while ptr:
        if ptr.data not in arr:
            arr.append(ptr.data)
        ptr = ptr.next
    
    newptr = None
    for i in range(len(arr)):
        # newnode = Node(arr[i])
        newptr = insAtEnd(newptr, arr[i])
    return newptr

def traverse(head):
    ptr = head
    while ptr:
        print(ptr.data, end="->")
        ptr = ptr.next
    print('None')

    print("LL after deleting duplicates looks like below")
    newptr = removeDups(head)
    while newptr:
        print(newptr.data, end="->")
        newptr = newptr.next
    print('None')

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)

a.next = b
b.next = c
c.next = d

# a = None
# for i in range(10,101,10):
a = insAtEnd(a, 70)
a = insAtEnd(a, 60)
a = insAtEnd(a, 50)
a = insAtEnd(a, 40)
a = insAtEnd(a, 30)
a = insAtEnd(a, 20)
a = insAtEnd(a, 10)

traverse(a)

'''
OUTPUT :
10->20->30->40->70->60->50->40->30->20->10->None
LL after deleting duplicates looks like below
10->20->30->40->70->60->50->None'''