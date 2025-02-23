'''check if a character exists in a string'''

def charCheck(string, tgt):
    return list(filter(lambda x: tgt in x, string))

inp = input("Enter a main string - ")
tgt = input("Enter target to check if exists in main string - ")

result = charCheck(inp.lower(), tgt.lower())

if len(result) > 0:
    print("Character was found in main string :)")
else:
    print("Character was not found in main string :(")