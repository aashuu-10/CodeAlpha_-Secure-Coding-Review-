# Secure Coding Review

## Project Overview

This project demonstrates a basic Secure Coding Review of a Python login application using static code analysis.

## Objective

The objective is to analyze Python code for security vulnerabilities and recommend secure coding practices.

## Features

- User Login Authentication
- Static Code Analysis using Bandit
- Security Review Report
- Secure Coding Recommendations

## Technologies Used

- Python 3
- Bandit
- VS Code

## Project Structure

```
Secure-Coding-Review
│── login.py
│── report.md
│── requirements.txt
│── .gitignore
│── README.md
```

## Installation

Install Bandit:

```bash
pip install bandit
```

Run the application:

```bash
python login.py
```

Analyze the code:

```bash
python -m bandit login.py
```

## Security Recommendations

- Avoid hardcoded credentials.
- Store passwords using hashing (bcrypt).
- Validate all user inputs.
- Store secrets in environment variables.

## Author

Ayush Kumar