"""Add Key-Value Pair
- Problem: Add a new key-value pair to a dictionary.
- Input: {"a": 1}, key = "b", value = 2
- Output: {"a": 1, "b": 2}
- Hint: Use dict[key] = value.
"""

dnary = {'a':1, 'b':2, 'c':3, 'd':4}
print("Current elements of dictionary are ", dnary)
key = input("Enter new key ")
val = int(input("Enter value associated with this key "))
dnary[key] = val
print(dnary)