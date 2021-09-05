from personal_details import Personal_details 
import json

def staff_menu():
    print ("Enter your option: \n 1: Personal details \n 2: Set your shifts \n 3: Upcoming shifts \n"
    )
    option = int(input("enter your option. from 1-3 to get the name on month : "))

    if option == 1:
        for d in Personal_details.details.items():
            print (d)
        # print (details.email)
 
    elif option == 2:
        result =  "febuary"
        print("the month is ", result)
 
    elif option == 3:
        result = "march"
        print("the month is ", result)
 
    else:
        print("Incorrect option")
 
 
 
staff_menu()