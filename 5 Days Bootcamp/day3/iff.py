""" set a password
check if password is equal to 123py
"""

set_pwd = "123py"
userInp = input("Enter password")
if userInp == set_pwd:
    print("Login success")
else:
    print("Login failure")