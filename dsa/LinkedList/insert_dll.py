""" insert a node at the begining, middle and end of a doubly linked list """

class Node:
    def __init__(self,value):
        self.prev = None
        self.value = value
        self.next = None

class DLL_insert:
    counter = 0

    def __init__(self):
        self.head = None

    def add_bigi(self, data):
        newnode = Node(data)
        
        if self.head == None:
            self.head = newnode
            self.counter += 1
            return
        newnode.next = self.head
        self.head = newnode
        self.counter += 1

    def add_end(self, data):
        newnode = Node(data)

        if self.head == None:
            self.head = newnode
            self.counter += 1
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = newnode
        self.counter += 1

    def add_after_pos(self, data, pos):
        newnode = Node(data)

        if self.head == None:
            self.head = newnode
            self.counter += 1
            return
        
        count = 0
        ptr = self.head
        while ptr is not None:                      # counts the total nodes of the LL
            ptr = ptr.next
            count += 1
        if pos > count:
            print("Invalid position.")
            return
        
        i = 0
        current = self.head     
        while i < pos:
            tail = current
            current = current.next                
            i += 1
        newnode.prev = tail
        newnode.next = current
        tail.next = newnode
        current.prev = newnode
        self.counter += 1
        

        
    def display(self):
        current = self.head

        if self.head is None:
            print("LL Empty. Nothing to display")
            return
        print(f'There are {self.counter} nodes in the linked list as seen below')
        print("None",end="<-->")
        while current is not None:
            print(current.value,end="<-->")
            current = current.next
        print("None")

obj = DLL_insert()
obj.display()
obj.add_bigi(10)
obj.add_after_pos(20,2)
obj.add_end(30)
obj.add_after_pos(50,3)
obj.display()

# not solved