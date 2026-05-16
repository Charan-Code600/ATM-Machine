


print("""
====================
WELL COME TO HDFC 
    ATM Machine
====================

Balance Check      enter---> 0
Minimum balance    enter---> 1
Withdraw           enter---> 2
deposit            enter---> 3
Transaction        enter---> 4
history
Exit               enter---> 5

Password protected....
""")
history = []
balance = 1000
pin = ""

while pin != "1234":
    pin = input("enter pin:")

print("Access Granted")

while True:
    option = (input("Choose: "))
    
    if option == "0":
        print(f"💰 Available Balance: ₹{balance}")

    elif option =="1":
        enter = int(input(" Enter number between 1 to 9  :"))
        if balance - enter < 1000:
            print("""
              
            ⚠ Minimum balance rule:
    Your account must always maintain ₹1,000.
Please add more funds or withdraw a smaller amount.
                  
            add more balance to press 3
              
            """)

    elif option == "2":
        enter = int(input("Withdraw amount:"))
        if enter <= balance - 1000:  
            balance = balance - enter
            history.append(f"Withdrawn: ₹{enter}")
            print(f"✅ Withdraw ₹{enter} From HDFC Bank || 💰 Available Balance: ₹{balance}")
        else:  # ✅ यह add करो
            print(f"""
⚠ Your account balance is ₹{balance}
Add more balance to press 3
        """)
              
    elif option == "3":
        deposit =int(input("deposit amount:"))
        if deposit > 0:
            balance += deposit
            history.append(f"Deposited: ₹{deposit}")
            print(f"✅ Update! ₹{deposit} deposited in HDFC Bank||  💰 New Balance: ₹{balance}")

    elif option == "4":
        print("\n--- Transaction History ---")
        if len(history) == 0:
            print("कोई transaction नहीं हुआ!")
        else:                          
            for h in history:
                print(h)

    elif option == "5":
        print("Thank you for Transaction")  
        break












