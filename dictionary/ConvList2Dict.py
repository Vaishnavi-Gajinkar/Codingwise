""" Convert List to Dictionary
- Problem: Convert a list of tuples to a dictionary.
- Input: [("a", 1), ("b", 2)]
- Output: {"a": 1, "b": 2}
- Hint: Use dict().
"""

lst_tup = [("a",1), ("b",2), ("c",3), ("d",4), ("e",5)]

converted = dict(lst_tup)

print(lst_tup)
print(converted)