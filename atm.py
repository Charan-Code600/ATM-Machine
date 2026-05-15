balance = 10000
print("""
====================
WELL COME TO HDFC 
    ATM Machine
====================
Balance Check   enter---> 1
Withdraw        enter---> 2
Deposit         enter---> 3
Exit            enter---> 4

""")

while True:
    option = (input("Choose: "))
    
    if option == "1":
         print(f"💰 Available Balance: ₹{balance}")
        
    elif option == "2":
        enter =int(input("enter amount:"))
        if enter <= balance :
            balance = balance-enter
            print(f"✅ Withdraw ₹{enter} From HDFC Bank ||    💰 Available Balance: ₹{balance}")
            
    elif option == "3":
        deposit =int(input("enter deposit:"))
        if deposit > 0:
            balance += deposit
            print(f"✅ Update! ₹{deposit} deposited in HDFC Bank||  💰 New Balance: ₹{balance}")
        
    elif option == "4":
        print("thank you for transaction ")
        break
