# https://docs.python.org/3/library/sqlite3.html
# if necessary, delete the database manually (see db file with app.py)
import sqlite3 # comes with python default library

# Connect to the database (creates a new database if it doesn't exist)
conn = sqlite3.connect('my_sql_database.db') # NOTE 1: Tihs is the name of the database - you will refer to it in app.py

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the table for customers
cursor.execute('''
    CREATE TABLE IF NOT EXISTS table1 (
        id INTEGER PRIMARY KEY,
        field1 TEXT,
        field2 TEXT
    )
''')

# Commit the changes 
conn.commit()

# Populate the customers table
table1_data = [
    (1, '1a', '1b'),
    (2, '2a', '2b'),
    (3, '3a', '3b'),
    # Add more customer records here
]

cursor.executemany('INSERT INTO table1 VALUES (?, ?, ?)', table1_data)

# Commit the changes and close the connection
conn.commit()
conn.close()