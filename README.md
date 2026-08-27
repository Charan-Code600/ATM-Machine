



# 🏦 ATM Machine

A simple ATM simulator built with Python, with PIN protection and persistent data storage.

## Features

- 🔐 PIN Protection (3 attempts before lockout)
- 🔒 Account Lock after 3 wrong PIN entries
- 💰 Balance Check
- 💸 Withdraw Money (with minimum balance enforcement)
- 💵 Deposit Money
- 📋 Transaction History (saved permanently to file)
- ⚠️ Minimum Balance Rule (₹1,000 must always remain in account)
- ✅ Input Validation (invalid or negative amounts are safely rejected)
- 💾 Data Persistence — balance and history are saved to files, so your data stays even after closing the program

## Requirements

- Python 3.x (no external libraries needed)

## How to Run

```bash
python atm.py
```

## Default PIN

To access the ATM, use this PIN when prompted:

```
1234
```

## How It Works

1. Run the script and enter the PIN when prompted (3 attempts allowed).
2. Once unlocked, choose an option from the menu (0-5).
3. Balance and transaction history are automatically saved to `balance.txt` and `history.txt` in the same folder, so your data is remembered the next time you run the program.

## Menu Options

| Option | Action |
|--------|--------|
| 0 | Check current balance |
| 1 | Check how much you can safely withdraw |
| 2 | Withdraw money |
| 3 | Deposit money |
| 4 | View transaction history |
| 5 | Exit |

## Technologies Used

- Python
- File Handling
- Lists
- Loops
- Conditionals

## Author

**Charan Aade | Python Developer**

🔗 [GitHub](https://github.com/Charan-Code600)

