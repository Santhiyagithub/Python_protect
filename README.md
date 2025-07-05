# Python_protect
Protecting Python Application from Reverse Engineering

# Python App Protection Using Pyarmor

This project demonstrates a practical method to **protect a Python application** from being reverse-engineered, copied, or tampered with.

We use an open-source tool called **Pyarmor** to obfuscate Python code and make it unreadable while still executable.

---

## 🎯 Objective

To prevent unauthorized users from accessing or understanding sensitive Python logic by transforming `.py` files into **secure, obfuscated bytecode** that cannot be easily reverse-engineered.

---

## 🧠 Description

Python source code is typically in plain text and easy to inspect. This poses a risk when deploying apps with:

- Proprietary algorithms
- Sensitive business logic
- Licensing constraints

Using **Pyarmor**, we obfuscate `.py` files into unreadable code that **preserves functionality** but **hides the logic** from users.

---

## 🛠️ Technologies Used

| Tool/Library     | Purpose                               |
|------------------|----------------------------------------|
| Python           | Main programming language              |
| Pyarmor          | Obfuscates Python files for protection |
| VS Code / Terminal | For local execution and testing      |

---

## 📄 Files in this Project

ProtectPython/
│
├── protect_python.py # Original Python app (with sensitive logic)
├── dist/protect_python.py # Obfuscated version (created by Pyarmor)
├── requirements.txt # Required package (pyarmor)
├── screenshots/ # Before and after screenshots
├── report.pdf # Summary of the task
└── README.md # This file


---

## 🔧 How to Use

### 1. Install Pyarmor
    ```bash
    pip install pyarmor

### 2. Obfuscate your Python file
    ```bash
    pyarmor obfuscate hello.py

### 3. Run the protected file
    ```bash
    python dist/hello.py


### Obfuscated Output

__pyarmor__(__name__, __file__, b'\x00\x00...')



