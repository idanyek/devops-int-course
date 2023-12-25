import sqlite3

# create a connection to the DB file
connection_manager = sqlite3.connect("gta.db")

# crate a cursor object
my_cursor = connection_manager.cursor()

# create a n new table
my_cursor.execute("CREATE TABLE IF NOT EXISTS gta (release_date INTEGER, release_name TEXT, release_city TEXT)")

query_string = """
INSERT INTO gta VALUES (?,?,?)
"""

# add single item

# query_param = (1997, "Grand Theft Auto", "state of New Guernsey")
# my_cursor.execute(query_string, query_param)

release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos"),
    (2025, "Grand Theft Auto V", "Los Santos")
]
# # add multiple with for:
# for game in release_list:
#     my_cursor.execute(query_string,game)
#
# # add multiple with executemany
# my_cursor.executemany(query_string,release_list)
#
# # add custom data:
# release_date = int(input("Release Date: "))
# release_name = input("Release name: ")
# release_city = input("Release city: ")
# my_tuple = (release_date,release_name,release_city)
# my_cursor.execute(query_string,my_tuple)

connection_manager.commit()

# get data from SQL

# for row in my_cursor.execute("SELECT * FROM gta"):
#     print(row)

sql_data = my_cursor.execute("SELECT * FROM gta")
# validate data

for data in release_list:
    if data not in sql_data:
        print(f"{data} NOT exists in DB")


connection_manager.close()

