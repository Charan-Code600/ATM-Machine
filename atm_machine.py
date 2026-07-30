



import os

print("""
           ╔══════════════════════════════════╗
           ║     WELCOME TO HDFC ATM MACHINE  ║
           ╚══════════════════════════════════╝

**********************************************************
           
        Balance Check                   Enter  →  0
        Minimum Balance Check           Enter  →  1
        Withdraw                        Enter  →  2
        Deposit                         Enter  →  3
        Transaction History             Enter  →  4
        Exit                            Enter  →  5

***********************************************************

  🔒 Password Protected
  
""")

history = []
if os.path.exists("history.txt"):
    with open("history.txt", "r", encoding="utf-8") as f:
        history = f.readlines()

balance = 1000
if os.path.exists("balance.txt"):
    with open("balance.txt", "r", encoding="utf-8") as f:
        balance = int(f.read())

pin = ""
attempts = 0
while pin != "1234":
    if attempts >= 3:
        print("🔒 Account Locked! Too many wrong attempts.")
        exit()
    pin = input("Enter PIN: ")
    attempts += 1
    if pin != "1234":
        print(f"❌ Wrong PIN! {3 - attempts} attempt(s) left.\n")

print("\n✅ PIN Correct! Account Unlocked. Welcome!\n")
print("=" * 36)

while True:
    option = input("\nChoose an option (0-5): ")

    if option == "0":
        print("-" * 36)
        print(f"💰  Available Balance: ₹{balance}")
        print("-" * 36)


    elif option == "1":
        max_withdrawable = balance - 1000
        print("-" * 36)
        print(f"ℹ️  Minimum balance required: ₹1,000")
        if max_withdrawable > 0:
            print(f"✅ You can withdraw up to ₹{max_withdrawable} right now")
        else:
            print("❌ You cannot withdraw anything — balance is at minimum limit.")
        print("-" * 36)

    elif option == "2":
        try:
            enter = int(input("Withdraw amount: "))
        except ValueError:
            print("❌ Invalid input! Enter a number.")
            continue

        print("-" * 36)
        if enter <= 0:
            print("❌ Withdrawal amount must be positive.")
        elif enter <= balance - 1000:
            balance = balance - enter
            with open("balance.txt", "w", encoding="utf-8") as f:
                f.write(str(balance))
            history.append(f"Withdrawn: ₹{enter}")
            with open("history.txt", "a", encoding="utf-8") as f:
                f.write(f"Withdrawn: ₹{enter}\n")
            print(f"✅ Withdrawn ₹{enter} from HDFC Bank")
            print(f"💰 Available Balance: ₹{balance}")
        else:
            print(f"⚠  Insufficient balance! Current balance: ₹{balance}")
            print("   Minimum ₹1,000 must remain in account.")
        print("-" * 36)

    elif option == "3":
        try:
            deposit = int(input("Deposit amount: "))
        except ValueError:
            print("❌ Invalid input! Enter a number.")
            continue

        print("-" * 36)
        if deposit > 0:
            balance += deposit
            with open("balance.txt", "w", encoding="utf-8") as f:
                f.write(str(balance))
            history.append(f"Deposited: ₹{deposit}")
            with open("history.txt", "a", encoding="utf-8") as f:
                f.write(f"Deposited: ₹{deposit}\n")
            print(f"✅ Deposited ₹{deposit} into HDFC Bank")
            print(f"💰 New Balance: ₹{balance}")
        else:
            print("❌ Deposit amount must be positive.")
        print("-" * 36)

    elif option == "4":
        print("-" * 36)
        print("📜 Transaction History")
        print("-" * 36)
        if len(history) == 0:
            print("No transactions yet.")
        else:
            for i, h in enumerate(history, start=1):
                print(f"{i}. {h.strip()}")
        print("-" * 36)

    elif option == "5":
        print("\n🙏 Thank you for banking with HDFC. Visit again!")
        break

    else:
        print("❌ Invalid option! Please choose between 0-5.")








