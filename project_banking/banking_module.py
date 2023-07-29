import pymysql as sm
con = sm.connect(host='127.0.0.1',user="root",password ="S17cs361@",database="db_trail")
# create curosr object
cur=con.cursor()
def create_table():
    #create table sql ddl in sql_ddl variable 
    sql_ddl='''CREATE TABLE banking_01 (account_number INT(100) NOT NULL AUTO_INCREMENT , 
    benificiery_name VARCHAR(200) NOT NULL , mobile INT(15) NOT NULL,adhar INT(16) NOT NULL , 
    age INT(3) NOT NULL , balance INT(200) NOT NULL ,status INT(2),
    PRIMARY KEY (account_number))'''
    # Execute sql statement 
    cur.execute(sql_ddl)
    #cur.execute(sql_ddl)
    con.commit()
    cur.close()
    con.close()
    
def opening_bank_account():
    print("\n Kindly provide the below deatils for opening bank account ")
    name=input("Enter Your Name : \t")
    mbl=eval(input("Enter Your Mobile Number  : \t"))
    eml=input("Enter Your Email Address : \t")
    adh=eval(input("Enter Your Adhar Number : \t"))
    age=eval(input("Enter Your Age  : \t"))
    bal=eval(input("Enter Your Opening Deposite Money  : \t"))
    data_insrt=(name,mbl,eml,adh,age,bal,1)
    # inserting data 
    var1="INSERT INTO person_details_01( benificiery_name , mobile ,Email, adhar,age ,balance ,status) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    # inserting data into Table with the help of varibale 
    cur.execute(var1,data_insrt)
    print(f"Hi {name}  your Account is Created ")
    con.commit()
    cur.close()
    con.close()

def money_deposit():
    print("\nYou Choose Option to deposite money")
    acc_no=int(input("Enter Your Account Number"))
    Deposit_money=int(input("Enter the amount that u wanted to deposite in your account "))
    query="UPDATE person_details_01 SET balance=balance+%s WHERE account_number=%s"
    data_insrt=(Deposit_money,acc_no)
    cur.execute(query,data_insrt)
    query1="SELECT * from person_details_01 WHERE account_number=%s"
    cur.execute(query1,acc_no)
    myresult = cur.fetchall()
    #print(myresult)
    print("Hi {0} you deposited {1} rupees and Your current balance is : {2}".format(myresult[0][1],Deposit_money,myresult[0][6]))
    con.commit()
    cur.close()
    con.close()


def money_withdraw():
    print("\nYou Choose Option ",chioce , "Which will for Withdrawale of Money ")
    acc_no=int(input("Enter Your Account Number"))
    Withdrawal_money=int(input("Enter the amount that u wanted to withdraw from your account "))
    query1="SELECT * from person_details_01 WHERE account_number=%s"
    cur.execute(query1,acc_no)
    myresult = cur.fetchall()
    if Withdrawal_money<=myresult[0][6]:
        query="UPDATE person_details_01 SET balance=balance-%s WHERE account_number=%s"
        data_insrt=(Withdrawal_money,acc_no)
        cur.execute(query,data_insrt)
        query_sel="SELECT * from person_details_01 WHERE account_number=%s"
        cur.execute(query_sel,acc_no)
        myresult_01 = cur.fetchall()
        print("Hi {0} you withdraw {1} rupees and Your current balance is : {2}".format(myresult_01[0][1],Withdrawal_money,myresult_01[0][6]))
    else:
        print("!! You don't have sufficient amount in your Account !!")
    con.commit()
    cur.close()
    con.close()

def balance_enquiry():
    print("\nYou Choose Option to check your current balance ")
    acc_no=int(input("Enter Your Account Number"))
    query="SELECT * from person_details_01 WHERE account_number=%s"
    cur.execute(query,acc_no)
    myresult = cur.fetchall()
    #print(myresult)
    if myresult==():
        print("Your Account number is wrong")
    else:
        print("Hi {0} Your Balance is : {1}".format(myresult[0][1],myresult[0][6]))
def update_mobile_number():
    print("\nYou Choose Option to  Update your mobile number in your account")
    acc_no=int(input("Enter Your Account Number  "))
    new_mob=int(input("Enter Your new mobile number "))
    query="UPDATE person_details_01 SET mobile=%s WHERE account_number=%s"
    data_insrt=(new_mob,acc_no)
    cur.execute(query,data_insrt)
    # mobile number Updated 
    # Display new mobile number
    query_sel="SELECT * from person_details_01 WHERE account_number=%s"
    cur.execute(query_sel,acc_no)
    myresult_01 = cur.fetchall()
    print("Hi {0} your mobile number is update .\nyour new mobile number is {1} ".format(myresult_01[0][1],myresult_01[0][2]))
    con.commit()
    cur.close()
    con.close()

def update_email_id():
    print("\nYou Choose Option to  Update your Email id in your account")
    acc_no=int(input("Enter Your Account Number  "))
    new_email=input("Enter Your new Email id ")
    query="UPDATE person_details_01 SET Email=%s WHERE account_number=%s"
    data_insrt=(new_email,acc_no)
    cur.execute(query,data_insrt)
    # mobile number Updated 
    # Display new mobile number
    query_sel="SELECT * from person_details_01 WHERE account_number=%s"
    cur.execute(query_sel,acc_no)
    myresult_01 = cur.fetchall()
    print("Hi {0} your Email id is updated .\nyour new Email id  is : {1} ".format(myresult_01[0][1],myresult_01[0][3]))
    con.commit()
    cur.close()
    con.close()

def close_account():
    print("\nYou Choose Option to  close your account")
    acc_no=int(input("Enter Your Account Number  "))
    query_sel="DELETE FROM person_details_01 WHERE account_number=%s"
    cur.execute(query_sel,acc_no)
    con.commit()
    cur.close()
    con.close()

