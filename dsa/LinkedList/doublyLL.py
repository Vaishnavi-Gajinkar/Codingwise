''' creating a doubly linked list '''

class Node:
    prev = None
    data = None
    next = None

    def __init__(self, data):
        self.data = data
        
def insertAtBigi(head, data):
    newnode = Node(data)

    if head == None:
        head = newnode
        print(f"Node {data} added in empty DLL (at begining)")
        return head
    
    newnode.next = head
    head.prev = newnode
    head = newnode
    print(f"Node {data} added at begining of DLL")
    return head

def insertAtEnd(head, data):
    newnode = Node(data)

    if head == None:
        head = newnode
        print(f"Node {data} added from end in the empty DLL")
        return head
    
    ptr = head
    while ptr.next != None:
        ptr = ptr.next
    newnode.prev = ptr
    ptr.next = newnode
    print(f"Node {data} added in DLL (from end)")
    return head

def insAtMid(head, pos, data):
    newnode = Node(data)

    if head == None:
        head = newnode
        print(f"Node {data} added to the empty DLL")
        return head
    elif pos == 0:
        newnode.next = head
        head.prev = newnode
        head = newnode
        print(f"Node {data} added in 0th position of DLL")
        return head
    
    ptr = head
    count = 0
    while ptr:
        count += 1
        ptr = ptr.next
    
    if pos <= count:
        qtr = head
        ftr = qtr.next
        i = 0

        while i < pos-1:
            qtr = qtr.next
            ftr = ftr.next
            i += 1
        if ftr == None:
            newnode.next = ftr
            newnode.prev = qtr
            qtr.next = newnode
            print(f"Node {data} added at end position of DLL")
            return head
        
        newnode.next = ftr
        newnode.prev = qtr
        qtr.next = newnode
        ftr.prev = newnode
        print(f"Node {data} added at {pos} position in non-empty DLL")
        return head
    else:
        print("Invalid Index. New node not added")
        return head

def insBeforeSval(head, sval, data):
    newnode = Node(data)

    if head == None:
        head = newnode
        print("node inserted before sval of empty DLL")
        return head
    elif head.data == sval:
        newnode.next = head
        head.prev = newnode
        head = newnode
        print("node inserted before sval of a non-empty DLL")
        return head
    
    ptr = head
    flag = False
    while ptr:
        if ptr.data == sval:
            # print('Search val found!')
            flag = True
            break
        ptr = ptr.next
    
    if flag:
        qtr = head
        ftr = qtr.next
        while ftr.data != sval:
            qtr = qtr.next
            ftr = ftr.next
        newnode.prev = qtr
        newnode.next = ftr
        qtr.next = newnode
        ftr.prev = newnode
        print("node inserted before sval of a non-empty DLL")
        return head
    
    else:
        print("search value not found")
        return head

def insAfterSval(head, sval, value):
    newnode = Node(value)

    if head == None:
        newnode.next = None
        head = newnode
        print("node inserted after sval of empty DLL")
        return head
    elif head.data == sval:
        newnode.prev = head
        head.next = newnode
        print("node inserted after sval of non-empty DLL")
        return head
    
    ptr = head
    flag = False
    while ptr:
        if ptr.data == sval:
            flag = True
            break
        ptr = ptr.next
    
    if flag:
        qtr = head
        ftr = qtr.next
        while qtr.data != sval:
            # print("QTR",qtr.prev,qtr.data,qtr.next)
            # print("FTR",ftr.prev,ftr.data,ftr.next)
            qtr = qtr.next
            ftr = ftr.next
        
            if ftr == None:
                newnode.prev = qtr
                newnode.next = ftr
                qtr.next = newnode
                print("node inserted after sval of non-empty DLL")
                return head
            newnode.prev = qtr
            newnode.next = ftr
            qtr.next = newnode
            ftr.prev = newnode
            return head
    else:
        print("search value not found")
        return head

