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
    # newnode.prev = None
    newnode.next = ptr
    ptr.prev = newnode
    head = newnode
    return head

def insertAtEnd(head, data):
    newnode = Node(data)

    if head == None:
        head = newnode
        return head
    
    ptr = head
    while ptr.next != None:
        ptr = ptr.next
    newnode.prev = ptr
    ptr.next = newnode
    return head

def insAtMid(head, pos, data):
    newnode = Node(data)

    ptr = head

    if head == None:
        head = newnode
        return head
    elif pos == 0:
        pointer = insertAtBigi(head, data)
        return pointer
        # newnode.next = head
        # head.prev = newnode
        # head = newnode
        # return head
    
    count = 0
    while ptr:
        count += 1
        ptr = ptr.next
    
    if pos <= count:
        qtr = head
        # print(qtr.data)
        ftr = qtr.next
        i = 0

        while i < pos-1:
            qtr = qtr.next
            ftr = ftr.next
            i += 1
        newnode.next = ftr
        newnode.prev = qtr
        qtr.next = newnode
        ftr.prev = newnode

        return head
    else:
        print("Invalid Index")
        return head

def insBeforeSval(head, sval, data):
    newnode = Node(data)
    ptr = head
    qtr = head
    ftr = qtr.next

    if head == None:
        newnode.next = head
        head = newnode
        return head
    elif head.data == sval:
        newnode.next = head
        head = newnode
        return head
    
    flag = False
    while ptr:
        if ptr.data == sval:
            # print('Search val found!')
            flag = True
            break
        ptr = ptr.next
    
    if flag:
        while ftr.data != sval:
            qtr = qtr.next
            ftr = ftr.next
        newnode.prev = qtr
        newnode.next = ftr
        qtr.next = newnode
        ftr.prev = newnode
        return head
    
    else:
        print("search value not found")
        return head

def insAfterSval(head, sval, data):
    newnode = Node(data)
    ptr = qtr = head
    ftr = qtr.next

    if head == None:
        newnode.next = head
        head = newnode
        return head
    elif head.data == sval:
        newnode.next = head.next
        newnode.prev = head
        head.next.prev = newnode
        head.next = newnode
        return head
    
    flag = False
    while ptr:
        if ptr.data == sval:
            flag = True
            break
        ptr = ptr.next
    
    if flag:
        while qtr.data != sval:
            qtr = qtr.next
            ftr = ftr.next
        
            if ftr == None:
                newnode.prev = qtr
                newnode.next = ftr
                qtr.next = newnode
                return head
            newnode.prev = qtr
            newnode.next = ftr
            qtr.next = newnode
            ftr.prev = newnode
            return head
    else:
        print("search value not found")

def delFrmBigi(head):
    if head == None:
        print("LL empty. Nothing to delete")
        return None
    head = head.next
    head.prev = None
    return head

def delAtEnd(head):
    if head == None:
        print("LL empty. Nothing to delete")
        return None
    elif head.next == None:
        print("Deleted the only node from LL")
        head = head.next
        return head
    qtr = head
    ftr = qtr.next
    while ftr.next:
        qtr = qtr.next
        ftr = ftr.next
    qtr.next = ftr.next
    ftr.prev = None
    del ftr
    return head

def delByPos(head,pos):
    if head == None:
        print("LL empty. Nothing to delete")
        return None
    elif pos == 0:
        head = head.next
        head.prev = None
        return head
    
    ptr = head
    count = 0
    while ptr:
        count += 1
        ptr = ptr.next
    
    if pos < count:
        i = 0 
        qtr = head
        ftr = qtr.next
        while i < pos-1:
            qtr = qtr.next
            ftr = ftr.next
            i += 1

        if ftr.next == None:
            qtr.next = ftr.next
            ftr.prev = None
            return head
        
        qtr.next = ftr.next
        ftr.next.prev = qtr
        del ftr
        return head
    else:
        print("Invalid index, cannot be deleted")
        return head

def delByVal(head, sval):
    if head == None:
        print("LL empty. Nothing to delete")
        return None
    elif head.data == sval:
        head = head.next
        return head
    
    flag = False
    ptr = head
    while ptr:
        if ptr.data == sval:
            flag = True
            break
        ptr = ptr.next
    
    if flag:
        qtr = head
        ftr = qtr.next
        while ftr.data != sval:
            qtr = qtr.next
            ftr = ftr.next

        if ftr.next == None:
            qtr.next = None
            del ftr
            return head
        
        qtr.next = ftr.next
        ftr.prev = None
        ftr.next.prev = qtr
        del ftr
        return head
    else:
        print("Search value not found")
        return head

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

    print(f'Currently there are {count} nodes in the DLL\n')

def digTraverse(head):
    ptr = qtr = head
    while ptr:
        print(f'{ptr.prev}\t{ptr.data}\t{ptr.next}')
        ptr = ptr.next

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
# digTraverse(a)
a = insertAtBigi(a, 5)
a = insertAtEnd(a, 45)
a = insAtMid(a, 0, 1)
a = insAtMid(a, 3, 15)
a = insAtMid(a, 25, 100)
a = insBeforeSval(a, 30, 25)
a = insBeforeSval(a, 50, 49)
a = insAfterSval(a, 30, 35)
a = insAfterSval(a, 45, 50)
# a = insAfterSval(a, 60, 61)
a = delFrmBigi(a)
a = delAtEnd(a)
a = delByPos(a, 8)
a = delByPos(a, 100)
a = delByVal(a, 15)
a = delByVal(a, 30)
a = delByVal(a, 100)
traverse(a)
# digTraverse(a)