<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:FFB800,100:FF8C00&height=150&section=header&text=ATM%20Machine&fontSize=50&fontColor=000000&animation=fadeIn&fontAlignY=35" width="100%"/>
</div>

<div align="center">

### A fully functional command-line ATM system with PIN security, real-time balance tracking, and persistent transaction history — built entirely in Python.

</div>


<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>



<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:FFB800,100:FF8C00&height=80&section=header&text=Badges&fontSize=50&fontColor=000000&fontAlignY=50" width="300"/>
</div>

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-00C851?style=for-the-badge&logo=checkmarx&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-FFB800?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-PIN%20Protected-FF4444?style=for-the-badge&logo=shieldcheck&logoColor=white)

</div>

<br>

## 📑 Table of Contents

- [Overview](#-overview)
- [Demo](#-demo)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation & Usage](#-installation--usage)
- [Menu Options](#-menu-options)
- [Project Structure](#-project-structure)
- [Key Highlights](#-key-highlights)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

<br>

## 📖 Overview

Real ATMs need to reliably verify identity, track balance, and remember transaction history between sessions. This project recreates that entire behavior using only core Python — no database, no external libraries — by combining secure input handling with simple file-based persistence. It was built to practice clean CLI design, state management, and real-world input validation.

<br>

## 🎬 Demo

```
           ╔══════════════════════════════════╗
           ║     WELCOME TO HDFC ATM MACHINE  ║
           ╚══════════════════════════════════╝

        Balance Check                   Enter  →  0
        Minimum Balance Check           Enter  →  1
        Withdraw                        Enter  →  2
        Deposit                         Enter  →  3
        Transaction History             Enter  →  4
        Exit                            Enter  →  5

  🔒 Password Protected

Enter PIN: ****
✅ PIN Correct! Account Unlocked. Welcome!
```

> 📸 *Add a real terminal screenshot here once available, for an even stronger first impression.*

<br>

## ✨ Features

- 🔐 **PIN Protection** — account locks after 3 incorrect attempts
- 💰 **Balance Check** — view current balance instantly
- 💸 **Smart Withdraw** — enforces a ₹1,000 minimum balance automatically
- 💵 **Deposit Money** — add funds with full validation
- 📋 **Transaction History** — every withdrawal/deposit permanently logged
- ✅ **Input Validation** — invalid or negative amounts safely rejected, no crashes
- 💾 **Data Persistence** — balance and history survive program restarts

<br>

## 🛠 Tech Stack

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![File Handling](https://img.shields.io/badge/-File%20Handling-4B8BBE?style=flat-square)

<br>

## 🚀 Installation & Usage

```bash
# Clone the repository
git clone https://github.com/Charan-Code600/atm-machine.git
cd atm-machine

# Run the program
python atm.py
```

**Default PIN:** `1234` (3 attempts allowed before lockout)

<br>

## 📋 Menu Options

| Option | Action |
|:------:|--------|
| 0 | Check current balance |
| 1 | Check how much you can safely withdraw |
| 2 | Withdraw money |
| 3 | Deposit money |
| 4 | View transaction history |
| 5 | Exit |

<br>

## 📁 Project Structure

```
atm-machine/
├── atm.py          # Main program
├── balance.txt     # Auto-generated — stores current balance
└── history.txt     # Auto-generated — stores transaction log
```

<br>

## 💡 Key Highlights

- Zero external dependencies — runs on any machine with Python installed
- Minimum-balance logic prevents overdraft on every withdrawal path
- Balance and history persist automatically, no manual save step needed
- Account auto-locks after 3 failed PIN attempts for basic security

<br>

## 🔮 Future Improvements

- [ ] Multi-user support with separate account files
- [ ] Encrypted PIN storage instead of plain-text check
- [ ] Interest calculation on stored balance
- [ ] GUI version using Tkinter

<br>

## 👤 Author

**Charan Aade** — Python & Data Analysis Developer

🔗 [GitHub](https://github.com/Charan-Code600) • [LinkedIn](https://linkedin.com/in/charanaade)

<br>

<div align="center">

![License](https://img.shields.io/badge/License-MIT-FFB800?style=for-the-badge)

</div>





