""" Key Lookup
-- Problem: Find the value associated with a key in a dictionary.
-- Input: {"a": 1, "b": 2}, key = "b"
-- Output: 2
-- Hint: Use dict.get(key).
"""

dnary = {'a':1, 'b':2, 'c':3, 'd':4 }

tgt = 'b'

print(dnary.get(tgt,'key not found'))
