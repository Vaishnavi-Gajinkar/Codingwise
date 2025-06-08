''' take the nodes of a binary tree and convert it into binary search tree '''
''' BST has nodes in ascending order when traversed in inorder seq '''

class Tree:
    data = None
    left = None
    right = None

    def __init__(self, data):
        self.data = data

def count_nodes(ptr):
    if ptr == None:
        return 0
    else:
        return 1 + count_nodes(ptr.left) + count_nodes(ptr.right)
    
def calc_height(ptr):
    if ptr == None:
        return 0 
    else:
        return 1 + max(calc_height(ptr.left), calc_height(ptr.right))
    
# def inorder(ptr,arr):
#     if ptr == None:
#         return
#     else:
#         inorder(ptr.left, arr)
#         print(ptr.data, end=", ")
#         # arr.append[ptr.data]
#         inorder(ptr.right, arr)
#     return arr

def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.data] + inorder(root.right)


def BST(ptr, value):
    if ptr == None:
        newnode = Tree(value)
        return newnode
    elif ptr.data > value:
        ptr.left = BST(ptr.left, value)
    elif ptr.data < value:
        ptr.right = BST(ptr.right, value)
    else:
        print("Duplicate value not entertained😒")
    return ptr

a = Tree(10)
b = Tree(94)
c = Tree(41)
d = Tree(82)
e = Tree(77)
f = Tree(12)
g = Tree(76)
h = Tree(56)
i = Tree(34)
j = Tree(2)

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f
c.right = g

d.left = h
d.right = i

e.left = j

print("Node Count:",count_nodes(a)," Tree Height:",calc_height(a))

print("\nInorder traversal before BST:",end=" ")
res = inorder(a)
print("\n",res)

bst = None
print("\nInorder traversal after BST :",end=" ")
for i in res:
    bst = BST(bst, i)
res = inorder(bst)
print("\n",res)

'''
OUTPUT :
Node Count: 10  Tree Height: 4

Inorder traversal before BST:
 [56, 82, 34, 94, 2, 77, 10, 12, 41, 76]

Inorder traversal after BST :
 [2, 10, 12, 34, 41, 56, 76, 77, 82, 94]
 
'''