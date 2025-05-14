''' implement the insertion, deletion and traversal functions in a circular doubly linkedlist. '''
''' consider exhaustive testcase scenarios for robustness '''

class Node:
    prev = None
    data = None
    next = None

    def __init__(self, data):
        self.data = data

def insAtBigi(head, value):
    if head == None:
        newnode = Node(value)
        newnode.next = newnode
        newnode.prev = newnode
        print("Node added at begining of an empty CDLL")
        return newnode
    
    qtr = head
    ftr = head.next
    while ftr != head:
        qtr = qtr.next
        ftr = ftr.next
    
    newnode = Node(value)
    newnode.next = ftr
    newnode.prev = qtr
    ftr.prev = newnode
    qtr.next = newnode

    print("Node added at begining of a non-empty CDLL")
    return newnode

def insAtEnd(head, value):
    if head == None:
        newnode = Node(value)
        newnode.next = newnode
        newnode.prev = newnode
        print("Node added at end of an empty CDLL")
        return newnode
    
    qtr = head
    ftr = head.next
    while ftr != head:
        qtr = qtr.next
        ftr = ftr.next
    
    newnode = Node(value)
    newnode.next = ftr
    newnode.prev = qtr
    ftr.prev = newnode
    qtr.next = newnode

    print("Node added at end of a non-empty CDLL")
    return head

def insAtBetween(head, pos, value):
    if head == None:
        print("Node added at begining position of an empty CDLL")
        return insAtBigi(head, value)
    if pos == 0:
        print("Node added at begining position of an empty CDLL")
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
        while i < pos-1:
            qtr = qtr.next
            ftr = ftr.next
            i += 1
        newnode = Node(value)
        newnode.next = ftr
        newnode.prev = qtr
        qtr.next = newnode
        ftr.prev = newnode

        print(f"Node added at position {pos} of CDLL")
        return head

def delAtBigi(head):
    if head == None:
        print("CDLL is empty. Nothing to delete from begining")
        return None
    if head.next == head:
        del head
        print("Deleted the only node. CDLL is empty now")
        return None
    qtr = head
    ftr = qtr.next
    while ftr != head:
        qtr = qtr.next
        ftr = ftr.next

    qtr.next = ftr.next
    ftr.next.prev = qtr
    del ftr
    print("Node deleted from begining of CDLL")
    return qtr.next

def delFrmEnd(head):
    if head == None:
        print("CDLL empty. NOthing to delete from end")
        return None
    elif head.next == head:
        del head
        print("Deleted the only node from end. CDLL empty")
        return None
    
    qtr = head
    ftr = qtr.next
    while ftr.next != head:
        qtr = qtr.next
        ftr = ftr.next
    qtr.next = ftr.next
    head.prev = qtr
    del ftr
    print("Deleted the node from end of CDLL")
    return head

def delFrmBtwn(head, pos):
    if head == None:
        print(f"CDLL empty. Nothing to delete at position {pos}")
        return None
    if pos == 0:
        print(f"Deleted node from position {pos}")
        return delAtBigi(head)
    
    count = 1
    ptr = head.next
    while ptr!=head:
        count += 1
        ptr = ptr.next
    
    if pos<count:
        i = 0
        qtr = head
        ftr = qtr.next
        while i < pos-1:
            qtr = qtr.next
            ftr = ftr.next
            i += 1
        qtr.next = ftr.next
        ftr.next.prev = qtr
        del ftr
        print(f"Node deleted from position {pos} of CDLL")
        return head
    else:
        print("Invalid index. Nothing to delete")
        return head

def traverse(head):
    qtr = head.next
    print("CDLL in proper order is:")
    print(head.data,end="<->")
    while qtr.next!=head:
        print(qtr.data,end="<->")
        qtr = qtr.next
    print(qtr.data)

    print("CDLL in reverse order is:")
    qtr = head.prev
    while qtr != head:
        print(qtr.data, end="<->")
        qtr = qtr.prev
    print(qtr.data)

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)

a.prev = d
a.next = b

b.prev = a
b.next = c

c.prev = b
c.next = d

d.prev = c
d.next = a

traverse(a)
a = insAtBigi(a, 5)
a = insAtEnd(a, 50)
a = insAtBetween(a, 3, 25)
traverse(a)
a = delAtBigi(a)
a = delFrmEnd(a)
a = delFrmBtwn(a, 3)
traverse(a)




'''
OUTPUT :
CDLL in proper order is:
10<->20<->30<->40
CDLL in reverse order is:
40<->30<->20<->10
Node added at begining of a non-empty CDLL
Node added at end of a non-empty CDLL
Node added at position 3 of CDLL
CDLL in proper order is:
5<->10<->20<->25<->30<->40<->50
CDLL in reverse order is:
50<->40<->30<->25<->20<->10<->5
Node deleted from begining of CDLL
Deleted the node from end of CDLL
Node deleted from position 3 of CDLL
CDLL in proper order is:
10<->20<->25<->40
CDLL in reverse order is:
40<->25<->20<->10
'''