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
        print(f"Node of value {value} added at begining when CSLL is empty")
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
    print(f"Node with val {value} added at begining of a non-empty CSLL")
    return newnode

def insAtEnd(head, value):
    newnode = Node(value)
    
    if head == None:
        newnode.next = newnode
        print(f"Node with value {value} added at end of an empty CSLL")
        return newnode
    
    qtr = head
    ftr = qtr.next
    while qtr.next != head:
        qtr = qtr.next
        ftr = ftr.next

    newnode.next = ftr
    qtr.next = newnode
    print(f"Node with value {value} added at end of a non-empty CSLL")
    return head

def insInBtwn(head, pos, value):
    if head == None:
        newnode = Node(value)
        head = newnode
        newnode.next = newnode
        print(f"Node with value {value} added at begining position of an empty CSLL")
        return head
    elif pos == 0:
        print(f"Node with value {value} added at begining position of a non-empty CSLL")
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
        newnode = Node(value)
        while i < pos-1:
            qtr = qtr.next
            ftr = ftr.next
            i += 1
        newnode.next = ftr
        qtr.next = newnode
        print(f"Node with value {value} added at position {pos} of an empty CSLL")
        return head
       
    else:
        print("Invalid position. No node added")
    
def delFromBigi(head):
    if head == None:
        print("LL empty. Nothing to delete")
        return None
    
    qtr = head
    ftr = qtr.next
    while ftr != head:
        ftr = ftr.next
        qtr = qtr.next

    qtr.next = ftr.next
    del ftr
    print("Node deleted from begining of a non-empty CSLL ")
    return qtr.next

def delFromEnd(head):
    if head == None:
        print("CSLL is empty. nothing to delete from end")
        return None
    qtr = head
    ftr = qtr.next

    while ftr.next != head:
        qtr = qtr.next
        ftr = ftr.next
    qtr.next = ftr.next
    del ftr
    print("Node deleted from End of a non-empty CSLL")
    return head

def delFromSpecificPos(head, pos):
    if head == None:
        print("CSLL is empty. Nothing to delete")
        return None
    elif pos == 0:
        print("Node deleted from begining position of a non-empty CSLL")
        return delFromBigi(head)
    
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
            ftr = ftr.next
            qtr = qtr.next
            i += 1
        qtr.next = ftr.next
        del ftr
        print(f"Node at position {pos} deleted from CSLL")
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
    print(f'{qtr.data}')
    print(f'Currently there are {count} nodes in the circularLL\n')

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
a = insInBtwn(a, 2, 15)
traverse(a)
a = delFromBigi(a)
a = delFromEnd(a)
a = delFromSpecificPos(a, 3)
traverse(a)

'''
OUTPUT:
10->20->30->40
Currently there are 4 nodes in the circularLL

Node with val 5 added at begining of a non-empty CSLL
Node with value 45 added at end of a non-empty CSLL
Node with value 15 added at position 2 of an empty CSLL
5->10->15->20->30->40->45
Currently there are 7 nodes in the circularLL

Node deleted from begining of a non-empty CSLL
Node deleted from End of a non-empty CSLL
Node at position 3 deleted from CSLL
10->15->20->40
Currently there are 4 nodes in the circularLL
'''