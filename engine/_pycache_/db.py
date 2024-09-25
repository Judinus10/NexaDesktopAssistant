import sqlite3

conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()


query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)


#insert into table
'''query = """
INSERT INTO sys_command (id, name, path) 
VALUES (004, 'vscode', '"C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"')
"""
cursor.execute(query)
conn.commit()'''



#create a table web command

'''query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
cursor.execute(query)
conn.commit()'''

# testing module
app_name = "Github Desktop"
cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
results = cursor.fetchall()
print(results[0])
