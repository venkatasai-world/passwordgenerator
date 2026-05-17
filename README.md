# 🔐 Password Generator

A simple and secure Password Generator application where users can generate strong passwords by selecting the number of letters, symbols, and numbers.

The generated password can be copied and used for websites, apps, and online accounts to improve security and protect user data.

---

## 🚀 Features

- Generate secure and random passwords
- Customize:
  - Number of letters
  - Number of symbols
  - Number of numbers
- Easy-to-use interface
- Strong password generation
- Beginner-friendly Python project

---

## 🛠️ Technologies Used

- Python

---

## 📂 Project Structure

```bash
passwordgenerator/
│
├── main.py
├── README.md
└── requirements.txt
```

---

## ▶️ How It Works

The program asks the user for:

1. Number of letters
2. Number of symbols
3. Number of numbers

It then generates a random and secure password using the selected inputs.

---

## 💻 Example Output

```bash
Welcome to the Password Generator!

How many letters would you like in your password?
8

How many symbols would you like?
2

How many numbers would you like?
3

Generated Password:
aB7@kL9#2mQ5
```

---

## 📜 Python Code Example

```python
import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

nr_letters = int(input("How many letters would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = []

for char in range(nr_letters):
    password.append(random.choice(letters))

for char in range(nr_symbols):
    password.append(random.choice(symbols))

for char in range(nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)

final_password = "".join(password)

print("Generated Password:", final_password)
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/venkatasai-world/passwordgenerator.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd passwordgenerator
```

### 3️⃣ Run the Program

```bash
python main.py
```

---

## 📌 Requirements

No external libraries are required.

Example `requirements.txt`

```txt
# No external dependencies
```

---

## 🎯 Learning Objectives

This project helps beginners understand:

- Python Lists
- Loops
- Random Module
- String Manipulation
- User Input Handling
- Password Security Basics

---

## 🌟 Future Improvements

- Add password strength checker
- Add copy-to-clipboard feature
- Build a Flask web application
- Add dark mode UI
- Save passwords securely

---

## 🔗 GitHub Repository

:contentReference[oaicite:0]{index=0}

---

## 👨‍💻 Author

Created by Venkata Sai
