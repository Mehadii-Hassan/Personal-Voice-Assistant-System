import speech_recognition as sr
import pyttsx3
import logging
import os
import datetime
import wikipedia
import webbrowser
import random
import subprocess
import google.generativeai as genai
import pyautogui

# Logging configuration
LOG_DIR = "logs" #folder name "logs"
LOG_FILE_NAME = "application.log" #file name

os.makedirs(LOG_DIR, exist_ok=True)
log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename= log_path,
    format= "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)

# Activating voice from our system
engine = pyttsx3.init("sapi5") #initialization
engine.setProperty("rate", 170) #voice speed control
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

# This is speak function
def speak(text):
    """This function converts text to voice"""
    print(f"Mehu: {text}")
    engine.say(text)
    engine.runAndWait() #for closing

#This function recognize the speech and convert it to text
def takeCommand():
    """This function takes command and recognize
    return:
        text as query
    """
    r = sr.Recognizer() #initialization
    with sr.Microphone() as source: 
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        
        # --- Misheard corrections ---
        corrections = {
            "main hoon": "mehu",
            "may hu": "mehu",
            "man who": "mehu",
            "mehu": "mehu",
            "mihu" : "mehu",
            "main hun" : "mehu",
            "mehul" : "mehu",
            "mehboob" : "mehu",
            "mein hun" : "mehu",
            "pihu" : "mehu"
        }
        for wrong, correct in corrections.items():
            query = query.lower().replace(wrong, correct)

        print(f"User Said : {query}\n")
    except Exception as e:
        logging.info(e)
        print("Say that again please")
        return "None" 
    return query

