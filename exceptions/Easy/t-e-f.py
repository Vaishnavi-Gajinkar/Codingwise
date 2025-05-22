''' implement a try-except-finally block where Finally prints "Execution complete" '''

try:
    age = int(input("What's your age? "))
    accept = input("Enter your dream occupation ")
    byWhen = int(input("By what age do you want to achieve it? "))
    ask = input("Are you working towards achieving it? (y/n)")

    if ask.lower() == "yes" or ask.lower == "y":
        assert byWhen >= age, "Sorry you've grown older now. Better luck next life"
        
        print("Great! Still have time now.")
    elif ask.lower() == "no" or ask.lower == "n":
        print("Why not? ")
        print("Why are you doing different? ")
        print("What is the immediate next step you can take? ")
        print("Who can help you get there? ")
        print("What's stopping you? ")
        raise Exception
except AssertionError as e:
    print(e,", ")
except Exception as e:
    print("You are full of excuses!")
finally:
    print("Great! You chose your hard")