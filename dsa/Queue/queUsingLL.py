''' Implement the queue datastructure using linked list '''

class Queue:
    data = None
    next = None

    def __init__(self, data):
        self.data = data

def isEmpty(ptr):
    if ptr == None:
        return True
    else:
        return False
    
def isFull(ptr):
    newnode = Queue("dummy val")
    if newnode == None:
        return True
    else:
        return False

def enqueue(head, value):
    if isFull(head):
        print("Queue is full now. cannot insert more nodes")
        return head
    elif head == None:
        newnode = Queue(value)
        head = newnode
        return head
    ptr = head
    while ptr.next:
        ptr = ptr.next
    newnode = Queue(value)
    ptr.next = newnode
    # print("Node appended to queue successfully")
    return head

def dequeue(head):
    if isEmpty(head):
        print("Queue empty. Nothing to dequeue")
        return head
    head = head.next
    print("Dequeued an element from queue")
    return head

def peek(head):
    if head == None:
        print("Queue is empty. nothing to display")
        return head
    ptr = head
    while ptr:
        print(ptr.data, end="-")
        ptr = ptr.next
    print("----")

def peekFront(head):
    if head == None:
        print("Nothing to peek front")
        return head
    print("Q peeked from front has", head.data)

def peekRear(head):
    if head == None:
        print("Nothing to peek end")
        return head
    while head.next:
        head = head.next
    print("Q peeked from  rear has", head.data)

q = None
peek(q)
peekFront(q)
peekRear(q)
dequeue(q)
q = enqueue(q, 10)
q = enqueue(q, 20)
q = enqueue(q, 30)
q = enqueue(q, 40)
q = enqueue(q, 50)
q = enqueue(q, 60)
q = enqueue(q, 70)

peek(q)

q = dequeue(q)
q = dequeue(q)

peek(q)
q = enqueue(q, 80)
peek(q)

peekFront(q)
peekRear(q)

'''
OUTPUT :
Queue is empty. nothing to display
Nothing to peek front
Nothing to peek end
Queue empty. Nothing to dequeue
10-20-30-40-50-60-70-----
Dequeued an element from queue
Dequeued an element from queue
30-40-50-60-70-----
30-40-50-60-70-80-----
Q peeked from front has 30
Q peeked from  rear has 80
'''