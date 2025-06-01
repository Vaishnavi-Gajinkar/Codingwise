''' implement the pre-order, in-order and post-order traversals in a binary tree '''

class Tree:
    left = None
    right = None
    data = None

    def __init__(self, data):
        self.data = data

def preorder(ptr):
    ''' displays the nodes of a tree in preorder sequence '''
    if ptr == None:
        return None
    print(ptr.data,end=" ")
    preorder(ptr.left)
    preorder(ptr.right)

def inorder(ptr):
    ''' displays the nodes of a tree in inorder sequence '''
    if ptr == None:
        return None
    preorder(ptr.left)
    print(ptr.data,end=" ")
    preorder(ptr.right)

def postorder(ptr):
    ''' displays the nodes of a tree in postorder sequence '''
    if ptr == None:
        return None
    preorder(ptr.left)
    preorder(ptr.right)
    print(ptr.data,end=" ")


a = Tree(10)
b = Tree(20)
c = Tree(30)
d = Tree(40)
e = Tree(50)
f = Tree(60)
g = Tree(70)
h = Tree(80)
i = Tree(90)
j = Tree(100)
k = Tree(110)

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f
c.right = g

d.left = h
d.right = i

e.left = j
e.right = k

print("-- Preorder sequence",preorder(a))
print("-- Inorder sequence",inorder(a))
print("-- Postorder sequence",postorder(a))


'''
OUTPUT:
10 20 40 80 90 50 100 110 30 60 70 -- Preorder sequence None
20 40 80 90 50 100 110 10 30 60 70 -- Inorder sequence None
20 40 80 90 50 100 110 30 60 70 10 -- Postorder sequence None
'''