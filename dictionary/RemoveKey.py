""" RemoveKey
- Problem: Remove a specific key.
- Input: {"a": 1, "b": 2}, key = "b"
- Output: {"a": 1}
- Hint: Use del dict[key].
"""

dnary = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
print("Current elements of dictionary are", dnary)

key = input("Enter key to be removed: ")
del dnary[key]

print("Element removed successfully", dnary)