def delFrmBigi(head):
    if head == None:
        print("DLL empty. Nothing to delete from begining")
        return None
    head = head.next
    head.prev = None
    print(f'node deleted from begining of DLL')
    return head

def delAtEnd(head):
    if head == None:
        print("DLL empty. Nothing to delete from End")
        return None
    elif head.next == None:
        print("Deleted the only node from DLL from end")
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
    print("Deleted the last node from DLL (from end)")
    return head

def delByPos(head,pos):
    if head == None:
        print("DLL empty. Nothing to delete by position")
        return None
    elif pos == 0:
        head = head.next
        head.prev = None
        print("Deleted the first node from DLL (by position)")
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
            print("deleted node from last index of DLL")
            return head
        
        qtr.next = ftr.next
        ftr.next.prev = qtr
        del ftr
        print("deleted node at the specified index")
        return head
    else:
        print("Invalid index, cannot be deleted")
        return head

def delByVal(head, sval):
    if head == None:
        print("DLL empty. Nothing to delete by value")
        return None
    elif head.data == sval:
        head = head.next
        head.prev = None
        print("Deleted the node at 0th index (by value)")
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
            print("deleted the last node in DLL (by value)")
            return head
        
        qtr.next = ftr.next
        ftr.prev = None
        ftr.next.prev = qtr
        del ftr
        print(f"deleted the node with value {sval}")
        return head
    else:
        print("Search value not found")
        return head

def traverse(head):
    ptr = qtr = head
    
    print('\nDLL in proper order has below data')
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

def digTraverse(head):
    ptr = qtr = head
    while ptr:
        print(f'{ptr.prev}\t{ptr.data}\t{ptr.next}')
        ptr = ptr.next

# a = Node(10)
# b = Node(20)
# a.next = b
# b.prev = a

a = None                                                            # TC 1 - checking if basic DLL getting created
for i in range(10,101,10):
    a = insertAtEnd(a, i)

traverse(a)
# digTraverse(a)

test1 = None                                                        # TC 2 - checking node addition from begining in empty DLL
test1 = insertAtBigi(test1, 1111)
traverse(test1)

a = insertAtBigi(a, 5)                                              # TC 3 - checking node addition from begining in a non-empty DLL

test2 = None                                                        # TC 4 - checking node addition from end in empty DLL
test2 = insertAtEnd(test2, 2222)
traverse(test2)

a = insertAtEnd(a, 105)                                             # TC 5 - checking node addition from end in a non-empty LL

test3 = None                                                        # TC 6 - inserting node at mid position when DLL is empty
test3 = insAtMid(test3, None, 3333)
traverse(test3)

a = insAtMid(a, 0, 1)                                               # TC 7 - inserting node at 0th position when LL is non-empty
a = insAtMid(a, 3, 15)                                              # TC 8 - inserting node at mid position when LL is non-empty
a = insAtMid(a, 14, 110)                                            # TC 9 - inserting node at end position using mid function in a non-empty LL
a = insAtMid(a, 999, 9999)                                          # TC10 - inserting node at an invalid position when LL is non-empty

test4 = None                                                        # TC11 - inserting node before search val when LL is empty
test4 = insBeforeSval(test4, None, 4444)
test4 = insBeforeSval(test4, 4444, 4440)                            # TC12 - inserting node before search val when head node matches search val
traverse(test4)

a = insBeforeSval(a, 150, 145)                                      # TC13 - inserting node before an invalid search value
a = insBeforeSval(a, 30, 25)                                        # TC14 - inserting node before search val when LL is not empty


test5 = None
test5 = insAfterSval(test5, None, 5555)                             # TC15 - inserting node after search val when LL is empty
test5 = insAfterSval(test5, 5555, 5559)                             # TC16 - inserting node after search val when LL is not empty
traverse(test5)

a = insAfterSval(a, 150, 155)                                       # TC17 - inserting node after an invalid search value
# a = insAfterSval(a, 30, 35)
# a = insAfterSval(a, 40, 45)
# traverse(a)

