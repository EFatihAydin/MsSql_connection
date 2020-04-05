import pyodbc 

# Some other example server values are
server = 'localhost'

database = 'db_name'

username = 'SA'

password = 'Password'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = cnxn.cursor()

cursor.execute("SELECT * FROM table_name;")

for i in cursor:
	print(i)