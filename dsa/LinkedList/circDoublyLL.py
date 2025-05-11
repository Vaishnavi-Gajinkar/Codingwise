''' implement the insertion, deletion and traversal functions in a circular doubly linkedlist. '''
''' consider exhaustive testcase scenarios for robustness '''

class Node:
    prev = None
    data = None
    next = None

    def __init__(self, data):
        self.data = data

def insAtBigi(head, value):
    if head == None:
        newnode = Node(value)
        newnode.next = newnode
        newnode.prev = newnode
        print("Node added at begining of an empty DCLL")
        return newnode
    
    qtr = head
    ftr = head.next
    while ftr != head:
        qtr = qtr.next
        ftr = ftr.next
    
    newnode = Node(value)
    newnode.next = ftr
    newnode.prev = qtr
    ftr.prev = newnode
    qtr.next = newnode

    print("Node added at begining of a non-empty DCLL")
    return newnode

def insAtEnd(head, value):
    if head == None:
        newnode = Node(value)
        newnode.next = newnode
        newnode.prev = newnode
        print("Node added at end of an empty DCLL")
        return newnode
    
    qtr = head
    ftr = head.next
    while ftr != head:
        qtr = qtr.next
        ftr = ftr.next
    
    newnode = Node(value)
    newnode.next = ftr
    newnode.prev = qtr
    ftr.prev = newnode
    qtr.next = newnode

    print("Node added at end of a non-empty DCLL")
    return head

def insAtBetween(head, pos, value):
    if head == None:
        print("Node added at begining position of an empty DCLL")
        return insAtBigi(head, value)
    if pos == 0:
        print("Node added at begining position of an empty DCLL")
        return insAtBigi(head, value)
    
    count = 1
    ptr = head.next
    while ptr != head:
        ptr = ptr.next
        count += 1

    if pos < count:
        i = 0
        qtr = head
        ftr = qtr.next
        while i < pos-1:
            qtr = qtr.next
            ftr = ftr.next
            i += 1
        newnode = Node(value)
        newnode.next = ftr
        newnode.prev = qtr
        qtr.next = newnode
        ftr.prev = newnode

        print(f"Node added at position {pos} of DCLL")
        return head

def traverse(head):
    qtr = head.next
    print("DCLL in proper order is:")
    print(head.data,end="<->")
    while qtr.next!=head:
        print(qtr.data,end="<->")
        qtr = qtr.next
    print(qtr.data)

    print("DCLL in reverse order is:")
    qtr = head.prev
    while qtr != head:
        print(qtr.data, end="<->")
        qtr = qtr.prev
    print(qtr.data)

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)

a.prev = d
a.next = b

b.prev = a
b.next = c

c.prev = b
c.next = d

d.prev = c
d.next = a

traverse(a)
a = insAtBigi(a, 5)
a = insAtEnd(a, 50)
a = insAtBetween(a, 3, 25)
traverse(a)

'''
OUTPUT :
DCLL in proper order is:
10<->20<->30<->40
DCLL in reverse order is:
40<->30<->20<->10
Node added at begining of a non-empty DCLL
Node added at end of a non-empty DCLL
Node added at position 3 of DCLL
DCLL in proper order is:
5<->10<->20<->25<->30<->40<->50
DCLL in reverse order is:
50<->40<->30<->25<->20<->10<->5
'''