import sqlite3

connection_original = sqlite3.connect("original.db")
cursor_original = connection_original.cursor()
cursor_original.execute("SELECT * FROM Pressure WHERE reading > 20.0;")
results = cursor_original.fetchall()
cursor_original.close()
connection_original.close()

connection_backup = sqlite3.connect("backup.db")
cursor_backup = connection_backup.cursor()
cursor_backup.execute("CREATE TABLE Pressure (reading float not null)")
query = "INSERT INTO Pressure values (?);"

for entry in results:
    cursor_backup.execute(query, entry)

cursor_backup.close()
connection_backup.commit()
connection_backup.close()
