""" Check Key Existence
- Problem: Check if a key exists in a dictionary.
- Input: {"a": 1, "b": 2}, key = "c"
- Output: False
- Hint: Use key in dict.
"""

dnary = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
tgt = input("Enter key to check if present ")

if tgt in dnary:
    print('Key exists')
else:
    print('Invalid key')
print(dnary)
