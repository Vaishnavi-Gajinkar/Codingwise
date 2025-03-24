""" delete a node from the begining, middle and end of a doubly linked list"""

class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

class Dll_addel():
    def __init__(self):
        self.head = None
        self.counter = 0

    def addnode(self, data):
        newnode = Node(data)

        if self.head == None:
            self.head = newnode
            self.counter += 1
            return
        current = self.head
        while current.next is not None:
            current = current.next
        newnode.prev = current
        current.next = newnode
        self.counter += 1

    def del_bigi(self):
        current = self.head

        if self.head is None:
            print("DLL is empty. Nothing to delete")
            return
        self.head = current.next
        current = current.next
        

    def del_end(self):
        pass

    def del_by_val(self,data):
        pass

    def del_by_pos(self,pos):
        pass

    def display(self):
        current = self.head

        print("None",end="<-->")
        while current is not None:
            print(current.value,end="<-->")
            current = current.next
        print("None")

    def disp_rev(self):
        current = self.head

        while current.next is not None:
            current = current.next
        
        print("None",end="<-->")
        while current is not None:
            print(current.value,end="<-->")
            current = current.prev
        print("None")

obj = Dll_addel()
obj.addnode(10)
obj.addnode(20)
obj.addnode(30)
obj.addnode(40)
obj.addnode(50)
obj.addnode(60)

obj.display()
obj.disp_rev()

# not solved