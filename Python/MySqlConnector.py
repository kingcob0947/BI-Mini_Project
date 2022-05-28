import mysql.connector
mydb =mysql.connector.connect(host='localhost',user='root',password='Master@123')
print(mydb.connection_id)
cur = mydb.cursor()
cur.execute("create database python_DB")