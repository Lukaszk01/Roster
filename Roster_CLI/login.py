from staff.main_menu import Staff_menu 

def user():
    print ("Pick a user: staff/employee")
    user = input()

    if user == "staff":
        print ("You are logged in as a staff member")
        staff_menu()

    else:
        print ("You are logged in as manager")
user()