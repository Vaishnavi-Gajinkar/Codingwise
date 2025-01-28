""" Default Value for Missing Key
- Problem: Get the value for a key or print a default if not found.
- Input: {"a": 1, "b": 2}, key = "c", default = 0
- Output: 0
- Hint: Use dict.get(key, default).
"""

dnary = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

key = input('Enter key ')

print(dnary.get(key,0))