def greeting():
    hour = (datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am at your service, please tell me how I can help you?")
greeting()

# Google Search
def google_search(query):
    search = query.replace("search google for", "")
    speak(f"Searching Google for {search}")
    webbrowser.open(f"https://www.google.com/search?q={search}")
    logging.info("Google search done")

#music..
def play_music():
    global music_playing
    music_playing = True

    music_dir = "C:\\Users\\Mehedi\\Desktop\\Personal-Voice-Assistant-System\\music"
    try:
        songs = os.listdir(music_dir)
        if songs:
            random_song = random.choice(songs)
            speak("Playing a random song Sir")
            os.startfile(os.path.join(music_dir, random_song))
            logging.info(f"Music played: {random_song}")
        else:
            speak("No music files found in your music directory.")
    except Exception as e:
        speak("Sorry Sir, I could not find your music folder.")
        logging.error(f"Music folder error: {e}")
    music_playing = False  # reset flag after execution

# Memory / Notes
def save_memory(text):
    with open("memory.txt", "a") as f:
        f.write(text + "\n")
    speak("Ok Sir, I remembered it in my memory")
    logging.info("Memory saved")

def read_memory():
    if os.path.exists("memory.txt"):
        with open("memory.txt", "r") as f:
            data = f.read()
        speak("Here is your saved memory")
        speak(data)
    else:
        speak("No memory found")
    logging.info("Memory read")

# Folder Create/Delete
def create_folder(name):
    os.makedirs(name, exist_ok=True)
    speak(f"Folder {name} created Sir")
    logging.info("Folder created")

def delete_folder(name):
    try:
        os.rmdir(name)
        speak(f"Folder {name} deleted Sir")
        logging.info("Folder deleted")
    except:
        speak("Folder could not be deleted")
        logging.error("Folder delete error")
    
# Screenshot Capture
def take_screenshot():
    ts = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    img = f"screenshot_{ts}.png"
    pyautogui.screenshot(img)
    speak("Screenshot taken Sir")
    logging.info("Screenshot saved")

# Closing Tab
def close_tab():
    pyautogui.hotkey('ctrl', 'w')
    logging.info("Current tab closed")

#gemini model
def gemini_model_response(user_input):
    GEMINI_API_KEY = "AIzaSyCA6SSKl2BMeQN3y327ZHEnYOWr1N1ZS2w"
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"You are my personal Assistant. Answer the provided question in short, Question: {user_input}"
    response = model.generate_content(prompt)
    result = response.text

    return result

while True:
    query = takeCommand()
    if query is None:
        continue  
    query = query.lower()

    #normal communication...
    if "your name" in query:
        speak("My name is Mehu")
        logging.info("User asked for assistant's name.")
    
    elif "how are you" in query or "are you" in query or "r u" in query:
        speak("I am fine, Thank you for asking me Sir!")
        logging.info("User asked for assistant's well-being.")
    
    elif "made you" in query:
        speak("I was created by Mehadi Hassan Sir")
        logging.info("User asked about assistant's creator.")
     
    elif "who is mehadi?" in query or "mehadi" in query or "mehedi" in query or "hassan" in query:
        speak("Mehadi Hassan, a CSE student at IUBAT and a learner at INCEPTION BD, is an aspiring AI and Data Science enthusiast exploring Machine Learning, Deep Learning, and Generative AI.")
        logging.info("User asked about assistant's creator.")
    
    elif "what is inception bd?" in query or "inception bd" in query or "inception" in query or "bd" in query:
        speak("INCEPTION BD is a leading Bangladesh-based tech learning community and training platform working on AI, Machine Learning, Deep Learning, Generative AI, and Data Science. It supports learners through workshops, bootcamps, competitions, hackathons, and project-based mentorship. Industry experts like Boktiar Ahmed Bappy and Md. Ridoy Hossain actively mentor and host AI and Data Science initiatives in the community.")
        logging.info("User asked about INCEPTION BD.")

    elif "thank" in query or "thank you" in query:
        speak("It's my pleasure Sir, Always happy to help")
        logging.info("User expressed gratitude..")

    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir the time is {strTime}")
        logging.info("User asked for current time.")

    #web browsing....
    elif "open google" in query:
        speak("ok sir, opening google.")
        webbrowser.open("https://www.google.com/")
        logging.info("User requested to open google.")
    elif "close google" in query:
        speak("Closing Google browser.")
        logging.info("Chrome browser closed.")
        close_tab()
    
    elif "open facebook" in query:
        speak("ok sir, opening facebook.")
        webbrowser.open("https://www.facebook.com")
        logging.info("User requested to open facebook.")
    elif "close facebook" in query:
        speak("Closing Facebook.")
        close_tab()

    elif "open github" in query or "git" in query:
        speak("ok sir, opening github.")
        webbrowser.open("https://github.com/Mehadii-Hassan")
        logging.info("User requested to open github.")
    elif "close github" in query:
        speak("Closing GitHub.")
        close_tab()
    
    elif "open linkedin" in query or "linkdin" in query:
        speak("ok sir, opening linkedin.")
        webbrowser.open("https://www.linkedin.com")
        logging.info("User requested to open linkedin.")
    elif "close linkedin" in query:
        speak("Closing LinkedIn.")
        close_tab()

    elif "open calendar" in query:
        speak("ok sir, opening calendar.")
        webbrowser.open("https://calendar.google.com")
        logging.info("User requested to open calendar.")
    elif "close calendar" in query:
        speak("Closing Calendar.")
        close_tab()

    #youtube search...
    elif "open youtube" in query:
        speak("ok sir, opening youtube.")
        query = query.replace("youtube", "")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        logging.info("User requested to search on youtube.")
    elif "close youtube" in query:
        speak("Closing YouTube.")
        close_tab()

    #system file...
    elif "close calculator" in query:
        speak("Closing Calculator.")
        subprocess.call(["taskkill", "/F", "/IM", "CalculatorApp.exe"])
        logging.info("Calculator closed.")
    elif "open calculator" in query or "calculator" in query:
        speak("ok sir, opening calculator.")
        subprocess.Popen("calc.exe")
        logging.info("User requested to open calculator.")
    
    elif "close notepad" in query:
        speak("Closing Notepad.")
        subprocess.call(["taskkill", "/F", "/IM", "notepad.exe"])
        logging.info("Notepad closed.")
    elif "open notepad" in query or "notepad" in query:
        speak("ok sir, opening notepad.")
        subprocess.Popen("notepad.exe")
        logging.info("User requested to open notepad.")
        
    #comand prompt
    elif "open terminal" in query or "open cmd" in query:
        speak("opening command prompt terminal")
        subprocess.Popen("cmd.exe")
        logging.info("User requested to open command prompt.")
    elif "close terminal" in query or "close cmd" in query:
        speak("Closing Command Prompt.")
        subprocess.call(["taskkill", "/F", "/IM", "cmd.exe"])
        logging.info("Command prompt closed.")

    #jokes...
    elif "joke" in query:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the math book look sad? Because it had too many problems.",
            "Why don't skeletons fight each other? They don't have the guts.",
            "Why did the computer go to the doctor? Because it caught a virus!",
            "Why did the scarecrow win an award? Because he was outstanding in his field.",
            "Why don't eggs tell jokes? They'd crack each other up.",
            "Why did the bicycle fall over? Because it was two-tired.",
            "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
            "Why did the student eat his homework? Because the teacher said it was a piece of cake.",
            "Why can't your nose be 12 inches long? Because then it would be a foot!"
        ]
        speak(random.choice(jokes))
        logging.info("User requested a joke.")
    
    #search wikipedia...
    elif "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        speak(result)
        logging.info("User requested to information form wikipedia.")
    
    #play music
    elif "close music" in query or "close song" in query:
        speak("Closing Music player.")
        subprocess.call(["taskkill", "/F", "/IM", "wmplayer.exe"])
        logging.info("Music player closed.")
    elif "play music" in query or "music" in query or "song" in query:
        play_music()
    
    # remember
    elif "remember this" in query:
        save_memory(query.replace("remember this", "").strip())

    elif "what did you remember" in query or "did you remember" in query:
        read_memory()
    
    # folder create or delete
    elif "create folder" in query or "new folder" in query or "make folder" in query:
        folder_name = query.replace("create folder", "")
        folder_name = folder_name.replace("new folder", "")
        folder_name = folder_name.replace("make folder", "")
        folder_name = folder_name.strip()
        create_folder(folder_name)

    elif "delete folder" in query or "remove folder" in query:
        folder_name = query.replace("delete folder", "")
        folder_name = folder_name.replace("remove folder", "")
        folder_name = folder_name.strip()
        delete_folder(folder_name)
    
    # take screenshot
    elif "take a screenshot" in query or "screenshot" in query:
        take_screenshot()
    
    elif "exit" in query or "stop" in query or "bye" in query:
        speak("Thank you for you time Sir. Have a great day ahead!")
        logging.info("User exit the program.")
        exit() 

    else:
        response = gemini_model_response(query)
        speak(response)
        logging.info("User asked for others question.")
