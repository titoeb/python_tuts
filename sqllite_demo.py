import sqlite3

# Create the database on file.
with sqlite3.connect('employee.db') as connection:

    # Create a cursor to execute queries.
    cursor = connection.cursor()
    
    #cursor.execute("""
    #    CREATE TABLE employees(first_name text, last_name text, pay integer)
    #""")

    #cursor.execute("""
    #    INSERT INTO employees VALUES('Corey, )
    #""")

    connection.commit()