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
    if (ptr.rear+1)%ptr.size == ptr.front:              # states that 1 cycle is completed
        return True
    else:
        return False

def enqueue(head, value):
    '''new values will be inserted/overwritten circularly until nothing is dequeued'''
    ptr = head
    if isFull(ptr):                                     
        print("Queue is full now. Cannot enqueue")          # will be true when dequeue starts
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

# def peek(ptr):
#     print(ptr.arr[ptr.front+1],end="-")
#     start = ptr.front+2
#     end = ptr.rear
#     while start < end:
#         print(ptr.arr[start],end="-")
#         start = (start+1)%ptr.size
#     print(ptr.arr[ptr.rear])
#     return ptr

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
cq = enqueue(cq, 105)                                   # overwrites as dequeue operation is not performed yet

print(cq.arr)

cq = dequeue(cq)
cq = dequeue(cq)

print(cq.arr)
cq = enqueue(cq, 110)
cq = enqueue(cq, 120)
cq = enqueue(cq, 130)
cq = enqueue(cq, 140)
cq = enqueue(cq, 150)
cq = enqueue(cq, 160)
cq = enqueue(cq, 170)
cq = enqueue(cq, 180)
cq = enqueue(cq, 190)
cq = enqueue(cq, 200)                                       # since front is moved and tried to rewrite, hence q Full error is displayed
print(cq.arr)
peekFront(cq)
peekRear(cq)

'''
OUTPUT:
Circular queue is empty. Nothing to dequeue
[105, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Element dequeued.
Circular queue is empty. Nothing to dequeue
[None, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Queue is full now. Cannot enqueue
[None, 110, 120, 130, 140, 150, 160, 170, 180, 190]
Peek front 110
Peek rear  190
'''