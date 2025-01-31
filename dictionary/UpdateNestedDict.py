""" Update Nested Dictionary
- Problem: Add a key-value pair to a nested dictionary.
- Input: {"a": {"b": 1}}, key = "c", value = 2
- Output: {"a": {"b": 1, "c": 2}}
- Hint: Access the nested dictionary using its key.
"""

dnary = {"a": {"b": 1}}
key = "c"
val = 2

for k, v in dnary.items():
    pass
dnary["a"].update({key:val})

print(dnary)
