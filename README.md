#     ____              ____             __
#    / __ )__  ______ _/ __ \____  _____/ /__
#   / __  / / / / __ `/ / / / __ \/ ___/ //_/
#  / /_/ / /_/ / /_/ / /_/ / /_/ / /  / ,<
# /_____/\__,_/\__, /_____/\____/_/  /_/|_|
#             /____/

Author: Vishal | CMD-Based Google Dork Tool for Bug Hunting
# BugDork


[![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/yourgithubusername/bugdork.svg?style=social&label=Stars)](https://github.com/yourgithubusername/bugdork/stargazers)

> **BugDork** is a powerful, command-line Google Dork tool designed for bug hunters and security researchers to generate effective Google search queries targeting specific domains.

---

## 🚀 Features

- Simple and user-friendly command-line interface  
- Supports multiple customizable dork categories  
- Loads dork templates dynamically from the `dorks/` directory  
- Option to open dork URLs automatically in the default browser  
- Stylish colored ASCII banner using `pyfiglet` and `termcolor`  
- Lightweight and easy to extend with minimal dependencies  

---

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourgithubusername/bugdork.git
   cd bugdork
   
   pip install -r requirements.txt

## Usage 
  python bugdork.py --help
 
  python bugdork.py --list
 
  python bugdork.py --domain example.com --type login

  python bugdork.py --domain example.com --type config --open
