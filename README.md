# Keylogging Simulation (Educational)

## 📌 Objective
This project demonstrates a basic keystroke logging mechanism in a controlled and ethical environment to understand how keylogging attacks work and analyze associated security risks.

## ⚙️ Technology Used
- Python 3
- pynput library

## 🧠 How It Works
- Captures keyboard input using event listeners
- Logs keystrokes locally into a text file
- Stops execution when ESC key is pressed
  
## Keylogging Risk Analysis

Keyloggers are commonly used by attackers to steal sensitive information such as login credentials. This simulation helps understand how easily keyboard inputs can be intercepted.

Organizations should implement endpoint detection, restrict script execution, and educate users about malware risks.

## ▶️ How to Run
```bash
pip install pynput
python keylogger.py
