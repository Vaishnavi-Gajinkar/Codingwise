''' Implement a multistack using array '''

class stack:
    top1 = -1
    top2 = None
    data = None
    arr = [None]

    def __init__(self, data):
        self.size = 10
        self.top2 = self.arr.size()
        self.data = data
        arr = [None] * self.size

def isEmptyBigi(ptr):
    if ptr.top1 == -1:
        return True
    else:
        return False
    
def isEmptyEnd(ptr):
    if ptr.top2 == ptr.arr.size():
        return True
    else:
        return False

def isFullBigi(ptr):
    if ptr.top1 == ptr.top2:
        return True
    else:
        return False
    
def isFullEnd(ptr):
    if ptr.top2 == ptr.arr.size():
        return True
    else:
        return False
    
def pushBigi(ptr, value):
    if isFullBigi:
        print(f"Stack is full from start. Value {value} not pushed")
        return ptr
    else:
        ptr.top1 += 1
        ptr.arr[top1] = value
        print(f"Value {value} inserted in multistack")
        return ptr

def pushEnd(ptr, value):
    if isFullEnd:
        print(f"Stack is full from end. Value {value} not pushed")
        return ptr
    else:
        ptr.top2 -= 1
        ptr.arr[top2] = value
        print(f"Value {value} inserted in multistack")
        return ptr