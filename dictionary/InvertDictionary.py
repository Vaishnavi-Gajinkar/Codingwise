""" Invert Dictionary
- Problem: Swap keys and values.
- Input: {"a": 1, "b": 2}
- Output: {1: "a", 2: "b"}
- Hint: Use dictionary comprehension.
"""

dnary = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
revDict = {}
for key, val in dnary.items():
    revDict[val] = key
print(revDict)

# Dictionary Comprehension 
pairev = {val:key for key,val in dnary.items()}
print(pairev)