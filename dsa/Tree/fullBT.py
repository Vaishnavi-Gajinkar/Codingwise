''' check if the tree is a full binary tree '''
''' i.e. nodes should have 0 or 2 children only '''

class Tree:
    data = None
    left = None
    right = None

    def __init__(self, data):
        self.data = data

def count_nodes(root, count=0):
    if root == None:
        return 0
    else:
        return 1+count_nodes(root.left)+count_nodes(root.right)             # 1 added to for root node countp

def calc_height(ptr, height=0):
    if ptr == None:
        return 0
    else:
        return 1+max(calc_height(ptr.left),calc_height(ptr.right))          # 1 added to for root node count

def isFullBT(ptr):
    if ptr == None:                                     #pointer is below leaf node
        return True
    elif ptr.left == None and ptr.right == None:        #pointer is on leaf node
        return True
    elif ptr.left != None and ptr.right == None:        #node has left child only
        return False
    elif ptr.left == None and ptr.right != None:        #node has right child only
        return False
    elif ptr.left != None or ptr.right != None:         #node has 2 children
        return isFullBT(ptr.left) and isFullBT(ptr.right)


a = Tree(10)
b = Tree(20)
c = Tree(30)
d = Tree(40)
e = Tree(50)
f = Tree(60)
g = Tree(70)

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f
c.right = g

cnt = count_nodes(a)
print(f"There are {cnt} nodes in the binary tree")

hyt = calc_height(a)
print(f"Height of tree is {hyt}")

flag = isFullBT(a)
if flag == True:
    print("This is a Full Binary Tree")
else:
    print("This is not a Full Binary Tree")


'''
OUTPUT:
There are 7 nodes in the binary tree
Height of tree is 3
This is a Full Binary Tree
------------------------------------------------
# if one leaf node is removed

There are 6 nodes in the binary tree
Height of tree is 3
This is not a Full Binary Tree
'''