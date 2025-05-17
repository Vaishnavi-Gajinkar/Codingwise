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

def delFrmBigi(head):
    if head == None:
        print("HSLL is empty. nothing to delete")
        return None
    if head.data == 1:
        head.next = None
        head.data = head.data -1
        print("Deleting the only node in HSLL from begining")
        return head
    
    qtr = head.next
    ftr = qtr.next
    head.next = ftr
    del qtr
    head.data = head.data -1
    print("Deleted a node from begining of HSLL")
    return head

def delFrmEnd(head):
    if head == None:
        print("HSLL is empty. Nothing to delete from end")
        return None
    qtr = head.next
    ftr = qtr.next
    while ftr.next != None:
        qtr = qtr.next
        ftr = ftr.next
    qtr.next = ftr.next
    del ftr
    head.data = head.data - 1
    print("Node deleted from end of HSLL")
    return head

def delByPos(head, pos):
    if head == None:
        print("HSLL empty. Nothing to delete")
        return None
    if pos == 0:
        return delFrmBigi(head)
    if pos == head.data-1:
        return delFrmEnd(head)
    if pos < head.data:
        qtr = head.next
        ftr = qtr.next
        i = 0
        while i < pos-1:
            qtr = qtr.next
            ftr = ftr.next
            i += 1
        qtr.next = ftr.next
        del qtr
        head.data = head.data - 1
        print(f"Node deleted from position {pos} of HSLL")
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

a = delFrmBigi(a)
a = delFrmEnd(a)
a = delByPos(a, 5)
traverse(a)

'''
OUTPUT :
HDLL is empty. Nothing to display
Node added at end position of an empty SLL
Node added at begining of empty SLL
Node added at end position of non-empty SLL
Node added at end position of non-empty SLL
Node added at end position of non-empty SLL
Node added at end position of non-empty SLL
Node added at end position of non-empty SLL
Node added at end position of non-empty SLL
Node added at end position of non-empty SLL
Node added at end position of non-empty SLL
Node added at end position of non-empty SLL
Node added at begining of a non-empty SLL
Node added at position 4 of HSLL
Node added at end position of non-empty SLL
13--->5->10->20->30->35->40->50->60->70->80->90->100->105->None
Deleted a node from begining of HSLL
Node deleted from end of HSLL
Node deleted from position 5 of HSLL
10--->10->20->30->35->40->60->70->80->90->100->None
'''