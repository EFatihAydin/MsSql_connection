import pymssql

conn = pymssql.connect(host=r"localhost", user='SA', password='Password', database='db_name')

print("Connected from DB")

cursor = conn.cursor()

cursor.execute("SELECT * FROM table_name;")

for i in cursor:
	print(i)