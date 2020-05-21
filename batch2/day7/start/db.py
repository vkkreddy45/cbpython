import sqlite3 as lite

# connect to the database
def connect(database_name):
    try:
        conn = lite.connect(database_name)
        return conn
    except lite.Error as e:
        print(e)

# To execute sql query
def execute(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except lite.Error as e:
        print(e)
        
# insert one record into table

# fetch all records from table

# fetch one record from table

# update one record in the table

# delete one record from table

# close the connection
