import sqlite3

conn = sqlite3.connect("nexa.db")
cursor = conn.cursor()


query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)


#insert into table
'''query = """
INSERT INTO sys_command (id, name, path) 
VALUES (002, 'Whatsapp', '"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"')
"""
cursor.execute(query)
conn.commit()

print("Added Successfully" )'''

#create a table web command

'''query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
cursor.execute(query)
conn.commit()'''

# testing module
app_name = "Whatsapp"
cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
results = cursor.fetchall()
if results:  # Check if results is not empty
    print(results[0])  # Access the first element of the results
else:
    print("No results found for:", app_name) 
