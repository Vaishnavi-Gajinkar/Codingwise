''' Implement the functions of a queue using a list '''

class queue:
    arr = [None]
    front = None
    rear = None
    size = None

def isEmpty(ptr):
    if ptr.front == ptr.rear:
        return True
    else:
        return False

def isFull(ptr):
    if ptr.rear == ptr.size-1:
        return True
    else:
        return False

def enqueue(ptr, data):
    if isFull(ptr):
        print("Queue is full. Cannot append more elements")
        return ptr
    ptr.rear += 1
    ptr.arr[ptr.rear] = data
    return ptr

def dequeue(ptr):
    if isEmpty(ptr):
        print("Queue is empty. Nothing to dequeue.")
        return ptr
    ptr.front += 1
    ptr.arr[ptr.front] = None
    return ptr

def peekFront(ptr):
    if ptr == None:
        print("Queue empty. Nothing to display")
        return ptr
    elif ptr.front == ptr.rear:
        print("Reached end of queue now!")
    elif ptr.front != -1:
        print("Front of Queue:", ptr.arr[ptr.front+1])
    elif ptr.front == -1 or ptr.rear != -1:
        print("Front of Queue:", ptr.arr[0])
    else:
        print("Front of Queue:",ptr.arr[ptr.front])

def peekRear(ptr):
    if ptr == None:
        print("Queue empty. Nothing to display")
        return ptr
    print("Rear of Queue:",ptr.arr[ptr.rear])

q = queue()
q.size = 10
q.arr = q.arr * q.size
q.front = -1
q.rear = -1

print(q.arr)
peekFront(q)
peekRear(q)
q = enqueue(q, 10)
q = enqueue(q, 20)
q = enqueue(q, 30)
q = enqueue(q, 40)
q = enqueue(q, 50)
print(q.arr)
peekFront(q)
peekRear(q)
q = enqueue(q, 60)
q = enqueue(q, 70)
q = enqueue(q, 80)
q = enqueue(q, 90)
q = enqueue(q, 100)
# q = enqueue(q, 10)
print(q.arr)
peekFront(q)
peekRear(q)
q = dequeue(q)
q = dequeue(q)
q = dequeue(q)
q = dequeue(q)
print(q.arr)
peekFront(q)
peekRear(q)
q = dequeue(q)
q = dequeue(q)
q = dequeue(q)
q = dequeue(q)
q = dequeue(q)
q = dequeue(q)
# q = dequeue(q)
print(q.arr)
peekFront(q)
peekRear(q)

'''
OUTPUT:
[None, None, None, None, None, None, None, None, None, None]
Reached end of queue now!
Rear of Queue: None
[10, 20, 30, 40, 50, None, None, None, None, None]
Front of Queue: 10
Rear of Queue: 50
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Front of Queue: 10
Rear of Queue: 100
[None, None, None, None, 50, 60, 70, 80, 90, 100]
Front of Queue: 50
Rear of Queue: 100
[None, None, None, None, None, None, None, None, None, None]
Reached end of queue now!
Rear of Queue: None
'''