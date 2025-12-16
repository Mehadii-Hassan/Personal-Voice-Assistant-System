# 🎙 Personal Voice Assistant — **Mehu**
**Mehu** is a Python-based offline voice assistant designed for a seamless **hands-free automation experience**, inspired by Iron Man’s **JARVIS**. It understands natural voice commands and performs useful system and web-based tasks with voice + terminal responses.


##  Capabilities
-  Time-aware greetings (Morning / Afternoon / Evening)
-  Speech recognition using **Google STT**
-  Voice responses using **pyttsx3 (Offline TTS)**
-  Announces **current date & time**
-  **Wikipedia search** with spoken summaries
-  Open browser sites: **Google, YouTube, Facebook, GitHub, LinkedIn, Calendar**
-  Close only the **active browser tab** (no full browser shutdown)
-  Create / delete folders via voice
-  Save & recall **memory notes** using a `.txt` file
-  Capture screenshots with auto **date-time filename**
-  Control & play random local music from folder
-  Open system apps: **Notepad, Calculator, CMD**
-  Close system apps via voice
-  Tell jokes & small talk responses
-  Exit assistant smoothly with a voice command


##  Tech Stack
- **Language:** Python 3.11+
- **APIs / Libraries:** `SpeechRecognition`, `pyttsx3`, `wikipedia`, `pyautogui`, `keyboard`, `os`
- **Runs Offline:** Yes (Except STT)


##  Prerequisites
- Python **3.11 or higher**
- A working microphone (Mobile mic via **WO Mic** is supported)


## Requirements

- python 3.11 or higher


## How to run?

1. Create a virtual environment

```bash
conda create --prefix .\venv python=3.11 -y
```

2. Activate virtual environment

```bash
conda activate .\venv
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

## 🎥 Demo Video

▶️ Watch the demo here:  
[https://www.linkedin.com/posts/md-mehadi-hassan-cse_python-nlp-artificialintelligence-activity-7405672960776122368-mbhY?utm_source=share&utm_medium=member_desktop&rcm=ACoAAF59OiEBnUq-S7MNLSIjP3CnLpOTzgPZflc](https://www.linkedin.com/posts/md-mehadi-hassan-cse_ai-pythonautomation-voiceassistant-activity-7400609475004628992-Fw-H?utm_source=share&utm_medium=member_desktop&rcm=ACoAAF59OiEBnUq-S7MNLSIjP3CnLpOTzgPZflc)

## Author
**Md. Mehadi Hassan**

Inspired by - **Boktiar Ahmed Bappy**


## License

This project is open-source and free to use for learning purposes.
