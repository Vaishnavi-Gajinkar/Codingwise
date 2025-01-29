""" Dictionary to List
- Problem: Convert a dictionary to a list of tuples.
- Input: {"a": 1, "b": 2}
- Output: [("a", 1), ("b", 2)]
- Hint: Use dict.items().
"""

dnary = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
lst = []
converted = dict.items(dnary)

print(dnary)
print(converted)

for tup in converted:
    lst.append(tup)
print(lst)