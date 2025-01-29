"""Find Max Value
- Problem: Find the key with the max value.
- Input: {"a": 1, "b": 3, "c": 2}
- Output: "b"
- Hint: Use max(dict, key=dict.get).
"""

dnary = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
maxVal = 0
maxKey = None
for key, val in dnary.items():
    if val > maxVal:
        maxVal = val
        maxKey = key
print(f'Key with the max value is {maxKey}')

# Alternative
print(max(dnary, key=dnary.get))