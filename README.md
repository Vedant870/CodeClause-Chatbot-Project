# 🤖 Rule-Based Chatbot using Python & NLTK
> Internship Project - CodeClause August 2025  
> Level: Entry | Category: AI | Project 1 of 4  

---

## 📌 Overview

This is a simple **rule-based chatbot** built using **Python**, **NLTK**, and **regular expressions**. It mimics basic human-like responses using predefined patterns and a minimal NLP pipeline.

✅ Key Features:
- Rule-based conversation engine
- Predefined responses using pattern matching
- Easy to extend and customize
- Simple command-line interface
- Lightweight and beginner-friendly

---

## 🧠 Tech Stack

| Tech               |Description                                  |
|--------------------|---------------------------------------------|
| 🐍 Python 3.x     | Core programming language                    |
| 📚 NLTK           | NLP Toolkit (for tokenization, stemming)     |
| 🧠 Regex          | For intent and pattern recognition           |
| 🔧 re, random     | Standard libraries for logic and variation   |

---

## 📁 Project Structure

```bash
CodeClause-Chatbot-Project/
│
├── bot_core.py       # 🔁 Chatbot engine and logic
├── main.py           # 🎯 Entry point to run the chatbot
├── requirements.txt  # 📦 All dependencies
├── .gitignore        # 🚫 Files to be ignored in Git
└── README.md         # 📘 This file# CodeClause-Chatbot-Project
Simple Rule-based Chatbot using Python and NLTK - CodeClause August 2025 Internship Project

🛠️ How to Setup and Run
✅ 1. Clone or Download
bash
Copy
Edit
git clone https://github.com/<your-username>/CodeClause-Chatbot-Project.git
cd CodeClause-Chatbot-Project
✅ 2. Install Required Libraries
bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt doesn't exist yet, run:

bash
Copy
Edit
pip install nltk
pip freeze > requirements.txt
✅ 3. Run the Chatbot
bash
Copy
Edit
python main.py
🎉 That’s it! You’ll see:

css
Copy
Edit
🤖 Hello! I’m a simple chatbot. Type "exit" to quit.
>>>
✨ Sample Output
bash
Copy
Edit
🤖 Hello! I’m a simple chatbot. Type "exit" to quit.
>>> hello
🤖 Hey there!

>>> how are you?
🤖 I’m doing great, thank you!

>>> what is your name?
🤖 I'm your friendly chatbot buddy!

>>> bye
🤖 Goodbye! Have a great day ahead!
🧠 How It Works (Internally)
Uses Regex patterns to identify user inputs

Matches them to intent-based responses

Tokenization and text cleaning with NLTK

Responses are non-AI, rule-based only

👨‍💻 Author
Vedant Kasaudhan
CodeClause Intern – August 2025
GitHub: Vedant870
