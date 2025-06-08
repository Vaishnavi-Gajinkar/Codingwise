''' implement to check if the tree is actually a BST or not '''
# from BinSrchTree import BST

class Tree:
    data = None
    left = None
    right = None

    def __init__(self,data):
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
        return 1+max(calc_height(ptr.left), calc_height(ptr.right))
    
def getBSTdata(ptr, arr=[]):
    if ptr == None:
        return
    else:
        getBSTdata(ptr.left, arr)
        # print(ptr.data)
        arr.append(ptr.data)
        getBSTdata(ptr.right, arr)
    return arr
    # print(arr)
    # isBST(arr)


def isBST(arr):
    ''' checks if the ptr to tree is already a BST or not '''
    i = 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            break
    else:                                                       # executes if internal break not triggered 
        display(True)                                           # elements of array are sorted in asc
        return
    display(False)                                              # elements of array are not sorted


def display(result):
    if result:
        print("Tree is a BST\n")
    else:
        print("Tree is not a BST\n")


def BST(ptr, value):
    ''' create a BST if current tree is not one already '''
    if ptr == None:
        newnode = Tree(value)
        return newnode
    elif ptr.data > value:
        ptr.left = BST(ptr.left, value)
    elif ptr.data < value:
        ptr.right = BST(ptr.right, value)
    else:
        print("Nodes of a tree cannot have duplicate value")
    
    return ptr


l = Tree(10)
m = Tree(94)
n = Tree(41)
o = Tree(82)
p = Tree(77)
q = Tree(12)
r = Tree(76)
s = Tree(56)
t = Tree(34)
u = Tree(2)

l.left = m
l.right = n

m.left = o
m.right = p

n.left = q
n.right = r

o.left = s
o.right = t

p.left = u

print(f"Total nodes: {count_nodes(l)}\tTree height: {calc_height(l)}\n")
arr = []                                        # to collect node values of raw tree
arr = getBSTdata(l, arr)
print(arr)
res = isBST(arr)

if not res:                                     # creating a BST if not already
    newTree = None                              
    for val in arr:
        newTree = BST(newTree, val)

    newarr = []                                 # to collect node values of asc sorted tree
    newarr = getBSTdata(newTree, newarr)
    print(newarr)
    isBST(newarr)

'''
OUTPUT:
Total nodes: 10 Tree height: 4

[56, 82, 34, 94, 2, 77, 10, 12, 41, 76]
Tree is not a BST

[2, 10, 12, 34, 41, 56, 76, 77, 82, 94]
Tree is a BST

'''