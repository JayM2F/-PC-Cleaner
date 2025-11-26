🖥️ PC Cleaner

Clean your Windows PC with one click! This tool removes temporary files, browser caches, and empties the recycle bin, freeing up space and improving performance.

✨ Features

🗑 Clean temporary folders (C:\Windows\Temp, user temp, prefetch)

🌐 Clear browser caches for Chrome, Edge, Firefox

🗑 Empty the Windows Recycle Bin

💾 Live log display in GUI showing all actions and space freed

📝 Automatically logs cleaning actions with timestamps

🎨 Customizable GUI with dark mode colors

⚡ Quick and easy one-click cleaning

📦 Requirements

Before starting, make sure you have:

Python 3.10+

Windows OS (tested on Windows 10/11)

🔧 Installation

Clone the repository:

git clone https://github.com/JayM2F/pc-cleaner
cd pc-cleaner


Run the program:

python main.py
# or
python3 main.py

🚀 Usage

Quick Start

Open main.py to launch the GUI.

Click Run Cleaner to start cleaning.

Monitor logs in real time.

After completion, a summary message box shows total space freed.

Exit

Click the Exit Cleaner button to close the program.

📂 Project Structure
pc-cleaner/
├── pc_cleaner_gui          # Main program entry point with GUI
├── pc_cleaner_cli          # Core functions for cleaning and logging
├── README.md               # This file
└── PC_Cleaner_Logs/        # Automatically created log folder

🖥 Supported Operating Systems

✅ Windows 10 / 11

📝 Dependencies

Python Packages:

Package	Purpose
tkinter	GUI creation
scrolledtext	Scrollable text box for logs

External:

Windows OS features for recycle bin cleaning

⚖️ License

This project is open source and intended for educational purposes.

Warning: This tool is for cleaning your own PC. Do not delete files from someone else’s computer without permission.

🌟 Contributors

JayM2F

Made with ❤️ by the collaborative team
