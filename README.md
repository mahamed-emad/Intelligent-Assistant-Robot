# 🤖 Intelligent Assistant Robot
Intelligent Assistant Robot is a versatile Windows automation tool that allows you to manage system tasks and run common applications quickly and efficiently.

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.10+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)

**A versatile Windows automation tool for managing system tasks and running applications quickly and efficiently**

</div>

---

## 🌟 Overview

**Intelligent Assistant Robot** is a powerful Windows automation assistant that enables you to control system tasks and launch common applications with speed and ease through a simple, elegant graphical interface.

## ✨ Features

- 🎧 **Bluetooth Management** - Easily add and manage earphones
- 🌐 **Application Launcher** - Open Edge, VS Code, and File Explorer with one click
- 🪟 **Window Control** - Minimize all windows or a specific window
- 🔔 **Notification Management** - Control system notifications
- ⚙️ **Task Manager Access** - Quick access to Task Manager
- 🎨 **Simple User Interface** - Clean and user-friendly design

## 📋 Requirements

- **Operating System:** Windows 10/11
- **Python:** Version 3.10 or higher
- **Required Libraries:**
  - `pyautogui`
  - `pygetwindow`
  - `pyperclip`
  - `tkinter` (included with Python)
  - `ctypes` (included with Python)

## 🚀 Installation & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Mahamed-Emad/Intelligent-Assistant-Robot.git
cd Intelligent-Assistant-Robot
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python src/intelligent_assistant_robot.py
```

## 🔧 Build Executable (Optional)

To create a standalone executable file that doesn't require Python:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole --icon="Intelligent Assistant Robot.ico" "src/intelligent_assistant_robot.py"
```

The executable will be created in the `dist/` folder.

## 📁 Project Structure

```
Intelligent-Assistant-Robot/
│
├── src/
│   └── intelligent_assistant_robot.py   # Main application
├── README.md                             # Project documentation
└── Intelligent Assistant Robot.ico      # Application icon
```

## 📦 requirements.txt Content

```txt
pyautogui>=0.9.54
pygetwindow>=0.0.9
pyperclip>=1.8.2
```

## 🎯 How to Use

1. Launch the application via Python or the executable file
2. Select the desired command from the graphical interface
3. Click the button to execute the operation

## 🏷️ Releases

### v1.0.0 - First Release

**Release Date:** December 2025

**Features:**
- ✅ Bluetooth management and earphone setup
- ✅ Open Edge, VS Code, and File Explorer
- ✅ Window and notification control
- ✅ Simple GUI for easy command execution

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Bug Reports & Feature Requests

If you encounter any issues or have suggestions for new features, please open an issue on GitHub.

## 👨‍💻 Developer

<div align="center">

**Made With Love ❤️ By Mahamed Emad**

[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=social&logo=github)](https://github.com/Mahamed-Emad)

</div>

---

<div align="center">

### ⭐ If you like this project, don't forget to give it a star!

</div>
