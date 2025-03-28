''' wap to delete the nodes with duplicate values of singly LL '''

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class SLL_duplicates:
    def __init__(self):
        self.head = None
        self.counter = 0
        self.newhead = None

    def insert_node(self, data):
        newnode = Node(data)

        if self.head == None:
            self.head = newnode
            print("Head node added successfully")
            self.counter += 1
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = newnode
        self.counter += 1

        # self.dupli_rem()

    def dupli_rem(self):
        org = self.head
        
        lst_with_dups = []
        while org is not None:
            lst_with_dups.append(org.value)
            org = org.next

        lst_wo_dups = []
        for val in lst_with_dups:
            if val not in lst_wo_dups:
                lst_wo_dups.append(val)

        new_count = len(lst_with_dups)-len(lst_wo_dups)

        for val in lst_wo_dups:
            nn = Node(val)
            if self.newhead == None:
                self.newhead = nn
            else:
                curr = self.newhead
                while curr.next is not None:
                    curr = curr.next
                curr.next = nn

        self.display(new_count)
        
    def display(self,new_count):
        ptr = self.head

        print(f'SLL with duplicates has {self.counter} nodes and it looks like below')
        while ptr is not None:
            print(ptr.value,end="->")
            ptr = ptr.next
        print("None")

        qtr = self.newhead

        print(f'SLL without duplicates has {new_count} nodes looks like below')
        while qtr is not None:
            print(qtr.value,end="->")
            qtr = qtr.next
        print("None")



obj = SLL_duplicates()
obj.insert_node(10)
obj.insert_node(10)
obj.insert_node(20)
obj.insert_node(20)
obj.insert_node(30)
obj.insert_node(30)
obj.insert_node(40)
obj.insert_node(40)

obj.dupli_rem()

# OUTPUT
'''
Head node added successfully
SLL with duplicates has 8 nodes and it looks like below
10->10->20->20->30->30->40->40->None
SLL without duplicates has 4 nodes looks like below
10->20->30->40->None

'''