import sqlite3

def get_name(database_file, person_id):
	query = "SELECT personal || ' ' || family FROM Person WHERE id='" + person_id + "';"
	connection = sqlite3.connect(database_file)
	cursor = connection.cursor()
	cursor.execute(query)
	results = cursor.fetchall()
	cursor.close()
	
	print("name of the person is %s"%(results[0][0]))
		
		
get_name('survey.db' , 'dyer')
