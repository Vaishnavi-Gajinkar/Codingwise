'''check if sum of digits of a number is odd or even '''
sum = 0

def add(num):
    if num == 0:
        return 0
    else:
        return sum + add(num)
    
def gen_nums(numbers):

    for val in range(len(str(numbers))):
        yield val

inp = int(input("Enter a number "))
lst = []

for iter in range(len(str(inp))):
    lst.append(gen_nums(inp))

print(add(lst))
# not solved