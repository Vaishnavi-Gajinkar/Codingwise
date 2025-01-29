"""Group by Value
- Problem: Group keys by their values.
- Input: {"a": 1, "b": 2, "c": 1}
- Output: {1: ["a", "c"], 2: ["b"]}
- Hint: Use defaultdict(list).
"""

dnary = {'a':1, 'b':2, 'c':1, 'd':4, 'e':2}
clubbed = {}

for key,val in dnary.items():
    if val in clubbed.values():
        clubbed[val].append(key)
    else:
        clubbed[val] = list(key)
print(clubbed)

# not solved