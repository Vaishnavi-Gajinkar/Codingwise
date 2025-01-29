""" Find Common Keys
- Problem: Find keys present in two dictionaries.
- Input: {"a": 1, "b": 2}, {"b": 3, "c": 4}
- Output: {"b"}
- Hint: Use set(dict1) & set(dict2).
"""

dict1 = {"a": 1, "b": 2, "d": 5}
dict2 = {"b": 3, "c": 4, "d": 7}

for key1 in dict1.keys():
    for key2 in dict2.keys():
        if key1 == key2:
            print(f'{key1}',end=" ")
print("is/are present in both dictionaries")
# ----------------------------------------------------
''' Alternate way 1 '''
set1 = set()
set2 = set()
for keys in dict1.keys():
    set1.update(keys)
for keyz in dict2.keys():
    set2.update(keyz)

for val in set1:
    if val in set2:
        print(val, end=" ")
# ----------------------------------------------------
''' Alternate way 2 '''
seyt1 = set(dict1)
seyt2 = set(dict2)
for val in seyt1:
    if val in seyt2:
        print(val, end=" ")