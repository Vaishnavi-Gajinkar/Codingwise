'''
*   * 
 * *  
  * 
 * * 
*   * 
'''
rows = 5
n = rows
for i in range(rows):
    for j in range(rows):
        if i == j or (i-1)==j or i==(j-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()

# not solved        
