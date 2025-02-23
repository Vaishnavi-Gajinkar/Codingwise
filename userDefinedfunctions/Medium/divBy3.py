'''display numbers which are not divisible by 3'''

def indivBy3(lst):

    new_lst = filter(lambda x : x%3 != 0, lst)
    return new_lst

inp = input("Enter values in list (seperated by comma) ")

lst = inp.split(',')

for position in range(len(lst)):
    lst[position] = int(lst[position])

result = list(indivBy3(lst))

print('The following elements of your list are not divisible by 3\n',result)