""" Group Anagrams
- Problem: Group words into anagrams using dictionaries.
- Input: ["bat", "tab", "rat", "tar"]
- Output: [["bat", "tab"], ["rat", "tar"]]
- Hint: Use defaultdict(list) with sorted words as keys.
"""

lst = ["bat", "tab", "rat", "tar"]
anag = []
for i in range(len(lst)):
    for j in range(1,len(lst)):
        if len(lst[i]) == len(lst[j]):
            for ch in lst[i]:
                if ch in lst[j]:
                    anag.append(list(lst[i],lst[j]))
print(anag)
    
