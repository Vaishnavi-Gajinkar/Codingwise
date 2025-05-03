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
    print(f'There are {counter} nodes in linkedlist at present')
    return

def traverse(head): 
    count(head)                             # calling the count function
    ptr = head
    while ptr != None:
        print(ptr.data,end="->")
        ptr = ptr.next
    print("None\n")
    return head

def insertAtBigi(head, data):
    newnode = Node(data)

    if head == None:
        head = newnode
        print("\nNode inserted at begining when LL was empty")
        return head
    else:
        newnode.next = head
        head = newnode
        print("\nNode inserted at begining when LL wasn't empty")
        return head

def insertEnd(head, data):
    newnode = Node(data)
    
    if head == None:
        head = newnode
        print("\nInsert from end when LL is empty")
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
    newnode = Node(data)
    if head == None:
        newnode.next = head
        head = newnode
        return head   
    
    elif pos == 0:
        newnode.next = head
        head = newnode
        return head
    
    count = 0
    ptr = head
    while ptr:
        count += 1
        ptr = ptr.next
         
    if pos <= count:
        i = 0
        qtr = head
        ftr = qtr.next
        while i < pos-1:                                # bring ftr to the insertion index / pos
            qtr = qtr.next
            ftr = ftr.next
            i += 1
        newnode.next = ftr
        qtr.next = newnode
        return head
    else:
        print("Invalid index.")
        return head

def insertB4val(head, sval, data):
    newnode = Node(data)
    if head == None:
        head = newnode
        print("Inserted node (before sval) in an empty LL")
        return head
    elif head.data == sval:
        newnode.next = head
        head = newnode
        print("Inserted node before head node in LL")
        return head

    flag = False                                    # checking if search value is present in LL
    ptr = head
    while ptr != None:                              
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
    else:
        print('Search value is not present')
        return head

def insertAftVal(head, sval, data):
    newnode = Node(data)

    if head == None:
        head = newnode
        print("Inserted node (after sval) in an empty LL")
        return head
    elif head.data == sval:
        head.next = newnode
        print("Inserted node after head node in LL")
        return head
    
    ptr = head                                      # checking if search value is present
    flag = False
    while ptr:
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
    else:
        print("Search value not found")
        return head

def delAtBigi(head):
    if head == None:
        print("LL is empty. Nothing to delete")
        return traverse(head)
    head = head.next
    print('Node at 1st position deleted')
    return traverse(head)

def delAtEnd(head):
    if head == None:
        print("LL is empty. Nothing to delete")
        return traverse(head)
    qtr = head
    ftr = qtr.next
    while ftr.next:
        qtr = qtr.next
        ftr = ftr.next
    qtr.next = ftr.next
    # del ftr

    return traverse(head)
 
def delAtBtwn(head, pos):
    if head == None:
        print("LL is empty. Nothing to delete")
        return traverse(head)
    elif pos == 0:
        head = head.next
        return traverse(head)
    
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
            i += 1
        qtr.next = ftr.next
        del ftr
        return traverse(head)
    else:
        print("Invalid position")
        return traverse(head)

def delAVal(head, sval):
    if head == None:
        print("LL is empty. Searched value cannot be deleted")
        return traverse(head)
    elif head.data == sval:
        head = head.next
        return traverse(head)
    
    flag = False
    copyptr = head
    while copyptr:
        if copyptr.data == sval:
            flag = True
            break
        copyptr = copyptr.next
    if flag:
        qtr = head
        ftr = qtr.next
        while ftr.data != sval:
            qtr = qtr.next
            ftr = ftr.next
        qtr.next = ftr.next
        del ftr
        return traverse(head)
    else:
        print(f"No deletion. Value {sval} not found")
        return traverse(head)

# a = Node(10)
# b = Node(20)
# c = Node(30)

# a.next = b
# b.next = c
# c.next = None

a = None                                                # TC 1 - checking if basic LL getting created
for i in range(10,51,10):
    a = insertEnd(a, i)

traverse(a)

test1 = None                                            # TC 2 - checking node addition from begining in empty LL
test1 = insertAtBigi(test1, 1111)
traverse(test1)

a = insertAtBigi(a , 5)                                 # TC 3 - checking node addition from begining in a non-empty LL
traverse(a)

test2 = None                                            # TC 4 - checking node addition from end in empty LL
test2 = insertEnd(test2, 2222)
traverse(test2)

a = insertEnd(a, 60)                                    # TC 5 - checking node addition from end in a non-empty LL
traverse(a)

