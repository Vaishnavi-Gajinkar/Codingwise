''' sort the elements of a singly linked list '''

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class SLL_addsort:
    def __init__(self):
        self.head = None
        self.sorted_ptr = None
        self.counter = 0

    def addnode(self,data):
        newnode = Node(data)
        current = self.head

        if current == None:
            self.head = newnode
            return
        while current.next is not None:
            current = current.next
        current.next = newnode

        self.counter += 1
        print(f'Node with value {data} added successfully!')
        self.display()

    def create_sorted_ll(self,array):
        sptr = self.sorted_ptr
        for val in array:
            sorted_node = Node(val)
            if sptr == None:
                sptr = sorted_node
                print(sptr.next)
            else:
                while sptr.next is not None:
                    sptr = sptr.next
                sptr.next = sorted_node

        sptr = self.sorted_ptr
        print("Sorted LL looks as below")
        while sptr is not None:
            print(sptr.value,end="->")
            sptr = sptr.next
        # print("None")
        # self.display_sorted()

    def sort_asc(self):
        current = self.head
        arr = []

        while current is not None:
            arr.append(current.value)
            current = current.next
        print(arr)
        self.create_sorted_ll(sorted(arr))

    def display(self):
        ptr = self.head
        while ptr is not None:
            print(ptr.value,end="-->")
            ptr = ptr.next
        print("None")

    # def display_sorted(self):
    #     sptr = self.sorted_ptr
    #     print("Sorted LL looks as below")
    #     while sptr is not None:
    #         print(sptr.value,end="->")
    #         sptr = sptr.next
    #     print("None")

obj = SLL_addsort()
ask = [int(x) for x in input("Enter node values seperated by comma ").split(',') ]
for val in ask:
    obj.addnode(val)

obj.sort_asc()

# NOT SOLVED