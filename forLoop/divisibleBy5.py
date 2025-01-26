""" Write a for loop to count how many numbers in the list [10,15,20,25,30] are divisible by 5 """

lst = [10,15,20,25,30]                              # defining list explicitly
count = 0
for val in lst:
    if val % 5 == 0:
        count += 1
        print(f'{val} is divisible by 5')
print(f'A total of {count} elements in list are divisible by 5')

total_elements = int(input("How many elements are there in your list? "))       # accepting list elements from user
print("Enter the elements: ")
cnt = 0
lizt = []
for i in range(total_elements):
    lizt.append(int(input()))

for j in range(len(lizt)):
    if lizt[j] % 5 == 0:
        cnt += 1
print(f'There are {cnt} elements in list which are divisible by 5')

