""" Remove Empty Values
- Problem: Remove keys with empty values.
- Input: {"a": 1, "b": None, "c": ""}
- Output: {"a": 1}
- Hint: Use dictionary comprehension.
"""

dnary = {"a": 1, "b": None, "c": ""}
new_dict = {}
for key, vals in dnary.items():
    if vals == "" or vals == None:
        continue
    else:
        new_dict[key] = vals
print(dnary)
print(new_dict)

#--Alternate way---------------------------
dict_comp = {key:val for key,val in dnary.items() if val!="" and val!=None}
print(dict_comp)
