""" Find Keys by Value
- Problem: Find all keys with a specific value.
- Input: {"a": 1, "b": 2, "c": 1}, value = 1
- Output: ["a", "c"]
- Hint: Use list comprehension.
"""

dnary = {"a": 1, "b": 2, "c": 1, "d": 2}
lst = []
tgt = 2

for key, val in dnary.items():
    if val == tgt:
        lst.append(key)
print(lst)

# -----Alternate way ---------------------------------------
lst_comp = [key for key,val in dnary.items() if val == tgt]
print(lst_comp)