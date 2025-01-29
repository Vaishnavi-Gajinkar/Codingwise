""" Sum of Values
- Problem: Compute the sum of all values.
- Input: {"a": 1, "b": 2, "c": 3}
- Output: 6
- Hint: Use sum(dict.values()).
"""

dnary = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
sum = 0

for val in dnary.values():
    sum += val

print(sum)
