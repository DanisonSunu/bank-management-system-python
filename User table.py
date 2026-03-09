import mysql.connector as sql

conn=sql.connect(host='localhost',user='root',database='bank',passwd='root')
cur=conn.cursor()

cur.execute('''
CREATE TABLE user_table(
username VARCHAR(25) PRIMARY KEY,
password VARCHAR(25) NOT NULL
)
''')