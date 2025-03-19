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
        current = self.head
        print(f"\nNode with value {value} to be deleted...")

        if current == None:
            print("LL empty. Nothing to delete")
            return
        elif current.data == value:
            self.head = self.head.next              # deleting head node
        else:
            while current is not None:
                if current.data == value:
                    break
                tail = current
                current= current.next               # deleting a non-head node
            tail.next = current.next

    def display(self):
        print("\nDisplaying the present state of list...")
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
obj.add_node(50)
obj.add_node(60)
obj.add_node(70)
obj.display()
obj.delete_node(10)
obj.display()
obj.delete_node(40)
obj.display()
obj.delete_node(70)
obj.display()

# OUTPUT :
"""
Displaying the present state of list...
LinkedList is empty

Displaying the present state of list...
10->20->30->40->50->60->70->None

Node with value 10 to be deleted...

Displaying the present state of list...
20->30->40->50->60->70->None

Node with value 40 to be deleted...

Displaying the present state of list...
20->30->50->60->70->None

Node with value 70 to be deleted...

Displaying the present state of list...
20->30->50->60->None

"""