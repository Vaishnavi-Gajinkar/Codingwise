""" delete a node from the begining, middle and end of a singly linked list"""

#from sll import Node, SLL

class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None

class Sll_addel:

    def __init__(self):
        self.head = None

    def add_node(self, value):
        newnode = Node(value)
        
        if self.head == None:
            self.head = newnode
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = newnode

    def delete_node(self,value):
        pass

    def display(self):

        if self.head is None:
            print("LinkedList is empty")
            return
        
        current = self.head
        while current:
            print(current.data,end="->")
            current = current.next
        print("None")

obj = Sll_addel()
obj.display()
obj.add_node(10)
obj.add_node(20)
obj.add_node(30)
obj.add_node(40)
obj.display()

# not solved