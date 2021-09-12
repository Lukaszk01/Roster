from staff.personal_details import Personal_details 
import json

class Staff_menu():
    print ("Enter your option: \n 1: Personal details \n 2: Set your shifts \n 3: Upcoming shifts \n"
    )
    option = int(input("enter your option. from 1-3: "))

    if option == 1:
        for d in Personal_details.details.items():
            print (d)
        # print (details.email)
 
    elif option == 'q':
        print("Thank you for using the app ")
 
    elif option == 3:
        result = "march"
        print("the month is ", result)
 
    else:
        print("Incorrect option")
 
 
 
