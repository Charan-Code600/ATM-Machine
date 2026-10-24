




<!-- ==================== ANIMATED BANNER ==================== -->


<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=cylinder&color=0:0f2027,100:2c5364&height=160&section=header&text=ATM%20Machine&fontSize=55&fontColor=FFB800&animation=scaleIn&fontAlignY=42&desc=Python%20%7C%20CLI%20%7C%20File%20Persistence&descSize=18&descAlignY=68" width="100%"/>
</div>

<!-- ==================== Tagline ==================== -->

<div align="center">

### A fully functional command-line ATM system with PIN security, real-time balance tracking, and persistent transaction history — built entirely in Python.

</div>



<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>



<!-- ==================== Badges ==================== -->

<div align="center">

# $\textsf{\color{#FFB800}{Badges}}$

</div>

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/Dependencies-None-00C851?style=for-the-badge)
![Interface](https://img.shields.io/badge/Interface-CLI-2B2B2B?style=for-the-badge&logo=gnubash&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-FFB800?style=for-the-badge)

</div>



<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>



<!-- ==================== Table of Contents ==================== -->

<div align="center">

#  $\textsf{\color{#FFB800}{Table of Contents}}$

</div>

<div align="center">
<table>
<tr><td align="left">

[![1 Overview](https://img.shields.io/badge/1-Overview-FFB800?style=for-the-badge&labelColor=1a1a2e)](#overview)
<br>
[![2 Demo](https://img.shields.io/badge/2-Demo-FFB800?style=for-the-badge&labelColor=1a1a2e)](#demo)
<br>
[![3 Features](https://img.shields.io/badge/3-Features-FFB800?style=for-the-badge&labelColor=1a1a2e)](#features)
<br>
[![4 Tech Stack](https://img.shields.io/badge/4-Tech%20Stack-FFB800?style=for-the-badge&labelColor=1a1a2e)](#tech-stack)
<br>
[![5 Installation](https://img.shields.io/badge/5-Installation-FFB800?style=for-the-badge&labelColor=1a1a2e)](#installation)
<br>
[![6 Menu Options](https://img.shields.io/badge/6-Menu%20Options-FFB800?style=for-the-badge&labelColor=1a1a2e)](#menu-options)
<br>
[![7 Project Structure](https://img.shields.io/badge/7-Project%20Structure-FFB800?style=for-the-badge&labelColor=1a1a2e)](#project-structure)
<br>
[![8 Key Highlights](https://img.shields.io/badge/8-Key%20Highlights-FFB800?style=for-the-badge&labelColor=1a1a2e)](#key-highlights)
<br>
[![9 Future Improvements](https://img.shields.io/badge/9-Future%20Improvements-FFB800?style=for-the-badge&labelColor=1a1a2e)](#future-improvements)
<br>
[![10 Author](https://img.shields.io/badge/10-Author-FFB800?style=for-the-badge&labelColor=1a1a2e)](#author)

</td></tr>
</table>
</div>


<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>



<!-- ==================== Overview ==================== -->

<a id="overview"></a>

![1 Overview](https://img.shields.io/badge/1-Overview-FFB800?style=for-the-badge&labelColor=1a1a2e)

<div align="center">

### Real ATMs need to reliably verify identity, track balance, and remember transaction history between sessions. This project recreates that entire behavior using only core Python — no database, no external libraries — by combining secure input handling with simple file-based persistence. It was built to practice clean CLI design, state management, and real-world input validation.

</div>


<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>



<!-- ==================== Demo ==================== -->

<a id="demo"></a>

![2 Demo](https://img.shields.io/badge/2-Demo-FFB800?style=for-the-badge&labelColor=1a1a2e)

<div align="center">
<i>A real session: two wrong PINs, login, minimum-balance rules, deposit, withdrawal, history and exit.</i>
</div>

```
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

Enter PIN: 3345
❌ Wrong PIN! 2 attempt(s) left.

Enter PIN: 7854
❌ Wrong PIN! 1 attempt(s) left.

Enter PIN: 1234

✅ PIN Correct! Account Unlocked. Welcome!

====================================

Choose an option (0-5): 0
------------------------------------
💰  Available Balance: ₹1000
------------------------------------

Choose an option (0-5): 1
------------------------------------
ℹ️  Minimum balance required: ₹1,000
❌ You cannot withdraw anything — balance is at minimum limit.
------------------------------------

Choose an option (0-5): 2
Withdraw amount: 50
------------------------------------
⚠  Insufficient balance! Current balance: ₹1000
   Minimum ₹1,000 must remain in account.
------------------------------------

Choose an option (0-5): 3
Deposit amount: 1500
------------------------------------
✅ Deposited ₹1500 into HDFC Bank
💰 New Balance: ₹2500
------------------------------------

Choose an option (0-5): 1
------------------------------------
ℹ️  Minimum balance required: ₹1,000
✅ You can withdraw up to ₹1500 right now
------------------------------------

Choose an option (0-5): 2
Withdraw amount: 145
------------------------------------
✅ Withdrawn ₹145 from HDFC Bank
💰 Available Balance: ₹2355
------------------------------------

Choose an option (0-5): 4
------------------------------------
📜 Transaction History
------------------------------------
1. Deposited: ₹1500
2. Withdrawn: ₹145
------------------------------------

Choose an option (0-5): 5

🙏 Thank you for banking with HDFC. Visit again!
```


<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>



<!-- ==================== Features ==================== -->

<a id="features"></a>

![3 Features](https://img.shields.io/badge/3-Features-FFB800?style=for-the-badge&labelColor=1a1a2e)

<div align="center">

| Feature | What it does |
|:--|:--|
| 🔐 **PIN Login** | 3 attempts allowed, the session ends after 3 wrong PINs |
| 💰 **Balance Check** | Shows the current balance instantly |
| ℹ️ **Withdrawal Limit Check** | Shows how much can be withdrawn while keeping the ₹1,000 minimum |
| 💸 **Withdraw** | Blocks any withdrawal that would drop the balance below ₹1,000 |
| 💵 **Deposit** | Adds funds, only positive amounts are accepted |
| 📋 **Transaction History** | Every deposit and withdrawal is logged and shown in order |
| 💾 **Data Persistence** | Balance and history are saved to files and reload on the next run |
| ✅ **Input Validation** | Letters, zero, negative amounts and wrong menu options are rejected with a clear message |

</div>


<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>



<!-- ==================== Tech Stack ==================== -->

<a id="tech-stack"></a>

![4 Tech Stack](https://img.shields.io/badge/4-Tech%20Stack-FFB800?style=for-the-badge&labelColor=1a1a2e)

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Standard Library](https://img.shields.io/badge/Standard%20Library-os-4B8BBE?style=for-the-badge)
![Storage](https://img.shields.io/badge/Storage-Text%20Files-2B2B2B?style=for-the-badge)

**Concepts practiced:** file handling · lists · loops · conditionals · exception handling · string formatting

</div>


<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>



<!-- ==================== Installation ==================== -->

<a id="installation"></a>

![5 Installation](https://img.shields.io/badge/5-Installation-FFB800?style=for-the-badge&labelColor=1a1a2e)

<div align="center">

**Requirement:** Python 3.x. There is nothing else to install.

</div>

```bash
# 1. Clone the repository
git clone https://github.com/Charan-Code600/ATM-Machine.git

# 2. Open the project folder
cd ATM-Machine

# 3. Run the program
python atm.py
```

<div align="center">

If `python` is not recognised on your system, use `python3 atm.py` instead.

**Default PIN:** `1234` &nbsp;|&nbsp; **Attempts allowed:** 3

</div>


<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>



<!-- ==================== Menu Options ==================== -->

<a id="menu-options"></a>

![6 Menu Options](https://img.shields.io/badge/6-Menu%20Options-FFB800?style=for-the-badge&labelColor=1a1a2e)

<div align="center">

| Option | Action |
|:------:|:-------|
| 0 | Check current balance |
| 1 | Check how much you can safely withdraw |
| 2 | Withdraw money |
| 3 | Deposit money |
| 4 | View transaction history |
| 5 | Exit |

</div>


<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>



<!-- ==================== Project Structure ==================== -->

<a id="project-structure"></a>

![7 Project Structure](https://img.shields.io/badge/7-Project%20Structure-FFB800?style=for-the-badge&labelColor=1a1a2e)

```text
ATM-Machine/
├── atm.py          # Main program
├── balance.txt     # Auto-generated, stores the current balance
└── history.txt     # Auto-generated, stores the transaction log
```


<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>



<!-- ==================== Key Highlights ==================== -->

<a id="key-highlights"></a>

![8 Key Highlights](https://img.shields.io/badge/8-Key%20Highlights-FFB800?style=for-the-badge&labelColor=1a1a2e)

- **Zero external dependencies:** runs on any machine that has Python installed
- **Minimum-balance rule:** the ₹1,000 limit is checked on every withdrawal, so the balance can never drop below it
- **Automatic persistence:** balance and history are saved after every transaction, with no manual save step
- **Safe input handling:** invalid, negative or non-numeric entries get a clear message instead of an error


<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>



<!-- ==================== Future Improvements ==================== -->

<a id="future-improvements"></a>

![9 Future Improvements](https://img.shields.io/badge/9-Future%20Improvements-FFB800?style=for-the-badge&labelColor=1a1a2e)

- [ ] Multi-user support with a separate account file for each user
- [ ] Store the PIN securely (hashed) instead of keeping it in the code
- [ ] Option to change the PIN from the menu
- [ ] Export the transaction history as a mini statement
- [ ] GUI version using Tkinter


<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>



<!-- ==================== Author ==================== -->

<a id="author"></a>

![10 Author](https://img.shields.io/badge/10-Author-FFB800?style=for-the-badge&labelColor=1a1a2e)

<div align="center">

### Charan Aade
Python & Data Analysis Developer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/charanaade)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Charan-Code600)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:charanade66@gmail.com)

</div>

