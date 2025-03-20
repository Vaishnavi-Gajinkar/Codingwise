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

    def add_mid(self, data, pos):
        newnode = Node(data)

        if self.head == None:
            self.head = newnode
            self.counter += 1
            return
        i = 1
        current = self.head
        while i <= pos:
            if current is None:
                print("Invalid position. Adding node at end by default.")
                self.add_end(data)
                break
            tail = current
            current = current.next                
            i += 1

            if self.counter == 1:                       # only one node exists in LL
                tail.next = newnode
                newnode.prev = tail
                self.counter += 1
            else:   
                newnode.next = tail.next                # multiple nodes exists in LL
                newnode.prev = tail
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
obj.add_mid(20,2)
obj.add_end(30)
obj.add_mid(50,3)
obj.display()

# not solved