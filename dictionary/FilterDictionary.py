"""Filter Dictionary
- Problem: Filter keys with values > 2.
- Input: {"a": 1, "b": 3}, threshold = 2
- Output: {"b": 3}
- Hint: Use dictionary comprehension.
"""

dnary = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
thrshold = 2
dict = {}
for key, val in dnary.items():
    if val > thrshold:
        dict[key] = val

print(dict)

# Dictionary Comprehension
thshold = {key:val for key, val in dnary.items() if val > 2}
print(thshold)