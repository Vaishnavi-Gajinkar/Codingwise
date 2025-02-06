'''
   *
  ***
 *****
*******
'''

n = int(input('Enter the max number of characters you want in this pattern'))

for i in range(n):
   for j in range(n-i-1):
      print(" ",end="")
   for k in range(i+1):
      print('*',end=" ")
   print()

# for a in range(n):
#    for b in range(n-1-a):
#       print(" ",end="")
#    for c in range(0,a+1):
#       print("* ",end="")
#    print()