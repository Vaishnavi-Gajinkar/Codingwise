""" Print last char of a string """

str = input("Enter a string ")
print(f'Last char of string is ')

# way1
print(str[-1])

# way2
for i in range(len(str)):
    ch = str[i]
print(ch)

# way3
lst = [char for char in str ]
print(lst[-1])
