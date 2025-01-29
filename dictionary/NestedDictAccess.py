""" Nested Dictionary Access
- Problem: Access a value in a nested dictionary.
- Input: {"a": {"b": {"c": 1}}}, key = ["a", "b", "c"]
- Output: 1
- Hint: Use a loop over keys.
"""

dnary = {'a': {'b': {'c': 1}}}

for key1, val1 in dnary.items():
    for key2, val2 in val1.items():
        for key3, val3 in val2.items():
            print(val3)