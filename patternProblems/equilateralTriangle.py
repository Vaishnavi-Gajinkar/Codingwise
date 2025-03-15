'''
   *
  ***
 *****
*******
'''

n = int(input('Enter the number of characters you want in the last line'))

for i in range(n):
   for j in range(n-i-1):
      print(" ",end="")
   for k in range(i+1):
      print('*',end=" ")
   print()

# pattern not as needed. only satisfactory