test3 = None
test3 = insertMid(test3, None, 3333)                    # TC 6 - inserting node at mid position when LL is empty
test3 = insertMid(test3, 0, 3330)                       # TC 7 - inserting node at 0th position when LL is non-empty
traverse(test3)

a = insertMid(a, 4, 35)                                 # TC 8 - inserting node at mid position when LL is non-empty
a = insertMid(a, 8, 65)                                 # TC 9 - inserting node at end position using mid function in a non-empty LL
a = insertMid(a, 15, 1500)                              # TC10 - inserting node at an invalid position when LL is non-empty

test4 = None
test4 = insertB4val(test4, 20, 4444)                    # TC11 - inserting node before search val when LL is empty
test4 = insertB4val(test4, 4444, 4440)                  # TC12 - inserting node before search val when head node matches search val
test4 = insertB4val(test4, 20, 4567)                    # TC13 - inserting node before an invalid search value
traverse(test4)

a = insertB4val(a, 20, 15)                              # TC14 - inserting node before search val when LL is not empty
a = insertB4val(a, 5, 4)
a = insertB4val(a, 60, 55)

test5 = None
test5 = insertAftVal(test5, None, 5555)                 # TC15 - inserting node after search val when LL is empty
test5 = insertAftVal(test5, 5555, 5559)                 # TC16 - inserting node after search val when LL is not empty
traverse(test5)

a = insertAftVal(a, 65, 70)
a = insertAftVal(a, 90, 25)                             # TC17 - inserting node after an invalid search value

traverse(a)

test6 = None
delAtBigi(test6)                                        # TC18 - deleting node from begining of an empty LL
a = delAtBigi(a)                                        # TC19 - deleting node from begining of a non-empty LL

test7 = None
test7 = delAtEnd(test7)                                 # TC20 - deleting node from end of an empty LL
a = delAtEnd(a)                                         # TC21 - deleting node from end of a non-empty LL

test8 = None
test8 = delAtBtwn(test8, 2)                             # TC22 - deleting node from specific position of an empty LL
a = delAtBtwn(a, 0)                                     # TC23 - deleting node from specific position of a non-empty LL
a = delAtBtwn(a, 8)
a = delAtBtwn(a, 12)                                    # TC24 - deletion from a specific position but with invalid index

test9 = None
test9 = delAVal(test9, 9999)                            # TC25 - deletion of a node from an empty LL
a = delAVal(a, 10)                                      # TC26 - delete a node with value at 0th position of LL
a = delAVal(a, 65)                                      # TC27 - delete a node with a specific value in LL

# OUTPUT :

'''PS C:path
Insert from end when LL is empty
There are 5 nodes in linkedlist at present
10->20->30->40->50->None


Node inserted at begining when LL was empty
There are 1 nodes in linkedlist at present
1111->None


Node inserted at begining when LL wasn't empty
There are 6 nodes in linkedlist at present
5->10->20->30->40->50->None


Insert from end when LL is empty
There are 1 nodes in linkedlist at present
2222->None

There are 7 nodes in linkedlist at present
5->10->20->30->40->50->60->None

There are 2 nodes in linkedlist at present
3330->3333->None

Invalid index.
Inserted node (before sval) in an empty LL
Inserted node before head node in LL
Search value is not present
There are 2 nodes in linkedlist at present
4440->4444->None

Inserted node before head node in LL
Inserted node (after sval) in an empty LL
Inserted node after head node in LL
There are 2 nodes in linkedlist at present
5555->5559->None

Search value not found
There are 13 nodes in linkedlist at present
4->5->10->15->20->30->35->40->50->55->60->65->70->None

LL is empty. Nothing to delete
There are 0 nodes in linkedlist at present
None

Node at 1st position deleted
There are 12 nodes in linkedlist at present
5->10->15->20->30->35->40->50->55->60->65->70->None

LL is empty. Nothing to delete
There are 0 nodes in linkedlist at present
None

There are 11 nodes in linkedlist at present
5->10->15->20->30->35->40->50->55->60->65->None

LL is empty. Nothing to delete
There are 0 nodes in linkedlist at present
None

There are 10 nodes in linkedlist at present
10->15->20->30->35->40->50->55->60->65->None

There are 9 nodes in linkedlist at present
10->15->20->30->35->40->50->55->65->None

Invalid position
There are 9 nodes in linkedlist at present
10->15->20->30->35->40->50->55->65->None

LL is empty. Searched value cannot be deleted
There are 0 nodes in linkedlist at present
None

There are 8 nodes in linkedlist at present
15->20->30->35->40->50->55->65->None

There are 7 nodes in linkedlist at present
15->20->30->35->40->50->55->None
'''