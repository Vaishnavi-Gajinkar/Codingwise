''' implement the functions of a double ended queue '''

class DQ:
    arr = []
    size = None

def isEmpty(ptr):
    if len(ptr.arr) == 0:                       # array will be empty if len(array) is 0
        return True
    else:
        return False

def isFull(ptr):
    if len(ptr.arr) == ptr.size:            # array will be full when len(array) is eq to size
        return True
    else:
        return False

def enqueueBigi(ptr, data):                         #adding element from begining of DeQueue
    if isFull(ptr):
        print("DQueue is full. cannot enqueue")
        return ptr
    ptr.arr.insert(0,data)
    return ptr

def enqueueEnd(ptr, data):                          #adding element from end of DeQueue
    if isFull(ptr):
        print("DQueue is full. cannot enqueue")
        return ptr
    ptr.arr.append(data)
    return ptr

def deqBigi(ptr):                                   #deleting element from begining of DeQueue
    if isEmpty(ptr):
        print("DQueue is empty. nothing to dequeue")        
        return ptr
    del ptr.arr[0]
    return ptr

def deqEnd(ptr):                                    #deleting element from end of DeQueue
    if isEmpty(ptr):
        print("DQueue is empty. nothing to dequeue")        
        return ptr
    del ptr.arr[len(ptr.arr)-1]
    return ptr
    
def peek(ptr):                                      #displaying all elements of queue as an array
    if isEmpty(ptr):
        print("DQueue is empty. nothing to show")
        return
    print(ptr.arr)
    return

dq = DQ()
dq.size = 10
dq.arr = dq.arr * dq.size

peek(dq)
dq = enqueueBigi(dq, 10)
dq = enqueueBigi(dq, 20)
dq = enqueueBigi(dq, 30)
dq = enqueueBigi(dq, 40)
dq = enqueueBigi(dq, 50)
dq = enqueueEnd(dq, 60)
dq = enqueueEnd(dq, 70)
dq = enqueueEnd(dq, 80)
dq = enqueueEnd(dq, 90)
dq = enqueueEnd(dq, 100)

dq = enqueueBigi(dq, 50)
dq = enqueueEnd(dq, 105)
peek(dq)
dq = deqBigi(dq)
dq = deqBigi(dq)
peek(dq)
dq = deqEnd(dq)
dq = deqEnd(dq)
peek(dq)
dq = deqEnd(dq)
dq = deqEnd(dq)
dq = deqEnd(dq)
dq = deqEnd(dq)
dq = deqEnd(dq)
dq = deqEnd(dq)

dq = deqBigi(dq)
dq = deqEnd(dq)
peek(dq)

'''
OUTPUT :
DQueue is empty. nothing to show
DQueue is full. cannot enqueue
DQueue is full. cannot enqueue
[50, 40, 30, 20, 10, 60, 70, 80, 90, 100]
[30, 20, 10, 60, 70, 80, 90, 100]
[30, 20, 10, 60, 70, 80]
DQueue is empty. nothing to dequeue
DQueue is empty. nothing to dequeue
DQueue is empty. nothing to show
'''