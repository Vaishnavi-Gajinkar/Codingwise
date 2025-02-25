'''find the largest digit in a number'''

value = input("Enter a numeric value ")

print(tuple(value))

sort = sorted(tuple(value))

print(sort)
print(f'Largest digit in your number is {int(sort[-1])}')