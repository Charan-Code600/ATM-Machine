
balance = 10000
pin = ""

while pin != "1234":
    pin = input("enter pin:")

print("Access Granted")

while True:
    option = (input("Choose: "))
    
    if option == "1":
         print(f"💰 Available Balance: ₹{balance}")

    elif option == "2":
        enter =int(input("Withdraw amount:"))
        if enter <= balance :
            balance = balance-enter
            print(f"✅ Withdraw ₹{enter} From HDFC Bank ||    💰 Available Balance: ₹{balance}")
            
    elif option == "3":
        deposit =int(input("deposit amount:"))
        if deposit > 0:
            balance += deposit
            print(f"✅ Update! ₹{deposit} deposited in HDFC Bank||  💰 New Balance: ₹{balance}")
        
    elif option == "4":
        print("thank you for transaction ")
        break

    
