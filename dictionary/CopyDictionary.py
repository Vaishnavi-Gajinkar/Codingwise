""" Copy Dictionary
- Problem: Create a copy of a dictionary.
- Input: {"a": 1, "b": 2}
- Output: {"a": 1, "b": 2}
- Hint: Use dict.copy().
"""

dnary = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
copy_dict = dnary.copy()

dnary.update([('f',6),('g',7)])

print(dnary)
print(copy_dict)