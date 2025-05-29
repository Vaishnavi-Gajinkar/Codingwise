''' Implement a circular queue using a list/array '''

class CircQ:
    front = None
    rear = None
    arr = [None]
    size = None

def isEmpty(ptr):
    if ptr.rear == ptr.front:
        return True
    else:
        return False

def isFull(ptr):
    if ptr.rear+1 == ptr.front:
        return True
    else:
        return False

def enqueue(head, value):
    ptr = head
    if isFull(ptr):
        print("Queue is full now. Cannot enqueue")
        return ptr
    ptr.rear = (ptr.rear+1)%(ptr.size)
    ptr.arr[ptr.rear] = value
    return head

def dequeue(head):
    ptr = head
    if isEmpty(ptr):
        print("Circular queue is empty. Nothing to dequeue")
        return ptr
    ptr.front = (ptr.front + 1) % ptr.size
    ptr.arr[ptr.front] = None
    print("Element dequeued.")
    return head

def peek(ptr):
    print(ptr.arr[ptr.front+1],end="-")
    start = ptr.front+2
    end = ptr.rear
    while start < end:
        print(ptr.arr[start],end="-")
        start = (start+1)%ptr.size
    print(ptr.arr[ptr.rear])
    return ptr

def peekFront(ptr):
    print("Peek front",ptr.arr[ptr.front+1])
    return

def peekRear(ptr):
    print("Peek rear ",ptr.arr[ptr.rear])
    return


cq = CircQ()
cq.front = -1
cq.rear = -1
cq.size = 10
cq.arr = cq.arr * cq.size

cq = dequeue(cq)
cq = enqueue(cq, 10)
cq = enqueue(cq, 20)
cq = enqueue(cq, 30)
cq = enqueue(cq, 40)
cq = enqueue(cq, 50)
cq = enqueue(cq, 60)
cq = enqueue(cq, 70)
cq = enqueue(cq, 80)
cq = enqueue(cq, 90)
cq = enqueue(cq, 100)

print(cq.arr)
peek(cq)

cq = dequeue(cq)
cq = dequeue(cq)
cq = dequeue(cq)
cq = dequeue(cq)
print(cq.arr)
cq = enqueue(cq, 110)
cq = enqueue(cq, 120)
print(cq.arr)
peek(cq)
peekFront(cq)
peekRear(cq)

'''
OUTPUT:
Circular queue is empty. Nothing to dequeue
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
10-20-30-40-50-60-70-80-90-100
Element dequeued.
Element dequeued.
Element dequeued.
Element dequeued.
[None, None, None, None, 50, 60, 70, 80, 90, 100]
[110, 120, None, None, 50, 60, 70, 80, 90, 100]
50-120
Peek front 50
Peek rear  120
'''