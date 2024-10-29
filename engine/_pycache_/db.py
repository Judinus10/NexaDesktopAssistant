import sqlite3
import csv

# Establish a connection to the database
conn = sqlite3.connect("nexa.db")
cursor = conn.cursor()

# Create sys_command table if it doesn't exist
'''query_sys_command = """
CREATE TABLE IF NOT EXISTS sys_command(
    id INTEGER PRIMARY KEY, 
    name VARCHAR(100), 
    path VARCHAR(1000)
)
"""
cursor.execute(query_sys_command)'''

# Optionally insert a record into sys_command (uncomment to use)
# cursor.execute("""
# INSERT INTO sys_command (id, name, path) 
# VALUES (002, 'Whatsapp', 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs')
# """)
# conn.commit()
# print("Added Successfully")

# Create web_command table if it doesn't exist
'''query_web_command = """
CREATE TABLE IF NOT EXISTS web_command(
    id INTEGER PRIMARY KEY, 
    name VARCHAR(100), 
    url VARCHAR(1000)
)
"""
cursor.execute(query_web_command)'''

# Optionally insert a record into web_command (uncomment to use)
# cursor.execute("""
# INSERT INTO web_command (id, name, url) 
# VALUES (null, 'youtube', 'https://www.youtube.com/')
# """)
# conn.commit()
# print("Web command added successfully")

# Create contacts table if it doesn't exist
query_contacts = """
CREATE TABLE IF NOT EXISTS contacts(
    id INTEGER PRIMARY KEY, 
    name VARCHAR(100), 
    mobile_no VARCHAR(15)
)
"""
cursor.execute(query_contacts)

# Insert data from contacts.csv into contacts table
# Specify the column indices you want to import (0-based index)
desired_columns_indices = [0, 1]  # Adjust these indices to match your CSV structure

with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        # Select columns only if they exist in the row
        selected_data = [row[i] for i in desired_columns_indices if i < len(row)]
        
        # Ensure we have the expected number of columns
        if len(selected_data) == len(desired_columns_indices):
            cursor.execute(
                '''INSERT INTO contacts (id, name, mobile_no) VALUES (null, ?, ?);''',
                tuple(selected_data)
            )
        else:
            print(f"Row skipped due to missing columns: {row}")

# Commit changes and close the connection
conn.commit()
conn.close()
print("Data imported successfully.")
