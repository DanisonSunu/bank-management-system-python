import mysql.connector as sql

conn=sql.connect(host='localhost',user='root',database='bank',passwd='root')
cur=conn.cursor()

cur.execute('''
CREATE TABLE transactions(
acct_no INT,
date DATE,
withdrawal_amt BIGINT,
amount_added BIGINT
)
''')