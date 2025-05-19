''' implement the stack data structure using a linked list '''

class stack:
    data = None
    next = None

    def __init__(self, data):
        self.data = data

def isEmpty(head):
    if head == None:
        return True
    else:
        return False

def isFull(head):
    newnode = stack(111)                # checking if harddrive mem is full
    if newnode == None:                 
        return True                     # ideally should never return true, unless no memory exists
    else:
        return False
    
def insAtEnd(head, value):
    if head == None or isFull(head):
        newnode = stack(value)
        head = newnode
        print("Node added in an empty stack")
        return head
    
    qtr = head
    while qtr.next != None:
        qtr = qtr.next
    newnode = stack(value)
    qtr.next = newnode
    print("Node added at stack top")
    return head

def delFrmEnd(head):
    if head == None or isEmpty(head):
        print("stack is empty. Nothing to pop")
        return head
    
    qtr = head
    ftr = qtr.next
    while ftr.next:
        qtr = qtr.next
        ftr = ftr.next
    val = ftr.data
    qtr.next = None
    del ftr
    print(f"Top node {val} deleted from stack")
    return head
    
def traverse(head):
    if head == None:
        print("Stack currently empty. Nothing to display")
        return head
    
    ptr = head
    count = 0
    while ptr:
        count += 1
        ptr = ptr.next
    print(f"Currently {count} node(s) exist in stack")
    
    qtr = head
    while qtr:
        print(qtr.data, end="->")
        qtr = qtr.next
    print("None")
    return head

def peek(head):
    qtr = head
    while qtr.next:
        qtr = qtr.next
    print(f'Stack Top value is {qtr.data}')
    print(f'Stack bottom value is {head.data}')

a = None
traverse(a)
a = insAtEnd(a, 10)
a = insAtEnd(a, 20)
a = insAtEnd(a, 30)
a = insAtEnd(a, 40)
a = insAtEnd(a, 50)
traverse(a)
a = delFrmEnd(a)
a = delFrmEnd(a)
traverse(a)
peek(a)


'''
OUTPUT :
Stack currently empty. Nothing to display
Node added in an empty stack
Node added at stack top
Node added at stack top
Node added at stack top
Node added at stack top
Currently 5 node(s) exist in stack
10->20->30->40->50->None
Top node 50 deleted from stack
Top node 40 deleted from stack
Currently 3 node(s) exist in stack
10->20->30->None
Stack Top value is 30
Stack bottom value is 10
'''