""" Value Count
- Problem: Count occurrences of a value in a dictionary.
- Input: {"a": 1, "b": 2, "c": 1}, value = 1
- Output: 2
- Hint: Use list(dict.values()).count(value).
"""

dnary = {'a':1, 'b':2, 'c':1, 'd':4, 'e':1}
tgt = int(input(f'{dnary}\nEnter the value to be counted '))
count = 0

for val in dnary.values():
    if val == tgt:
        count += 1
print(f'The value {tgt} has appeared {count} times in dictionary')

print(list(dnary.values()).count(tgt))