



<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:FFB800,100:FF8C00&height=150&section=header&text=ATM%20Machine&fontSize=60&fontColor=000000&animation=fadeIn&fontAlignY=35" width="100%"/>
</div>

<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=18&pause=1000&color=FFB800&center=true&vCenter=true&width=600&repeat=false&lines=%F0%9F%94%92+Secure+PIN-Protected+ATM+Simulator+%7C+%F0%9F%92%BE+Persistent+Data+Storage)](https://git.io/typing-svg)

</div>
### A secure, PIN-protected ATM simulator built in Python with persistent data storage — no database required.

</div>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

## 📑 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation & Usage](#-installation--usage)
- [Menu Options](#-menu-options)
- [Project Structure](#-project-structure)
- [Highlights](#-highlights)
- [Future Improvements](#-future-improvements)
- [Author](#-author)
- [License](#-license)

## 📖 Overview

Real ATMs need to reliably track balance, enforce security, and remember transaction history between sessions — this project recreates that behavior entirely with core Python, using file handling instead of a database. It was built to practice secure input handling, persistent state management, and clean CLI design.

## ✨ Features

- 🔐 **PIN Protection** — account locks after 3 incorrect attempts
- 💰 **Balance Check** — view current balance instantly
- 💸 **Smart Withdraw** — enforces a ₹1,000 minimum balance rule automatically
- 💵 **Deposit Money** — add funds with validation
- 📋 **Transaction History** — every withdrawal/deposit permanently logged
- ✅ **Input Validation** — invalid or negative amounts safely rejected, no crashes
- 💾 **Data Persistence** — balance and history survive program restarts (file-based storage)

## 🛠 Tech Stack

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![File Handling](https://img.shields.io/badge/-File%20Handling-4B8BBE?style=flat-square)

## 🚀 Installation & Usage

```bash
# Clone the repository
git clone https://github.com/Charan-Code600/atm-machine.git
cd atm-machine

# Run the program
python atm.py
```

**Default PIN:** `1234` (3 attempts allowed before lockout)

## 📋 Menu Options

| Option | Action |
|:------:|--------|
| 0 | Check current balance |
| 1 | Check how much you can safely withdraw |
| 2 | Withdraw money |
| 3 | Deposit money |
| 4 | View transaction history |
| 5 | Exit |

## 📁 Project Structure

```
atm-machine/
├── atm.py          # Main program
├── balance.txt     # Auto-generated — stores current balance
└── history.txt     # Auto-generated — stores transaction log
```

## 💡 Highlights

- Zero external dependencies — runs on any machine with Python installed
- Minimum-balance logic prevents overdraft in every withdrawal path
- History and balance persist automatically without any manual save step

## 🔮 Future Improvements

- [ ] Multi-user support with separate account files
- [ ] Encrypted PIN storage instead of plain-text check
- [ ] Interest calculation on stored balance
- [ ] GUI version using Tkinter

## 👤 Author

**Charan Aade** — Python & Data Analysis Developer

🔗 [GitHub](https://github.com/Charan-Code600) • [LinkedIn](https://linkedin.com/in/charanaade)

## 📄 License

This project is licensed under the MIT License.
