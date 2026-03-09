import datetime as dt
import mysql.connector as sql

conn = sql.connect(host='localhost',user='root',database='bank',passwd='root')
cur = conn.cursor()

c='y'

while c=='y':

    print()
    print('1.Create Bank Account')
    print()
    print('2.Transaction')
    print()
    print('3.Customer Details')
    print()
    print('4.Transaction Details')
    print()
    print('5.Delete Account')
    print()
    print('6.Quit')
    print()

    n=int(input('Enter Your Choice: '))
    print()


    if n==1:

        acc_no=int(input('Enter Your Account Number: '))
        print()

        acc_name=input('Enter Your Account Name: ')
        print()

        ph_no=int(input('Enter Your Phone Number: '))
        print()

        add=input('Enter Your Place: ')
        print()

        cr_amt=int(input('Enter your Credit Amount: '))

        cur.execute("INSERT INTO customer_details VALUES(%s,%s,%s,%s,%s)",
                    (acc_no,acc_name,ph_no,add,cr_amt))

        conn.commit()

        print()
        print('Account Created Successfully')


    elif n==2:

        acct_no=int(input('Enter Your Account Number: '))

        cur.execute("SELECT * FROM customer_details WHERE acct_no=%s",(acct_no,))
        data=cur.fetchall()

        if len(data)==0:

            print()
            print('Account Number Invalid! Sorry Try Again Later!')
            print()

        else:

            print()
            print('1.Withdraw Amount')
            print()
            print('2.Add Amount')
            print()

            x=int(input('Enter Your Choice: '))
            print()

            if x==1:

                amt=int(input('Enter Withdrawal Amount: '))

                cur.execute("UPDATE customer_details SET cr_amt=cr_amt-%s WHERE acct_no=%s",(amt,acct_no))

                cur.execute("INSERT INTO transactions VALUES(%s,%s,%s,%s)",
                            (acct_no,dt.date.today(),amt,0))

                conn.commit()

                print()
                print('Account Updated Successfully!')


            elif x==2:

                amt=int(input('Enter Amount to be added: '))

                cur.execute("UPDATE customer_details SET cr_amt=cr_amt+%s WHERE acct_no=%s",(amt,acct_no))

                cur.execute("INSERT INTO transactions VALUES(%s,%s,%s,%s)",
                            (acct_no,dt.date.today(),0,amt))

                conn.commit()

                print()
                print('Account Updated Successfully!')


    elif n==3:

        acct_no=int(input('Enter Your Account Number: '))
        print()

        cur.execute("SELECT * FROM customer_details WHERE acct_no=%s",(acct_no,))
        data=cur.fetchone()

        if data is None:

            print()
            print('Invalid Account Number')

        else:

            print('Account Number: ',data[0])
            print()
            print('Account Name: ',data[1])
            print()
            print('Phone Number: ',data[2])
            print()
            print('Address: ',data[3])
            print()
            print('Credit Amount: ',data[4])


    elif n==4:

        acct_no=int(input('Enter Your Account Number: '))
        print()

        cur.execute("SELECT * FROM transactions WHERE acct_no=%s",(acct_no,))
        data=cur.fetchall()

        if len(data)==0:

            print('No Transactions Found')

        else:

            for row in data:

                print('Account Number: ',acct_no)
                print()
                print('Date: ',row[1])
                print()
                print('Withdrawal Amount: ',row[2])
                print()
                print('Amount Added: ',row[3])
                print()


    elif n==5:

        print('Delete Your Account')

        acct_no=int(input('Enter Your Account Number: '))

        cur.execute("DELETE FROM customer_details WHERE acct_no=%s",(acct_no,))
        conn.commit()

        print('Account Deleted Successfully')


    elif n==6:

        print('Do You Want To Exit?(Y/N)')

        c=input('Enter Your Choice: ')

        if c in ['Y','y']:

            print('Thank You Visit Again')
            break