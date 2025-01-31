""" Count Characters
- Problem: Count occurrences of characters in a string using a dictionary.
- Input: "hello"
- Output: {"h": 1, "e": 1, "l": 2, "o": 1}
- Hint: Use a loop and dict.setdefault().
"""

str = input("Enter a string ")
dnary = {}

for ch in str:
    if ch in dnary:
        dnary[ch] += 1
    else:
        dnary.setdefault(ch,1)
        # dnary[ch] = 1
print(dnary)
