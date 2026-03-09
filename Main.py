import mysql.connector as sql
import datetime as dt

conn = sql.connect(host='localhost',user='root',database='bank',passwd='root')
cur = conn.cursor()

print('====================WELCOME STARK BANK====================')
print(dt.datetime.now())

print('1.Register')
print()
print('2.Login')
print()

n = int(input('Enter Your Choice: '))
print()

if n == 1:
    name = input('Enter a Username: ')
    print()

    passwd = input('Enter a 4 Digit Password: ')   # changed (removed int)
    print()

    cur.execute("INSERT INTO user_table(username,password) VALUES(%s,%s)",(name,passwd))
    conn.commit()

    print()
    print('User Created Successfully')


elif n == 2:

    name = input('Enter Your Username: ')
    print()

    passwd = input('Enter your 4 Digit Password: ')   # changed
    print()

    cur.execute("SELECT * FROM user_table WHERE username=%s AND password=%s",(name,passwd))

    if cur.fetchone() is None:
        print()
        print('Invalid Username or Password')

    else:
        print('Login Successful')
        import menu