# Password Strength Analyzer with Custom Wordlist Generator

This is a Python-based desktop application that helps you analyze the strength of a password and generate a custom wordlist using basic personal information. It's a useful tool for learning about password security and creating targeted dictionaries for ethical hacking and penetration testing

---

## Features

- Analyze password strength using the `zxcvbn` algorithm
- View estimated crack time, guesses needed, and suggestions
- Score interpreted on a scale from Very Weak to Very Strong
- Generate custom wordlists using:
  - Name, birth year, pet name, favorite word/team
  - Leetspeak variations and common suffixes like `123`, `@2025`, etc.
- Export results and wordlists as `.txt` files
- Clean and easy-to-use GUI built with Tkinter

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/seetharamdamarla/password-security-tool.git
cd password-security-tool
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

> Make sure you're using **Python 3.8+** and have Tkinter (usually pre-installed).

---

## How to Run

```bash
python gui.py
```

This will launch the GUI where you can:
- Input a password and analyze its strength
- Fill in personal details and generate a custom wordlist
- Save the results locally

---

## Requirements

- Python 3.8 or higher
- `zxcvbn` library
- Tkinter (standard with most Python installations)

---

## License

MIT License – use freely for ethical and legal purposes.

---

## Disclaimer

This tool is for **educational and ethical use only**.  
Do **not** use it for unauthorized access or malicious activity. Always respect privacy and legal boundaries.
