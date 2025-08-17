# Face Recognition System

A Python-based face recognition system using OpenCV (Haar Cascade) and the Face++ API.  
Includes a compiled `.exe` for easy use without requiring Python installation.

---

## Features
- Detects faces using Haar Cascade classifier  
- Performs recognition with Face++ API  
- Works as both a Python script and a Windows EXE  
- Stores known faces in `Faces.json` locally
- Configurable securely via `config.json` (created from example file)

---

## 📥 Installation (Source Code)
1. Clone the repository:
   ```bash
   git clone https://github.com/evanpgibi/Face-Recognition.git
   cd Face-Recognition
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

---

## ⚙️ Configuration (Important!)
This project requires a config.json file with your Face++ API credentials.
To keep your keys private, the real config.json is ignored by Git.

1. Copy the example config file:
   ```bash
   cp config.example.json config.json
   (On Windows: duplicate config.example.json and rename to config.json)

2. Open config.json and add your Face++ keys:
   ```bash
   {
     "FACESET_TOKEN": "YOUR_FACESET_TOKEN",
     "API_KEY": "YOUR_API_KEY_HERE",
     "API_SECRET": "YOUR_API_SECRET_HERE"
   }

3. Save the file. The program will now load your credentials without exposing them on GitHub.

## ▶️ Usage
1. Run the exe (for non-programmers):
  Download the zip file from the Releases page, extract it, and double-click `Face_Recognition.exe` to run.

2. Run with Python:
   ```bash
   python Face_Recognition.py

   
