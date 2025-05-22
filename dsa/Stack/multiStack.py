''' Implement a multistack using array '''

class stack:
    top1 = None
    top2 = None
    data = None
    arr = [None]
    size = None

def isEmptyBigi(ptr):
    if ptr.top1 == -1:
        return True
    else:
        return False
    
def isEmptyEnd(ptr):
    if ptr.top2 == ptr.size-1:
        return True
    else:
        return False

def isFull(ptr):
    if ptr.top1 +1 == ptr.top2:
        return True
    else:
        return False
    
# def isFullEnd(ptr):
#     if ptr.top2 == ptr.():
#         return True
#     else:
#         return False
    
def pushBigi(ptr, value):
    if isFull(ptr):
        print(f"Stack is full. Value {value} cannot be pushed from front")
        return ptr
    else:
        ptr.top1 += 1
        ptr.arr[ptr.top1] = value
        print(f"Value {value} inserted in multistack")
        return ptr

def pushEnd(ptr, value):
    if isFull(ptr):
        print(f"Stack is full. Value {value} cannot be pushed from end")
        return ptr
    else:
        ptr.top2 -= 1
        ptr.arr[ptr.top2] = value
        print(f"Value {value} inserted in multistack")
        return ptr
    
def popB(ptr):
    if isEmptyBigi(ptr):
        print("Stack is empty from begining. Nothing to pop")
        return ptr
    else:
        ptr.arr[ptr.top1] = None
        ptr.top1 -= 1
        print("Value popped from start of stack.")
        return ptr

def popE(ptr):
    if isEmptyEnd(ptr):
        print("Stack is empty from end. Nothing to pop")
        return ptr
    else:
        ptr.arr[ptr.top2] = None
        ptr.top2 += 1
        print("Value popped from end of stack.")
        return ptr

head = stack()
head.size = 10
head.arr = head.arr * head.size
head.top1 = -1
head.top2 = head.size

head = pushBigi(head, 10)
head = pushBigi(head, 20)
head = pushBigi(head, 30)
head = pushBigi(head, 40)
head = pushBigi(head, 50)

print(head.arr)

head = pushEnd(head, 100)
head = pushEnd(head, 90)
head = pushEnd(head, 80)
head = pushEnd(head, 70)
head = pushEnd(head, 60)

print(head.arr)
head = pushBigi(head, 111)

head = popB(head)
print(head.arr)

head = popE(head)
print(head.arr)

head = popB(head)
head = popB(head)
head = popB(head)
head = popB(head)
head = popB(head)
print(head.arr)

head = popE(head)
head = popE(head)
head = popE(head)
head = popE(head)

'''
OUTPUT :
Value 10 inserted in multistack
Value 20 inserted in multistack
Value 30 inserted in multistack
Value 40 inserted in multistack
Value 50 inserted in multistack
[10, 20, 30, 40, 50, None, None, None, None, None]
Value 100 inserted in multistack
Value 90 inserted in multistack
Value 80 inserted in multistack
Value 70 inserted in multistack
Value 60 inserted in multistack
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Stack is full. Value 111 cannot be pushed from front
Value popped from start of stack.
[10, 20, 30, 40, None, 60, 70, 80, 90, 100]
Value popped from end of stack.
[10, 20, 30, 40, None, None, 70, 80, 90, 100]
Value popped from start of stack.
Value popped from start of stack.
Value popped from start of stack.
Value popped from start of stack.
Stack is empty from begining. Nothing to pop
[None, None, None, None, None, None, 70, 80, 90, 100]
Value popped from end of stack.
Value popped from end of stack.
Value popped from end of stack.
Stack is empty from end. Nothing to pop
'''