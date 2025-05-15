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
        head.data = 1
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

def traverse(head):
    if head == None:
        print("HDLL is empty. Nothing to display")
        return None
    else:
        qtr = head.next
        print(qtr.data,end="--->")
        while qtr != None:
            print(qtr.data,end="->")
            qtr = qtr.next
        print("None")
        return head

a = None
# b = Node(20)
# c = Node(30)
# d = Node(40)
# e = Node(50)
        
for i in range(10,101,10):
    a = insAtEnd(a, i)

traverse(a)