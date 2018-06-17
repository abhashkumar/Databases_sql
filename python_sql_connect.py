import sqlite3

def get_name(database_file, person_id):
    query = "SELECT personal || ' ' || family FROM Person WHERE id=?;"

    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute(query, [person_id])
    results = cursor.fetchall()
    cursor.close()
    connection.close()

    return results[0][0]

print("Full name for dyer:", get_name('survey.db', 'dyer'))
