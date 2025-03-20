''' creating a doubly linked list '''

class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None
    
    def addNode(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        
        current = self.head

        while current.next != None:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def display(self):
        current = self.head

        if current == None:
            print("DLL is empty. Nothing to display")
            return
        print("\nLL in proper order is\nNone<-->",end="")
        while current:
            print(current.value,end="<-->")
            current = current.next
        print("None")

    def disp_rev(self):
        current = self.head

        if self.head == None:
            print("LL is empty. Nothing to display")
            return
        print("\nLL in reverse order is\nNone<-->",end="")
        while current.next != None:
            current = current.next
        while current != None:
            print(current.value,end="<-->")
            current = current.prev
        print("None")

obj = DoublyLL()
obj.addNode(10)
obj.addNode(20)
obj.addNode(30)
obj.addNode(40)
obj.addNode(50)
obj.display()
obj.disp_rev()



# OUTPUT :
'''
LL in proper order is
None<-->10<-->20<-->30<-->40<-->50<-->None

LL in reverse order is
None<-->50<-->40<-->30<-->20<-->10<-->None
'''