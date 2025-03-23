''' write a function that takes a number and ensures its positive '''

while True:
    try:
        val = int(input("Enter a positive number: "))

        assert val > 0, "Enter a positive number plej"

        print("Good Job!")
        ask = input("Again ? (y/n)")

        if ask.lower() == 'n' or ask.lower() == 'no':
            print('It was funn playing 😊 Gubbaai')
            break
    
    except AssertionError as e:
        print('Assertion error caught,',e)

    except ValueError as ve:
        print("Value error caught,",ve)


# OUTPUT:
'''
Enter a positive number: -9
Assertion error caught, Enter a positive number plej
Enter a positive number: bvm
Value error caught, invalid literal for int() with base 10: 'bvm'
Enter a positive number: 9
Good Job!
Again ? (y/n)n
It was funn playing 😊 Gubbaai
'''