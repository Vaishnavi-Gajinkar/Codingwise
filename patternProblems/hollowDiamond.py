'''
   *
  * *
 *   *
*     *
 *   *
  * *
   *
   
'''
n = 4
for i in range(n):
   for j in range(n-i-1):
      print(" ",end="")
   # for k in range(1):
   #    print("*",end="")
   print("*",end="")
   for l in range(i,i+1,2):
      print(" ",end="")
   print("*")
