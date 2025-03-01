'''find the ASCII value / character associated with the input '''

class Ascii:
    def checkAscii(self,char):
        self.char = char
        return ord(self.char)
    
    def checkVal(self,val):
        self.val = val
        return chr(val)
    

a = Ascii()
flag = [0]

while 0 in flag:
    try:
        inp = int(input("""\nEnter the number corresponding to ur action:
                    1. Check the ASCII value of my character
                    2. Check the character present at my ASCII value 
                    3. Exit \t"""))

        if inp == 1:
            char = input("Enter your character \t")
            asci = a.checkAscii(char)
            print(f'ASCII value of your character {char} is {asci}')
            flag = [0 if input("Would you like to perform another operation?(y/n) ") == 'y' else 1]
        elif inp == 2:
            value = int(input("Enter the value to get the ASCII char at that loc\nNote: ASCII values are btwn - to - only \t"))
            char = a.checkVal(value)
            print(f"The ASCII character associated with ur value {value} is {char}")
            flag = [0 if input("Would you like to perform another operation?(y/n) ") == 'y' else 1]
        else:
            flag = [1]

    except Exception as e:
        print(e)
        print("Invalid input. Pls try again")
        flag = [0]