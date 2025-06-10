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

def delFrmBST(ptr, value):
    if ptr == None:
        return None
    elif ptr.data > value:
        ptr.left = delFrmBST(ptr.left, value)
    elif ptr.data < value:
        ptr.right = delFrmBST(ptr.right, value)
    elif ptr.data == value:
        if ptr.left == None:
            temp = ptr.right
            ptr = None
            return temp
        elif ptr.right == None:
            temp = ptr.left
            ptr = None
            return temp
        else:
            temp = ptr.data
            ptr = ptr.left
            predd = Predecessor(ptr)
            






def inorder(ptr):
    if ptr == None:
        return
    else:
        inorder(ptr.left)
        print(ptr.data, end=", ")
        inorder(ptr.right)
    

arr = [int(x) for x in input("Enter node values of tree (comma seperated)").split(",")]

a = None
for val in range(len(arr)):
    a = createBST(a, arr[val])

print("Total nodes in tree -",count_nodes(a))
print("Height of tree is -",calc_height(a))
print(inorder(a))