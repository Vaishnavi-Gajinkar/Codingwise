''' creating a singly linked list '''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def add_node(self,data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode


    def display(self):
        current = self.head
        while current.next:
            print(current.value,end=" -> ")
            current = current.next
        print('None')

sll = SLL()
sll.add_node(10)
sll.add_node(20)
sll.add_node(30)
sll.add_node(40)
sll.display()