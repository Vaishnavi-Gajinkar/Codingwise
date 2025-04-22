''' implement the insertion, deletion and traversal functions in a singly linkedlist. '''
''' consider exhaustive testcase scenarios for robustness '''

class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data

# counter = 0                                 
def count(head):                            # to keep track of node count 
    counter = 0
    ptr = head
    while ptr != None:
        counter += 1
        ptr = ptr.next
    print(f'\nThere are {counter} nodes in linkedlist at present')
    return

def traverse(head): 
    count(head)                             # calling the count function
    ptr = head
    while ptr != None:
        print(ptr.data,end="->")
        ptr = ptr.next
    print("None")

def insertAtBigi(head, data):
    newnode = Node(data)

    if head == None:
        head = newnode
        return head
    else:
        newnode.next = head
        head = newnode
        return head

def insertEnd(head, data):
    newnode = Node(data)
    
    if head == None:
        head = newnode
        return head
    qtr = head
    ftr = qtr.next
    while ftr != None:
        qtr = qtr.next
        ftr = ftr.next
    newnode.next = None
    qtr.next = newnode
    return head

def insertMid(head, pos, data):
    qtr = head
    if qtr == None:
        head = insertAtBigi(qtr, data)
        return head     #check
    elif pos == 0:
        head = insertAtBigi(qtr, data)
        return head

    i = 0
    ftr = qtr.next
    newnode = Node(data)
    while i < pos:
        qtr = qtr.next
        ftr = ftr.next
        i += 1
    newnode.next = ftr
    qtr.next = newnode

    return head


a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)

a.next = b
b.next = c
c.next = d
d.next = None

traverse(a)

a = insertAtBigi(a,5)
a = insertEnd(a,50)
a = insertMid(a, 0, 25)
traverse(a)