test6 = None                                                        # TC18 - deleting node from begining of an empty LL
test6 = delFrmBigi(test6)

a = delFrmBigi(a)                                                   # TC19 - deleting node from begining of a non-empty LL

test7 = None                                                        # TC20 - deleting node from end of an empty LL
test7 = delAtEnd(test7)

a = delAtEnd(a)                                                     # TC21 - deleting node from end of a non-empty LL

test8 = None                                                        # TC22 - deleting node from specific position of an empty LL
test8 = delByPos(test8, None)

a = delByPos(a, 0)                                                  # TC23 - deleting node from 0th position of a non-empty LL
a = delByPos(a, 7)                                                  # TC23 - deleting node from specific position of a non-empty LL
a = delByPos(a, 12)                  # check                        # TC23 - deleting node from last position of a non-empty LL
a = delByPos(a, 20)                                                 # TC24 - deletion from a specific position but with invalid index

test9 = None                                                        
test9 = delByVal(test9, 9999)                                       # TC25 - deletion of a node from an empty LL

a = delByVal(a, 10)                                                 # TC26 - delete a node with value at 0th position of LL
a = delByVal(a, 70)                                                 # TC27 - delete a node with a specific value in DLL
a = delByVal(a, 105)                                                # TC27 - delete a node with a value at end of DLL
traverse(a)
# digTraverse(a)

'''
OUTPUT :
Node 10 added from end in the empty DLL
Node 20 added in DLL (from end)
Node 30 added in DLL (from end)
Node 40 added in DLL (from end)
Node 50 added in DLL (from end)
Node 60 added in DLL (from end)
Node 70 added in DLL (from end)
Node 80 added in DLL (from end)
Node 90 added in DLL (from end)
Node 100 added in DLL (from end)

DLL in proper order has below data
None->10->20->30->40->50->60->70->80->90->100->None
DLL in reverse order has below data
None->100->90->80->70->60->50->40->30->20->10->None
Currently there are 10 nodes in the DLL
Node 1111 added in empty DLL (at begining)

DLL in proper order has below data
None->1111->None
DLL in reverse order has below data
None->1111->None
Currently there are 1 nodes in the DLL
Node 5 added at begining of DLL
Node 2222 added from end in the empty DLL

DLL in proper order has below data
None->2222->None
DLL in reverse order has below data
None->2222->None
Currently there are 1 nodes in the DLL
Node 105 added in DLL (from end)
Node 3333 added to the empty DLL

DLL in proper order has below data
None->3333->None
DLL in reverse order has below data
None->3333->None
Currently there are 1 nodes in the DLL
Node 1 added in 0th position of DLL
Node 15 added at 3 position in non-empty DLL
Node 110 added at end position of DLL
Invalid Index. New node not added
node inserted before sval of empty DLL
node inserted before sval of a non-empty DLL

DLL in proper order has below data
None->4440->4444->None
DLL in reverse order has below data
None->4444->4440->None
Currently there are 2 nodes in the DLL
search value not found
node inserted before sval of a non-empty DLL
node inserted after sval of empty DLL
node inserted after sval of non-empty DLL

DLL in proper order has below data
None->5555->5559->None
DLL in reverse order has below data
None->5559->5555->None
Currently there are 2 nodes in the DLL
search value not found
DLL empty. Nothing to delete from begining
node deleted from begining of DLL
DLL empty. Nothing to delete from End
Deleted the last node from DLL (from end)
DLL empty. Nothing to delete by position
Deleted the first node from DLL (by position)
deleted node at the specified index
Invalid index, cannot be deleted
Invalid index, cannot be deleted
DLL empty. Nothing to delete by value
Deleted the node at 0th index (by value)
deleted the node with value 70
deleted the last node in DLL (by value)

DLL in proper order has below data
None->15->20->25->30->40->50->80->90->100->None
DLL in reverse order has below data
None->100->90->80->50->40->30->25->20->15->None
Currently there are 9 nodes in the DLL
'''