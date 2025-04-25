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
    newnode = Node(data)
    if qtr == None:
        newnode.next = head
        head = newnode
        return head   
    
    elif pos == 0:
        newnode.next = head
        head = newnode
        return head

    i = 0
    ftr = qtr.next
    while i < pos-1:                                # bring ftr to the insertion index / pos
        qtr = qtr.next
        ftr = ftr.next
        i += 1
    newnode.next = ftr
    qtr.next = newnode

    return head

def insertB4val(head, sval, data):
    ptr = head
    newnode = Node(data)
    if ptr == None:
        head = newnode
        return head
    elif ptr.data == sval:
        newnode.next = head
        head = newnode
        return head
    
    flag = False
    ptr = head
    while ptr != None:                              # to check if value is present in LL
        if ptr.data == sval:
            flag = True
            break
        ptr = ptr.next
    
    if flag:                                        # add node before search val 
        qtr = head
        ftr = qtr.next
        while ftr.data != sval:
            qtr = qtr.next
            ftr = ftr.next
        newnode.next = ftr
        qtr.next = newnode
    return head

def insertAftVal(head, sval, data):
    ptr = head
    newnode = Node(data)

    if ptr == None:
        newnode.next = head
        head = newnode
        return head
    elif ptr.data == sval:
        newnode.next = head
        head = newnode
        return head
    
    flag = False
    while ptr != None:
        if ptr.data == sval:
            flag = True
            break
        ptr = ptr.next
    if flag:                                        # add node after search val
        qtr = head
        ftr = qtr.next
        while qtr.data != sval:
            qtr = qtr.next
            ftr = ftr.next
        newnode.next = ftr
        qtr.next = newnode

        return head

def delAtBigi(head):
    if head == None:
        print("LL is empty. Nothing to delete")
        return None
    head = head.next
    return head

def delAtEnd(head):
    if head == None:
        print("LL is empty. Nothing to delete")
        return None
    qtr = head
    ftr = qtr.next
    while ftr.next:
        qtr = qtr.next
        ftr = ftr.next
    qtr.next = ftr.next
    del ftr

    return head
 
def delAtBtwn(head, pos):
    if head == None:
        print("LL is empty. Nothing to delete")
        return None
    elif pos == 0:
        head = head.next
        return head
    
    count = 0
    copyptr = head
    while copyptr:
        count += 1
        copyptr = copyptr.next
        
    if count > pos:
        qtr = head
        ftr = qtr.next
        i = 0
        while i < pos-1: 
            qtr = qtr.next
            ftr = ftr.next
        qtr.next = ftr.next
        del ftr
        return head
    else:
        print("Invalid position")


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
a = insertMid(a, 0, 1)
a = insertB4val(a, 30, 25)
a = insertAftVal(a, 30, 35)
traverse(a)

#Output :

'''PS C:\Users\Lenovo\OneDrive\Documents\PythonPractise> & C:/Users/Lenovo/AppData/Local/Programs/Python/Python313/python.exe c:/Users/Lenovo/OneDrive/Documents/PythonPractise/CodingWise/dsa/LinkedList/singlyLL.py

There are 4 nodes in linkedlist at present
10->20->30->40->None

There are 9 nodes in linkedlist at present
1->5->10->20->25->30->35->40->50->None'''