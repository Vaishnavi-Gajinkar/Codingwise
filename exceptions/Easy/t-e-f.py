''' implement a try-except-finally block where Finally prints "Execution complete" '''

try:
    age = int(input("What's your age? "))
    accept = input("Enter your dream occupation ")
    byWhen = int(input("By what age do you want to achieve it? "))
    ask = input("Are you working towards achieving it? (y/n)")

    if ask.lower() == "yes" or ask.lower() == "y":
        assert byWhen >= age, "Sorry you've grown older now. Better luck next life"
        
        print("Great! Still have time now.")
    elif ask.lower() == "no" or ask.lower() == "n":
        print("Why not? ")
        print("Why are you doing different? ")
        print("What is the immediate next step you can take? ")
        print("Who can help you get there? ")
        print("What's stopping you? ")
        raise Exception("\nYou are full of excuses!!!")
except AssertionError as e:
    print(e,", ")
except ValueError as e:
    print("\nInvalid Input. Pls try again later.")
finally:
    print("\nYou chose your hard")

'''
OUTPUT :
What's your age? 18
Enter your dream occupation DA/DS
By what age do you want to achieve it? 30
Are you working towards achieving it? (y/n)Y
Great! Still have time now.

You chose your hard
--------------------------------------------------------------------------------------------------------
What's your age? 18
Enter your dream occupation DA/DS
By what age do you want to achieve it? 30
Are you working towards achieving it? (y/n)N
Why not? 
Why are you doing different?
What is the immediate next step you can take?
Who can help you get there?
What's stopping you?

You chose your hard
Traceback (most recent call last):
  File "c:\Users\Lenovo\OneDrive\Documents\PythonPractise\CodingWise\exceptions\Easy\t-e-f.py", line 19, in <module>
    raise Exception("\nYou are full of excuses!!!")
Exception:
You are full of excuses!!!
---------------------------------------------------------------------------------------------------------
What's your age? 30
Enter your dream occupation SDE
By what age do you want to achieve it? 25
Are you working towards achieving it? (y/n)Y
Sorry you've grown older now. Better luck next life , 

You chose your hard
---------------------------------------------------------------------------------------------------------
What's your age? 30
Enter your dream occupation SDE 
By what age do you want to achieve it? 25
Are you working towards achieving it? (y/n)N
Why not? 
Why are you doing different?
What is the immediate next step you can take?
Who can help you get there?
What's stopping you?

You chose your hard
Traceback (most recent call last):
  File "c:\Users\Lenovo\OneDrive\Documents\PythonPractise\CodingWise\exceptions\Easy\t-e-f.py", line 19, in <module>
    raise Exception("\nYou are full of excuses!!!")
Exception:
You are full of excuses!!!
------------------------------------------------------------------------------------------------------
What's your age? QWERTY

Invalid Input. Pls try again later.

You chose your hard
'''