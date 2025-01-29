""" Reverse Dictionary
- Problem: Reverse the mapping, creating lists for duplicate values.
- Input: {"a": 1, "b": 2, "c": 1}
- Output: {1: ["a", "c"], 2: ["b"]}
- Hint: Use defaultdict(list).
"""

dnary = {"a": 1, "b": 2, "c": 1, "d": 2}
revDict = {}

for key, val in dnary.items():
    if val in revDict:
        revDict[val].append(key)
    else:
        revDict[val] = list(key)
print(revDict)