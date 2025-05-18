''' Implement stack using a list '''

class stack:
    top = None
    arr = [None]
    size = None

    def __init__(self):
        self.top = -1
        self.size = 10
        self.arr = self.arr * self.size
    
def isEmpty(ptr):
    if ptr == None or ptr.top == -1:
        return True
    else:
        return False

def isFull(ptr):
    if ptr == None or ptr.top == (ptr.size)-1:
        return True
    else:
        return False
    
def push(ptr, data):
    if isFull(ptr):
        print("Stack is Full. cannot add the element",data)
        return ptr
    else:
        ptr.top += 1
        ptr.arr[ptr.top] = data
        return ptr

def pop(ptr):
    if isEmpty(ptr):
        print("Stack is Empty. cannot pop anything")
        return ptr
    else:
        val = ptr.arr[ptr.top] 
        ptr.arr[ptr.top]=None
        ptr.top -= 1
        print(f"Element {val} removed from stack top")
        return ptr

ptr = stack()
print(ptr.arr)
pop(ptr)
push(ptr,10)
push(ptr,20)
push(ptr,30)
push(ptr,40)
push(ptr,50)
push(ptr,60)
push(ptr,70)
push(ptr,80)
push(ptr,90)
push(ptr,100)
print(ptr.arr)
push(ptr,110)
pop(ptr)
pop(ptr)
print(ptr.arr)
push(ptr, 111)
print(ptr.arr)

'''
OUTPUT :
[None, None, None, None, None, None, None, None, None, None]
Stack is Empty. cannot pop anything
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Stack is Full. cannot add the element 110
Element 100 removed from stack top
Element 90 removed from stack top
[10, 20, 30, 40, 50, 60, 70, 80, None, None]
[10, 20, 30, 40, 50, 60, 70, 80, 111, None]
'''