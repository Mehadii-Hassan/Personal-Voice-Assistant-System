# Personal-Voice-Assistant-System (Mehu)

"MEHU" is a python-based voice assistant that can interact with the user through speech recognization, perform tasks like opening applications, searching on Google or Wikipedia, playing music randomly, telling jokes, and having small talk.

This project uses speech recognization and text-to-speech (TTS) to provide a hands-free assistant experience similar to Iron Man's JARVIS.


## 🛠 Features
   
- Greet the user according to the time of day (morning, afternoon, evening)
- Recognize voice commands using Google Speech Recognition
- Speak responses using pyttsx3
- Time & Date announcements
- Wikipedia search with spoken summary
- Open websites like Google, Facebook, YouTube, Linkedin, Github
- Close websites like Google, Facebook, YouTube, Linkedin, Github
- Play random music from a specified folder
- Open system applications: Calculator, Notepad, CMD
- Close system applications: Calculator, Notepad, CMD
- Open Calendar (Google Calendar via browser)
- Tell jokes and respond to basic small talk
- Exit gracefully with a voice command


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

## Author
**Md. Mehadi Hassan**

Inspired by Boktiar Ahmed Bappy


## License

This project is open-source and free to use for learning purposes.
