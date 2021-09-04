def user():
    print ("Pick a user: staff/employee")
    user = input()

    if user == "staff":
        print ("You are logged in as a staff member")
    else:
        print ("You are logged in as manager")
user()