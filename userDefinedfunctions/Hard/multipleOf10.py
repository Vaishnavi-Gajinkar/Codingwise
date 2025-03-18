'''find the nearest multiple of 10 of a number'''

n = int(input("Enter a number "))

rem = n % 10

if rem < 5:
    res = n - rem
else:
    res = n + 10 - rem

print(res)
