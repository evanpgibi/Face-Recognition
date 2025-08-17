# Face Recognition System

A Python-based face recognition system using OpenCV (Haar Cascade) and the Face++ API.  
Includes a compiled `.exe` for easy use without requiring Python installation.

---

## Features
- Detects faces using Haar Cascade classifier  
- Performs recognition with Face++ API  
- Works as both a Python script and a Windows EXE  
- Stores known faces in `faces.json`  
- Configurable securely via `config.json` (created from example file)

---

## 📥 Installation (Source Code)
1. Clone the repository:
   ```bash
   git clone https://github.com/evanpgibi/Face-Recognition.git
   cd Face-Recognition
###Install dependencies:
pip install -r requirements.txt

---

## ⚙️ Configuration (Important!)
This project requires a config.json file with your Face++ API credentials.
To keep your keys private, the real config.json is ignored by Git.

###Copy the example config file:

cp config.example.json config.json
(On Windows: duplicate config.example.json and rename to config.json)

###Open config.json and add your Face++ keys:

{
  "FACESET_TOKEN": "YOUR_FACESET_TOKEN",
  "API_KEY": "YOUR_API_KEY_HERE",
  "API_SECRET": "YOUR_API_SECRET_HERE"
}
Save the file. The program will now load your credentials without exposing them on GitHub.

##▶️ Usage
###Run with Python:

python Face_Recognition.py

###Or run the EXE:

Face_Recognition.exe
