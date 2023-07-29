import banking_module as bank
# one time activity to create table 
#bank.create_table()
chioce=int(input('''  \t\t\tPress 1 For Opening Bank Account
                       Press 2 for Deposit of Money 
                       Press 3 For Withdrawal 
                       Press 4 For Balance enquiry 
                       Press 5 For Update mobile number 
                       Press 6 For Update Email id
                       Press 7 For Closing Your Account 
                       Enter Your Chioce. \t'''))

if chioce==1:
    bank.opening_bank_account()
elif chioce==2:
    bank.money_deposit()
elif chioce==3:
    bank.money_withdraw()
elif chioce==4:
    bank.balance_enquiry()
elif chioce==5:
    bank.update_mobile_number()
elif chioce==6:
    bank.update_email_id()
elif chioce==7:
    bank.close_account()
else :
    print("!!! ohh Please choose correct options !!!")
