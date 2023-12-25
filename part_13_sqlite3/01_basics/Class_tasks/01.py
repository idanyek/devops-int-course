import sqlite3

# create a connection to the DB file
connection_manager = sqlite3.connect("users.db")

# crate a cursor object
my_cursor = connection_manager.cursor()

# create a n new table
my_cursor.execute("CREATE TABLE IF NOT EXISTS users "
                  "(title TEXT, first_name TEXT, last_name TEXT, age INTEGER, address TEXT)")


insert_query = """
INSERT INTO users VALUES (?,?,?,?,?)
"""

title = input("enter title: ")
first_name = input("enter first name: ")
last_name = input("enter last name: ")
age = int(input("enter age: "))
address = input("enter address: ")

received_data = (title,first_name,last_name,age,address)
my_cursor.execute(insert_query,received_data)

connection_manager.commit()

if received_data in my_cursor.execute("SELECT * FROM USERS"):
    print(f"{received_data} inserted successfully to the DB")
else:
    raise Exception("failed to insert data to DB")

connection_manager.close()
