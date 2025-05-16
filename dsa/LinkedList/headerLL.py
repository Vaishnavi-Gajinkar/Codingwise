''' Implement the header linked list as a singly linked list '''
''' add the Add, Delete, Traverse functions in it '''
''' consider exhaustive TCs for robustness '''

class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data

def insAtBigi(head, value):
    if head == None:
        head = Node(1)
        newnode = Node(value)
        # head.data = head.data+1
        head.next = newnode
        print("Node added at begining of empty SLL")
        return head
    qtr = head.next
    newnode = Node(value)
    newnode.next = qtr
    head.next = newnode
    head.data = head.data+1
    print("Node added at begining of a non-empty SLL")
    return head

def insAtEnd(head, value):
    if head == None:
        print("Node added at end position of an empty SLL")

        return insAtBigi(head, value)
    qtr = head.next
    ftr = qtr.next
    while ftr != None:
        qtr = qtr.next
        ftr = ftr.next
    newnode = Node(value)
    qtr.next = newnode
    head.data = head.data+1
    print("Node added at end position of non-empty SLL")
    return head

def insAtBtwn(head, pos, value):
    if head == None:
        print("Node added at 0th pos of HSLL")
        return insAtBigi(head, value)
    if pos == head.data:
        return insAtEnd(head, value)
    
    if pos < head.data:
        i = 0
        qtr = head.next
        ftr = qtr.next
        while i < pos-1:
            qtr = qtr.next
            ftr = ftr.next
            i += 1
            # if ftr == None:
            #     qtr.next = newnode
            #     return head
        newnode = Node(value)
        newnode.next = ftr
        qtr.next = newnode
        head.data = head.data + 1
        print(f"Node added at position {pos} of HSLL")
        return head
    else:
        print("Invalid position. Node not added")
        return head

def traverse(head):
    if head == None:
        print("HDLL is empty. Nothing to display")
        return None
    else:
        qtr = head.next
        print(head.data,end="--->")
        while qtr != None:
            print(qtr.data,end="->")
            qtr = qtr.next
        print("None")
        return head

a = None
traverse(a)

for i in range(10,101,10):
    a = insAtEnd(a, i)

a = insAtBigi(a,5)
a = insAtBtwn(a, 4, 35)
a = insAtBtwn(a, 12, 105) 
traverse(a)

