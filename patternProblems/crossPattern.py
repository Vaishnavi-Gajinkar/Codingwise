'''
*   * 
 * *  
  * 
 * * 
*   * 
'''
rows = int(input("Enter an odd number "))
n = rows
for i in range(rows):
    for j in range(rows):
        if i == j or (n-i-1)==j or i==(n-j-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
if rows %2 == 0:
    print("Told you to provide odd number na 😒")

'''
OUTPUT :
Enter an odd number 9
*       *
 *     *
  *   *
   * *
    *
   * *
  *   *
 *     *
*       *
'''