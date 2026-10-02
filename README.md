

<!-- ==================== Title ==================== -->

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:FFB800,100:FF8C00&height=150&section=header&text=ATM%20Machine&fontSize=60&fontColor=000000&animation=fadeIn&fontAlignY=35" width="100%"/>
</div>


<!-- ==================== Tagline ==================== -->

<div align="center">
<h3 style="color: #FFB800;">A fully functional command-line ATM system with PIN security, real-time balance tracking, and persistent transaction history — built entirely in Python.</h3>
</div>


<!-- ==================== Border Line ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>



<!-- ==================== Badges ==================== -->


<div align="center">
  <div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:FFB800,100:FF8C00&height=80&section=header&text=Badges&fontSize=60&fontColor=000000&fontAlignY=50" width="400"/>
</div>
  
<p align="center">
  <svg width="35" height="35" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M12 21L3 12H8V3H16V12H21L12 21Z" fill="#FFD700" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
</p>
  
</div>

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-00C851?style=for-the-badge&logo=checkmarx&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-FFB800?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-PIN%20Protected-FF4444?style=for-the-badge&logo=shieldcheck&logoColor=white)

</div>
















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
