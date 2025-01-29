""" Combine Dictionaries
- Problem: Add values of matching keys.
- Input: {"a": 1, "b": 2}, {"a": 3, "c": 4}
- Output: {"a": 4, "b": 2, "c": 4}
- Hint: Use a loop.
"""

dict1 = {"a": 1, "b": 2, "d": 5, "e": 3}
dict2 = {"e": 2, "a": 3, "c": 4, "d": 2}
combined = {}
for key1, val1 in dict1.items():
    for key2, val2 in dict2.items():
        if key1 == key2:
            combined[key1] = val1 + val2
        else:
            combined[key1] = val1
            combined[key2] = val2
print(dict1)
print(dict2)
print(combined)


# not solved