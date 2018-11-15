import pyodbc

server = 'tcp:35.231.197.213:3066'
database = 'bluebike'
username = 'bbd-create'
password = 'bbd-create-123'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute('SELECT * FROM station')

rows = cursor.fetchall()
for row in rows:
    print row.user_id, row.user_name