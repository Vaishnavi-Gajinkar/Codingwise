""" Calculate the remainder when dividing two numbers """

flag = 0

while flag==0:
    try:
        numerator = int(input('Enter numerator value '))
        denominator = int(input('Enter denominator value '))

        remainder = numerator % denominator

        print('Remainder of this calculation is',remainder)
        flag = 1

    except Exception as e:
        flag = 0
        print("An error occured!")
    
    finally:
        if flag == 0:
            print("Enter correct values again")
        else:
            print("Ended the program successfully")