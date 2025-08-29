'''check if 2 strings have the same length '''

def size_chker(*args):

    lst = []
    for item in args[0]:
        if len(item) not in lst:
            lst.append(len(item))

    return lst


inp = input("Enter multiple strings (comma seperated) ").split(",")

res = size_chker(inp)

if len(res) == 1:
    print("All strings are of same length")
else:
    print("Strings are of different sizes")


# not solved