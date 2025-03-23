'''
   *
  ***
 *****
*******
'''
# way 1
n = int(input('Enter the max number of characters you want in last line of this pattern'))

for a in range(n):
   if a%2==0:
      for b in range(n-1-a):
         print(" ",end="")
      for c in range(1,a+2):
         print("* ",end="")
      print()


# way 2
ask = input("How many number of lines do you want in this pattern? ")
n = int(ask)

for i in range(n):
   for j in range(n-i-1):
      print(" ",end="")
   for k in range(i+1):
      print('*',end="")
   for l in range(i):
      print('*',end="")
   print()