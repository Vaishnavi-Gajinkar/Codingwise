''' implement to delete nodes of a BST '''
''' nodes can be leaf / one child parent / two child parent '''

# from BinSrchTree import BST, count_nodes, calc_height, inorder
# a = None
# a = BST(a, 9)
# b = BST(a, 11)
# c = BST(a, 13)
# a.left = b
# a.right = c

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
        return 1+ max(calc_height(ptr.left), calc_height(ptr.right))

def createBST(ptr, value):
    if ptr == None:
        newnode = Tree(value)
        return newnode
    elif ptr.data > value:
        ptr.left = createBST(ptr.left, value)
    elif ptr.data < value:
        ptr.right = createBST(ptr.right, value)

    return ptr

def predecessor(ptr):
    ptr = ptr.left
    while ptr.right != None:
        ptr = ptr.right
    return ptr

def successor(ptr):
    ptr = ptr.right
    while ptr.left != None:
        ptr = ptr.left
    return ptr


def delFrmBST(ptr, value, pref='s'):
    if ptr == None:
        return None
    elif ptr.data > value:
        ptr.left = delFrmBST(ptr.left, value, pref)
    elif ptr.data < value:
        ptr.right = delFrmBST(ptr.right, value, pref)
    else: #elif ptr.data == value:
        if ptr.left == None:
            temp = ptr.right
            ptr = None
            return temp
        
        if ptr.right == None:
            temp = ptr.left
            ptr = None
            return temp
        
        # if pref == 'p':
        #     predd = predecessor(ptr)
        #     ptr.data = predd.data

        #     ptr = ptr.left
        #     ptr = delFrmBST(ptr, predd.data, pref)
        #     return ptr 
        
        # elif pref == 's':
        succ = successor(ptr)
        ptr.data = succ.data

        ptr = ptr.right
        ptr = delFrmBST(ptr, succ.data, pref)
        return ptr


def inorder(ptr):
    if ptr == None:
        return
    else:
        inorder(ptr.left)
        print(ptr.data, end=", ")
        inorder(ptr.right)
    

arr = [int(x) for x in input("Enter node values of tree (comma seperated)").split(",")]

# a = Tree(10)
# b = Tree(94)
# c = Tree(41)
# d = Tree(82)
# e = Tree(77)
# f = Tree(12)
# g = Tree(76)
# h = Tree(56)
# i = Tree(34)
# j = Tree(2)

# a.left = b
# a.right = c

# b.left = d
# b.right = e

# c.left = f
# c.right = g

# d.left = h
# d.right = i

# e.left = j

a = None
for val in range(len(arr)):
    a = createBST(a, arr[val])

print("Total nodes in tree -",count_nodes(a))
print("Height of tree is -",calc_height(a))
print(inorder(a))

delVal = int(input("Enter ur val to be deleted "))
pref = input("Given a choice, would you prefer successor or predecessor ? ")
pref = pref[0].lower()
a = delFrmBST(a, delVal, pref)

print(inorder(a))

'''
OUTPUT :
Enter node values of tree (comma seperated)5,4,8,6,7,3,2
Total nodes in tree - 7
Height of tree is - 4
2, 3, 4, 5, 6, 7, 8, None
Enter ur val to be deleted 1
Given a choice, would you prefer successor or predecessor ? s
None
'''

# not solved