""" Compare two strings and check if they are the same """

string1 = input("Enter first string ")
string2 = input("Enter second string ")

# way1
if string1.strip() == string2.strip():
    print("Strings are exactly same")
elif string1.lower() == string2.lower():
    print("Strings are same but differ in case")
else:
    print("Stings are different")

# way2

if len(string1) == len(string2):
    flag = 0
    for chars in range(len(string1)):
        if string1[chars] != string2[chars]:
            flag = 1
            break
    if flag == 0:
        print("Entered strings are same")
    else:
        print("Entered strings are different")
else:
    print("Entered strings are completly different")


