'''
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA 
'''
print(chr(65))          # A

ask = input("How many number of lines do you want in this pattern? ")
n = int(ask)

for i in range(n):
   char = ord("A")
   for j in range(n-i-1):
      print(" ",end="")
   for k in range(i+1):
      print(chr(char),end="")
      char += 1
   char -= 1
   for l in range(i):
      char -= 1
      print(chr(char),end="")
   print()