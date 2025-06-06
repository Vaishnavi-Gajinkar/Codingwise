''' check if a tree is complete binary tree '''
''' i.e. nodes should be filled from left to right '''

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
        return 1+count_nodes(ptr.left)+count_nodes(ptr.right)
    
def calc_height(ptr):
    if ptr == None:
        return 0
    else:
        return 1+max(calc_height(ptr.left),calc_height(ptr.right))
    
def isCompleteBT(ptr,tot_nodes,index=0):
    if ptr == None:
        return True
    elif index >= tot_nodes:                    # check if nodes is always 1 greater than index
        return False
    return isCompleteBT(ptr.left,tot_nodes,index*2+1) and isCompleteBT(ptr.right,tot_nodes,index*2+2)   # formula to calc the index of CN is PN*2+1 or PN*2+2


a = Tree(10)
b = Tree(20)
c = Tree(30)
d = Tree(40)
e = Tree(50)
f = Tree(60)
g = Tree(70)
h = Tree(80)
i = Tree(90)

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f
c.right = g

d.left = h
# d.right = i

cnt = count_nodes(a)
hyt = calc_height(a)
print(f"Tree has {cnt} nodes")
print(f"Height of the tree is {hyt}")

if isCompleteBT(a,cnt,0):
    print("It is a complete binary tree")
else:
    print("It is not a complete binary tree")


'''
OUTPUT:
Tree has 9 nodes
Height of the tree is 4
It is a complete binary tree
--------------------------------------------------------------------------
# upon disbalancing the tree
Tree has 8 nodes
Height of the tree is 4
It is not a complete binary tree
'''