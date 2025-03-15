'''
   *
  ***
 *****
*******
 *****
  ***
   *
'''
flag = 0
while flag == 0:
   try:
      total_lines = int(input("Enter the number of lines you want in this pattern "))
      half = total_lines // 2

      for i in range(half+1):
         for j in range(half-i):
            print(" ",end="")
         for k in range(i+1):
            print("* ",end="")
         print()
      for i in range(half+1,total_lines):
         for j in range(i-half):
            print(" ",end="")
         for k in range(total_lines-i):
            print("* ",end="")
         print()
      assert total_lines % 2 != 0
      flag = 1
   except AssertionError:
      print("Please retry with odd number of lines, as seen in sample pattern.")
      flag = 0
   finally:
      if flag == 1:
         print("Beautiful Pattern 😍")
      else:
         print("This pattern looks ugly 😒")