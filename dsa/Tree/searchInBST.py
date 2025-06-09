''' implement to search if a given node value is present in BST '''

class Tree:
    data = None
    left = None
    right = None

    def __init__(self, data):
        self.data = data

def getData(ptr, arr=[]):
    ''' returns array of nodes in the tree '''
    if ptr == None:
        return None
    else:
        getData(ptr.left, arr)
        arr.append(ptr.data)
        getData(ptr.right, arr)
    return arr

def isBST(arr):
    ''' checking if tree is a BST'''
    i = 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return(False)
    else:
        return(True)

def search(ptr, value):
    ''' searching the node value in BST '''
    if ptr == None:
        return False
    elif ptr.data == value:
        return True
    elif ptr.data > value:
        return search(ptr.left, value)
    elif ptr.data < value:
        return search(ptr.right, value)
    

def BST(ptr, value):
    ''' creating a BST from an array '''
    if ptr == None:
        newnode = Tree(value)
        return newnode
    elif ptr.data > value:
        ptr.left = BST(ptr.left, value)
    elif ptr.data < value:
        ptr.right = BST(ptr.right, value)
    else:
        print("No duplicates allowed in nodes of a tree")
    
    return ptr

def inorder(ptr):
    if ptr == None:
        return None
    else:
        inorder(ptr.left)
        print(ptr.data,end=", ")
        inorder(ptr.right)
    
def preorder(ptr):
    if ptr == None:
        return None
    else:
        print(ptr.data,end=", ")
        preorder(ptr.left)
        preorder(ptr.right)

def postorder(ptr):
    if ptr == None:
        return None
    else:
        postorder(ptr.left)
        postorder(ptr.right)
        print(ptr.data,end=", ")

a = Tree(5)                                         # nodes in BST seq
b = Tree(3)
c = Tree(8)
d = Tree(2)
e = Tree(4)
f = Tree(7)
g = Tree(9)


# a = Tree(10)                                      # nodes in random seq
# b = Tree(94)
# c = Tree(41)
# d = Tree(82)
# e = Tree(77)
# f = Tree(12)
# g = Tree(76)


a.left = b
a.right = c

b.left = d
b.right = e

c.left = f
c.right = g


print('Current nodes of the tree are ',getData(a))                  # displaying nodes of tree
serch_val = int(input("Enter a node value to search "))             # accepting a search value from user

arr = []
arr = getData(a, arr)
res = isBST(arr)            

if res:                                                             
    print("Searching directly in a BST")
    serch_res = search(a, serch_val)                                # searching in BST
else:
    print("Tree is not a BST. creating a BST and then searching")
    newtree = None
    for val in arr:
        newtree = BST(newtree, val)                                 # creating a BST
    newarr = []
    print(getData(newtree,newarr))                                  # searching in newly created BST
    serch_res = search(newtree, serch_val) 

if serch_res:
    print("Node exists in tree")
else:
    print("Node does not exist")

'''
OUTPUT :
# for nodes entered in BST sequence

Current nodes of the tree are  [2, 3, 4, 5, 7, 8, 9]
Enter a node value to search 5
Searching directly in a BST
Node exists in tree
------------------------------------
Current nodes of the tree are  [2, 3, 4, 5, 7, 8, 9]
Enter a node value to search 21
Searching directly in a BST
Node does not exist

----------------------------------------------------------------
# for nodes not entered in BST sequence

Current nodes of the tree are  [82, 94, 77, 10, 12, 41, 76]
Enter a node value to search 12
Tree is not a BST. creating a BST and then searching
[10, 12, 41, 76, 77, 82, 94]
Node exists in tree
------------------------------------
Current nodes of the tree are  [82, 94, 77, 10, 12, 41, 76]
Enter a node value to search 1
Tree is not a BST. creating a BST and then searching
[10, 12, 41, 76, 77, 82, 94]
Node does not exist
'''