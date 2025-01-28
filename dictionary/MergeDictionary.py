""" Merge Dictionaries
- Problem: Merge two dictionaries.
- Input: {"a": 1}, {"b": 2}
- Output: {"a": 1, "b": 2}
- Hint: Use dict1.update(dict2).
"""

dict1 = {'a':1, 'b':2}
dict2 = {'c':3, 'd':4}
#print(type(dict1),type(dict2))
dict1.update(dict2)
print(dict1)
