balance = 100000
total_trans=0
transactions=[5000, -2000, 0, -70000, 15000]
for transaction in transactions:
    if transaction >0:
       
            balance=balance+transaction
            total_trans=total_trans+1
            print(f"An Amount of {transaction} is deposited in the account ")
            print("========================================")

    elif (transaction<0):
        if -transaction>balance:
            print("Insufficent balance. ")
        elif -transaction >50000:
             print(f"Account freezed. you entered {-transaction} amount ")
             break
        else:
            balance=balance+transaction
            total_trans=total_trans+1
            print(f"An Amount of {-transaction} is withdraw from the account ")
            print(f"your current balance of the account is {balance}") 
            print("=====================================")
    else:
        continue
print(f"THE FINAL BALANCE OF THE ACCOUNT IS: {balance}")
print(f"TOTAL TRANSACTIONS {total_trans}")
