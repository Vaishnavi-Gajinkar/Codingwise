'''
   *
  ***
 *****
*******
 *****
  ***
   *
'''

total_lines = int(input("Enter the max number of lines you want in this pattern "))
center = 0
if total_lines%2 == 0:
    center = int(total_lines / 2)
else:
    center = int(total_lines / 2 + 1)

for i in range(center):
   if i % 2 == 0:
      for j in range(center-i-1):
         print(" ",end="")
      for k in range(1,i+2):
         print("* ",end="")
      print()