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
        print("Added a node successfully. Updated LL looks as below")
        self.display()

    def del_bigi(self):
        current = self.head

        if self.head is None:
            print("DLL is empty. Nothing to delete")
            return
        self.head = current.next
        current = current.next
        current.prev = None

        self.counter -= 1
        print("Deleted the node from begining of LL. Updated LL looks as below")
        self.display()

    def del_end(self):
        current = self.head

        if current == None:
            print("LL empty. Nothing to delete")
            return
        while current.next is not None:
            tail = current
            current = current.next
        tail.next = current.next
        del current
        
        self.counter -= 1
        print("Deleted the node from end of LL. Updated LL looks as below")
        self.display()

    def del_by_val(self,data):
        current = self.head

        if self.head is None:
            print("DLL is empty. Nothing to delete ")
            return
        
        loc = -1
        ptr = current
        while ptr is not None:
            loc += 1
            if ptr.value == data:
                break
            ptr = ptr.next

        self.del_by_pos(loc)

    def del_by_pos(self,pos):
        current = self.head
              
        i = 0
        if self.head is None:
            print("LL empty. nothing to delete ")
            return
        elif pos == self.counter-1:
            self.del_end()
            return
        elif pos == 0:
            self.del_bigi()
            return
        elif pos<0 or pos >= self.counter:
            print(f"Invalid position {pos}")
            return
        while i < pos:
            tail = current
            current = current.next
            i += 1
        tail.next = current.next
        current.next.prev = tail
        self.counter -= 1
        print(f"Deleted the node at position {pos}.Updated LL looks as below")
        self.display()

    def display(self):
        current = self.head

        print("None",end="<-->")
        while current is not None:
            print(current.value,end="<-->")
            current = current.next
        print(f"None\t\t\tTotalNodeCount:{self.counter}")

    def disp_rev(self):
        current = self.head

        while current.next is not None:
            current = current.next
        print("\nDoubly LL in reverse order looks as below")
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

obj.del_bigi()
obj.del_end()
obj.del_by_pos(3)
obj.del_by_pos(5)
obj.disp_rev()

# OUTPUT : 
'''
Added a node successfully. Updated LL looks as below
None<-->10<-->20<-->None                        TotalNodeCount:2
Added a node successfully. Updated LL looks as below
None<-->10<-->20<-->30<-->None                  TotalNodeCount:3
Added a node successfully. Updated LL looks as below
None<-->10<-->20<-->30<-->40<-->None                    TotalNodeCount:4
Added a node successfully. Updated LL looks as below
None<-->10<-->20<-->30<-->40<-->50<-->None                      TotalNodeCount:5
Added a node successfully. Updated LL looks as below
None<-->10<-->20<-->30<-->40<-->50<-->60<-->None                        TotalNodeCount:6
Deleted the node from begining of LL. Updated LL looks as below
None<-->20<-->30<-->40<-->50<-->60<-->None                      TotalNodeCount:5
Deleted the node from end of LL. Updated LL looks as below
None<-->20<-->30<-->40<-->50<-->None                    TotalNodeCount:4
Deleted the node from end of LL. Updated LL looks as below
None<-->20<-->30<-->40<-->None                  TotalNodeCount:3
Invalid position 5

Doubly LL in reverse order looks as below
None<-->40<-->30<-->20<-->None
'''