cost = float(input("Enter your shopping amt"))

if (cost > 10000):
    method = input("Enter your payment method (i.e. Card/Cash)")
    if (method == "Card" or method == "card"):
        print("You are eligible for a 10% discount")
    else:
        print("sorry you are not eligible for the discount")
else:
    print("sorry you are not eligible for the discount")