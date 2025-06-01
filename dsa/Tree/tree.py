''' implement a simple tree data structure '''

class Tree:
    left = None
    right = None
    data = None

    def __init__(self, data):
        self.data = data
        
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

print(f'Root node a has value {a.data}')
print(f'Left of a is {a.left.data} and Right of a is {a.right.data}')
print(f'Left of b is {b.left.data} and Right of b is {b.right.data}')
print(f'Left of c is {c.left.data} and Right of c is {c.right.data}')
print(f'Left of d is {d.left.data} and Right of d is {d.right.data}')
print(f'Left of e is {e.left.data} and Right of e is {e.right.data}')
print(f'Left of f is {f.left} and Right of f is {f.right}')
print(f'Left of g is {g.left} and Right of g is {g.right}')
print(f'Left of h is {h.left} and Right of h is {h.right}')
print(f'Left of i is {i.left} and Right of i is {i.right}')
print(f'Left of j is {j.left} and Right of j is {j.right}')
print(f'Left of k is {k.left} and Right of k is {k.right}')