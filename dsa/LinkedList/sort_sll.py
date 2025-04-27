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

def sortIt(head, data):
    ptr = head
    arr = []

    while ptr:
        arr.append(ptr.data)
        ptr = ptr.next
    arr.sort()

    newptr = head
    while


def traverse(head):
    qtr = ftr = head
    count = 0
    while qtr:
        count += 1
        qtr = qtr.next
    print(f"Currently there are {count} nodes in the LL")

    while ftr:
        print(ftr.data, end="->")
        ftr = ftr.next
    print("None")



a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)

a.next = b
b.next = c
c.next = d
d.next = None

a = insAtEnd(a,65)
a = insAtEnd(a,32)
a = insAtEnd(a,15)
a = insAtEnd(a,43)

traverse(a)