'''
*******
 *****
  ***
   *
'''

rows = int(input('Enter the max number of rows you want in this pattern '))
n = rows

firstrow = n + n - 1

for i in range(n):
   count_str = firstrow
   for j in range(i):
      print(" ",end="")
   while count_str > 0:
      print('*',end="")
      count_str -= 1
   firstrow -= 2
   print()