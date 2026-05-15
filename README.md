# Real-Time Syntax Highlighter (PCAL)

![Python](https://img.shields.io/badge/Python-3-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![Status](https://img.shields.io/badge/status-completed-brightgreen)

This project is a **real-time, grammar-based** syntax highlighter.

---

### Dark Mode

<img width="498" height="412" alt="pcal_dark" src="https://github.com/user-attachments/assets/060a749a-c3fc-4a8f-9759-5b9c61deab8a" />

---

### Light Mode

<img width="498" height="412" alt="pcal" src="https://github.com/user-attachments/assets/0dea591d-a954-4379-841e-b5c705cf0be8" />

---

## 📂 Project Structure

```text
Realtime_Syntax_Highlighter_PCAL/
│── gui.py           # Tkinter-based real-time syntax highlighting interface
│── lexer.py         # Lexical analyzer (tokenization using regex)
│── parser.py        # Recursive descent parser for grammar validation
│── deneme.pcal      # Sample PCAL source code
│── dark.png         # Dark mode screenshot
│── light.png        # Light mode screenshot
│── makale.pdf       # Project paper
│── rapor.pdf        # Detailed technical report
│── README.md
└── __pycache__/     # Python cache files
```

---

## 🔍 Project Overview

The application consists of the following core components:

- **Lexical Analyzer (Lexer)**: Tokenizes the input based on regular expressions.  
- **Syntax Analyzer (Parser)**: Checks the token sequence against a context-free grammar.  
- **Highlighting Engine**: Assigns colors based on token types.  
- **GUI**: Developed using Tkinter, highlights syntax in real-time as the user types.  

> ⚠️ No ready-made highlighting libraries were used.

---

## 🛠 Technologies Used

- **Programming Language**: Python 3  
- **GUI**: Tkinter  
- **Parser Type**: Top-Down (Recursive Descent)  
- **Lexer Method**: State Diagram & Programmatic Implementation  
- **Language**: PCAL (simple, educational custom programming language)  

---

## ✅ Highlighted Token Types

| Token Type   | Description                                                                 |
|--------------|----------------------------------------------------------------------------|
| IDENTIFIER   | Represents variable or function names. Consists of letters.               |
| NUMBER       | Integer constants.                                                         |
| OPERATOR     | Basic mathematical operators such as +, -, *, /.                          |
| EQUALS       | Assignment operator (`=`).                                                 |
| QUESTION     | Used to retrieve the result of an operation (`?`).                         |
| DELIMITER    | Separator for end-of-line (`,` in this project).                           |
| PAREN        | Parentheses to indicate operation precedence (`(` and `)`).               |

---

## 📺 Demo Video

You can watch the project demo video at the link below:

🔗 [YouTube Demo Video](https://www.youtube.com/watch?v=eCkWtttOFr0)

---

## 📄 Paper

A detailed write-up explaining the methods and development process used in this project:

🔗 [Paper Link](https://github.com/AFurkanOcel/Realtime_Syntax_Highlighter_PCAL/blob/main/makale.pdf)

---

## 📘 Documentation

🔗 [Project Report (PDF)](https://github.com/AFurkanOcel/Realtime_Syntax_Highlighter_PCAL/blob/main/rapor.pdf) – Detailed technical documentation and full explanation of the development process.

### ➤ Language and Grammar Selection
The project is implemented using PCAL, a simple, educational language. Its grammar was defined and applied within the project.

### ➤ Syntax Analysis
Top-down recursive descent method was used for syntax analysis. Input is validated against the defined grammar.

### ➤ Lexical Analysis
The lexer is developed from scratch in Python using regular expressions and operates based on a state diagram.

### ➤ Parser Method
Top-down approach using recursive descent technique for syntax validation.

### ➤ Highlighting Scheme
Each token type is assigned a distinct color using the `Text` widget with `tag_config()`.

### ➤ GUI Implementation
The interface highlights syntax in real-time as the user types. The GUI is simple and user-friendly.

---

## 👤 Developer

**A. Furkan ÖCEL**
