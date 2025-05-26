Author: Vishal | CMD-Based Google Dork Tool for Bug Hunting
# BugDork


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
        or
   pip install -r requirements.txt --break-system-packages

## Usage 
  python bugdork.py --help
 
  python bugdork.py --list
 
  python bugdork.py --domain example.com --type login

  python bugdork.py --domain example.com --type config --open
