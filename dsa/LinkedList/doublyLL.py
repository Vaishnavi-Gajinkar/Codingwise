''' creating a doubly linked list '''

class Node:
    prev = None
    data = None
    next = None

    def __init__(self, data):
        self.data = data
        
def insertAtBigi(head, data):
    newnode = Node(data)
    ptr = head
    if head == None:
        newnode.next = head
        head = newnode
        return head
    
    newnode.next = head
    head.prev = newnode
    head = newnode
    return head

def insertAtEnd(head, data):
    newnode = Node(data)
    ptr = head

    if head == None:
        head = newnode
        return head
    while ptr.next != None:
        ptr = ptr.next
    newnode.prev = ptr
    ptr.next = newnode
    return head

def insAtMid(head, pos, data):
    newnode = Node(data)

    ptr = qtr = head

    if head == None:
        head = newnode
        return head
    elif pos == 0:
        insertAtBigi(head, data):
        return
    
    count = 0
    while ptr:
        count += 1
        ptr = ptr.next
    
    if pos <= count:
        ftr = qtr.next
        i = 0

        while i < pos-1:
            

def traverse(head):
    ptr = qtr = head
    
    print('DLL in proper order has below data')
    print('None',end='->')
    while ptr:
        print(ptr.data,end="->")
        ptr = ptr.next
    print('None')

    count = 0

    print('DLL in reverse order has below data\nNone',end='->')
    while qtr.next != None:
        qtr = qtr.next
    while qtr:
        print(qtr.data,end="->")
        qtr = qtr.prev
        count += 1
    print('None')

    print(f'Currently there are {count} nodes in the DLL')



a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)

a.next = b
b.prev = a
b.next = c
c.prev = b
c.next = d
d.prev = c

traverse(a)

a = insertAtBigi(a, 5)
a = insertAtEnd(a, 45)

traverse(a)