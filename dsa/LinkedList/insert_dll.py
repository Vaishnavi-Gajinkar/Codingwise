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
        
        if self.head == None:                       # TC : LL is empty
            self.head = newnode
            self.counter += 1
            return
        newnode.next = self.head                    # TC : LL exists
        newnode.prev = None
        self.head = newnode
        self.counter += 1

        print(f'Prev {newnode.prev} Next {newnode.next}')

    def add_end(self, data):
        newnode = Node(data)

        if self.head == None:                       # TC : LL is empty
            self.head = newnode
            self.counter += 1
            return
        current = self.head                         # TC : LL exists
        while current.next != None:
            current = current.next
        newnode.prev = current
        current.next = newnode
        self.counter += 1

        print(f'Prev {newnode.prev} Next {newnode.next}')
        
    def add_at_pos(self, data, pos):
        newnode = Node(data)

        count = 0                                   # to count the total nodes of the LL
        ptr = self.head
        while ptr is not None:                      
            ptr = ptr.next
            count += 1

        if self.head == None:                       # adding node if LL is empty
            self.head = newnode
            self.counter += 1
            return
        elif pos == 0:                              # adding node at 0th position
            self.add_bigi(data)
            return
        elif pos == count:                          # adding node at last position
            self.add_end(data)
            return
        elif pos >= count:                          # adding node at inexisting position
            print("Invalid position.")
            return
        
        i = 0                                       # adding node at a valid existing positon
        current = self.head  
        while i < pos:                              # situating tail at previous & current at next pos wrt new node
            tail = current                         
            current = current.next
            i += 1
        newnode.prev = tail
        newnode.next = current
        tail.next = newnode
        current.prev = newnode
        self.counter += 1
        
        print(f'Prev {newnode.prev} Next {newnode.next}')

    def add_b4_val(self,data,val):
        
        newnode = Node(data)

        search = 0                                   # checks if node with searching val exists
        ptr = self.head
        while ptr is not None:
            if ptr.value == val:
                break
            ptr = ptr.next
            search += 1
        else:
            print(f"Node with value {val} does not exist. Hence cannot add the new node with value {data}")
            return
        
        if search == 0:                             # search value found at 0th position
            self.add_bigi(data)
            return
        elif search == self.counter:                # search value found at last position
            self.add_end(data)
            return
        current = self.head                         # search value found at some mid position
        i = 0
        while i < search:
            tail = current
            current = current.next
            i += 1
        newnode.next = current
        newnode.prev = tail
        tail.next = newnode
        current.prev = newnode
        self.counter += 1
        
        print(f'Prev {newnode.prev} Next {newnode.next}')

    def display(self):
        current = self.head

        if self.head is None:
            print("LL Empty. Nothing to display")
            return
        print(f'There are {self.counter} nodes in the linked list as seen below')
        print("Proper LL\tNone",end="<-->")
        while current is not None:
            print(current.value,end="<-->")
            current = current.next
        print("None")

    def disp_rev(self):
        current = self.head

        while current.next is not None:
            current = current.next
        print("Reverse LL\tNone",end="<-->")
        while current.prev is not None:
            print(current.value,end="<-->")
            current = current.prev
        print("None")

obj = DLL_insert()
# obj.display()
obj.add_at_pos(20,0)
obj.add_bigi(10)
obj.add_end(30)
obj.add_end(40)
obj.add_at_pos(50,2)
# obj.display()
obj.add_b4_val(77,80)
# obj.display()
# obj.disp_rev()


#10-20-50-30-40

# not solved
