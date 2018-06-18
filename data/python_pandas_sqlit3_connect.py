import pandas as pd
import sqlite3

#Read sqlite query result into pandas DataFrame
con = sqlite3.connect("portal_mammals.sqlite")
df = pd.read_sql_query("SELECT *FROM surveys",con)


#varify that result of sql is stored in the dataframe
print(df.head())

con.close()

