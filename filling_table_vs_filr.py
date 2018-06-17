import sqlite3
from numpy.random import uniform
from datetime import datetime

def writing_data_in_filer_(random_numbers):
	start_time = datetime.now()

	file_to_write = open('temp_file.txt', 'w')
	for number in random_numbers:
		file_to_write.write(str(number) + "\n")

	file_to_write.close()

	print("Total execution time in writing data : " + str(datetime.now() - start_time))



def inserting_into_table(random_numbers):
	start_time = datetime.now()

	connection = sqlite3.connect("original.db")
	cursor = connection.cursor()
	cursor.execute("CREATE TABLE pressure(reading float not null)")
	query = "INSERT INTO pressure values(?);"

	for number in random_numbers:
		cursor.execute(query , [number])


	cursor.close()

	connection.commit()
	connection.close()

	print("Total execution time in inserting table: " + str(datetime.now() - start_time))




random_numbers = uniform(low=10.0, high=25.0, size=100000)
inserting_into_table(random_numbers)

writing_data_in_filer_(random_numbers)
