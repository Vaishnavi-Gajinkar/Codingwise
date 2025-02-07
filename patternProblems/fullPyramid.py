'''
   *
  ***
 *****
*******
'''

n = int(input('Enter the max number of characters you want in this pattern'))

for a in range(n):
   if a%2==0:
      for b in range(n-1-a):
         print(" ",end="")
      for c in range(1,a+2):
         print("* ",end="")
      print()