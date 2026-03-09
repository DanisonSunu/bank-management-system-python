import mysql.connector as sql

con=sql.connect(host='localhost',user='root',passwd='root',database='bank')

if con.is_connected():
    print('Connected successfully')

cur=con.cursor()

cur.execute('''
CREATE TABLE customer_details(
acct_no INT PRIMARY KEY,
acct_name VARCHAR(25),
phone_no BIGINT,
address VARCHAR(25),
cr_amt FLOAT
)
''')