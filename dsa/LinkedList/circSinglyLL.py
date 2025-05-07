''' implement the insertion, deletion and traversal functions in a circular singly linkedlist. '''
''' consider exhaustive testcase scenarios for robustness '''

class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data

def insAtBigi(head, value):
    newnode = Node(value)
    
    if head == None:
        newnode.next = newnode
        return newnode
    # newnode.next = head                           # cannot add node from head as end node needs to be connected to newnode then
    # head = newnode
    
    qtr = head
    ftr = qtr.next
    while qtr.next != head:
        qtr = qtr.next
        ftr = ftr.next

    newnode.next = ftr
    qtr.next = newnode
    return newnode

def insAtEnd(head, value):
    newnode = Node(value)
    
    if head == None:
        newnode.next = newnode
        return newnode
    
    qtr = head
    ftr = qtr.next
    while qtr.next != head:
        qtr = qtr.next
        ftr = ftr.next

    newnode.next = ftr
    qtr.next = newnode
    return head

def traverse(head):
    qtr = head
    ftr = qtr.next
    count = 1
    while ftr != head:
        print(qtr.data,end='->')
        qtr = qtr.next
        ftr = ftr.next
        count += 1
    print(f'{qtr.data}->None')
    print(f'Currently there are {count} nodes in the circularLL')

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)

a.next = b
b.next = c
c.next = d
d.next = a

traverse(a)
a = insAtBigi(a, 5)
a = insAtEnd(a, 45)
traverse(a)