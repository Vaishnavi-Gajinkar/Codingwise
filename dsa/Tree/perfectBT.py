''' check if the tree is a perfect binary tree '''
''' i.e. nodes should have 0 or 2 children only & height of left tree = height of right tree '''

class Tree:
    data = None
    left = None
    right = None

    def __init__(self, data):
        self.data = data

def count_nodes(ptr, count=0):
    if ptr == None:
        return 0
    else:
        return 1+count_nodes(ptr.left)+count_nodes(ptr.right)             # 1 added to for root node countp

def calc_height(ptr, height=0):
    if ptr == None:
        return 0
    else:
        return 1+max(calc_height(ptr.left),calc_height(ptr.right))          # 1 added to for root node count

def isperfectBT(ptr, hyt, level=0):
    if ptr == None:
        return True
    elif ptr.left == None and ptr.right == None:
        return hyt == level+1
    elif ptr.left == None or ptr.right == None:
        return False
    return isperfectBT(ptr.left,hyt,level+1) and isperfectBT(ptr.right,hyt,level+1)


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

# c.left = f
# c.right = g

cnt = count_nodes(a)
print(f"There are {cnt} nodes in the binary tree")

hyt = calc_height(a)
print(f"Height of tree is {hyt}")

flag = isperfectBT(a, hyt, 0)
if flag == True:
    print("It is a Perfect Binary Tree")
else:
    print("It is not a Perfect Binary Tree")
    
'''
OUTPUT :
There are 7 nodes in the binary tree
Height of tree is 3
It is a Perfect Binary Tree
-----------------------------------------------
# if nodes are removed

There are 5 nodes in the binary tree
Height of tree is 3
It is not a Perfect Binary Tree
'''