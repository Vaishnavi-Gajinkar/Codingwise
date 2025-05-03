""" insert a node at the begining, middle and end of a singly linked list """

class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class SLL_insert(object):
    def __init__(self):
        self.head = None
    
    def insert_end(self,data):
        newnode = Node(data)

        if self.head == None:
            self.head = newnode
            return
        current = self.head
        while current.next:
            current = current.next
        
        current.next = newnode

    def insert_mid(self,data,search):
        newnode = Node(data)

        current = self.head

        while current.value != search:
            current = current.next
        newnode.next = current.next
        current.next = newnode
    
    def insert_bigi(self,data):
        newnode = Node(data)

        current = self.head
        self.head = newnode
        newnode.next = current
    
    def display(self):
        current = self.head

        while current:
            print(current.value,end="->")
            current = current.next
        print("None")

    
obj = SLL_insert()
obj.insert_end(10)
obj.insert_end(20)
obj.insert_end(30)
obj.display()
print("Node Added at end position Successfully\n")
obj.insert_bigi(5)
obj.display()
print("Node Added at begining position Successfully\n")
obj.insert_mid(25,20)
obj.display()
print("Node Added at middle position Successfully\n")

'''
OUTPUT :
10->20->30->None
Node Added at end position Successfully

5->10->20->30->None
Node Added at begining position Successfully

5->10->20->25->30->None
Node Added at middle position Successfully
'''