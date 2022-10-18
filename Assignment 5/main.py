# Name: Trang Ngo
# Date: 10/12/2022
# File Purpose: Output, Call all of the function in contacts module

from contacts import *
contact_list = Contacts(filename = 'c.dat')
while True:
    print ("           *** TUFFY TITAN CONTACT MAIN MENU \n")
    print ("1. Add contact")
    print ("2. Modify contact")
    print ("3. Delete contact")
    print ("4. Print contact list")
    print ("5. Set contact filename")
    print ("6. Exit the program")
    print ()
    menu_choice = int(input("Enter menu choice: "))
    print ()

    # add contact
    if (menu_choice == 1):
        phone = input("Enter phone number: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        r = contact_list.add_contact(id = phone, first_name = first_name, last_name = last_name)
        if r == "error":
            print("Phone number already exists.")
        else:
            print ("Added: " + r[0] + " " + r[1] + ".")
        print()

    # modify contact
    elif (menu_choice == 2):
        phone = input("Enter phone number: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name")
        r = contact_list.modify_contact(id = phone, first_name = first_name, last_name = last_name)
        if r == "error":
            print ('Phone number does not exist.')
        else:
            print ("Modified: " + r[0] + " " + r[1] + ".")
        print()

    # delete contact
    elif (menu_choice == 3):
        phone = input ("Enter phone number: ")
        r = contact_list.delete_contact(id = phone)
        if r == "error":
            print ("Invalid Phone number")
        else:
            print ("Deleted: " + r[0] + " " + r[1] + ".")
        print ()

    # print the contact list  
    elif (menu_choice == 4):
        print ("==================== CONTACT LIST ====================")
        print ("Last Name             First Name            Phone")
        print ("====================  ====================  ==========")
        for key in contact_list.data:
            print(f'{contact_list.data[key][1]:22}{contact_list.data[key][0]:22}{key:12}')
        print ()
    
    # set file name
    elif (menu_choice == 5):
        filename = input("Enter new filename:")
        contact_list = Contacts(filename = filename)   
        print()
    
    elif (menu_choice == 6):
        break
    else:
        print ("Invalid choice")