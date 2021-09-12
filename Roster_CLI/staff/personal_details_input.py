import mysql.connector

mydb = mysql.connector.connect(
    email = "email",
    birth_date = "birth_date",
    full_name = "full_name",
    phone_number = "phone_number",
    gender = "gender",
    position = "position",
    employment = "employement",
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)



