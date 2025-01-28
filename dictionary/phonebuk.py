""" PHONEBOOK APPLICATION
This application is a replica of the original phonbook diaries, except for the technological aspect of it.
Users can View the existing entries of phonebook.
Users can Add a new contact.
Users can Search for a contact.
users can Delete a contact.
"""

details = ['Name','Contact','Address']
default_val = 0
phonebook = dict.fromkeys(details,default_val)

while True:
    inp = int(input(""" What operation to perform ?
        1. View Contacts
        2. Add Contact
        3. Search Details
        4. Delete Contact
        5. Exit """))
    if inp == 1:
        for key, val in phonebook.items():
            print(key , val)
    elif inp == 2:
        print("Enter details of user")
        name = input('Enter Name')
        number = int(input('Enter Contact Number'))
        addr = input("Enter Address")
        phonebook.update({'Name':name, 'Contact':number, 'Address':addr})
        print('Contact updated successfully !')
    elif inp == 3:
        name = input("Enter name of user: ")
        print(f'Contact : {phonebook['Contact']}\nAddress : {phonebook['Address']}')
    elif inp == 4:
        name = input("Enter name of contact to be deleted ")
        if name in phonebook.values():
            del phonebook[name]
        else:
            print("Invalid contact to delete.")
    else:
        break