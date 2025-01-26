""" Write a FOR loop to check if a list contains only even numbers """

nums = input("Enter list numbers seperated by comma")

lizt = nums.split(',')

for num in lizt:
    if int(num) % 2 != 0:
        print("odd number found in list!")
        break
else:
    print(f'all your list items are even')
