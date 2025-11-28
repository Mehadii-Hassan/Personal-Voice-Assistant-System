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
    """This function converts text to voice
    Args:
        text 
    Returns:
        voice
    """
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait() #for closing


#This function recognize the speech and convert it to text
def takeCommand():
    """This function takes command and recognize
    return:
        text as query
    """
    #this code taken from documentation
    r = sr.Recognizer() #initialization
    with sr.Microphone() as source: 
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
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

#gemini model
def gemini_model_response(user_input):
    GEMINI_API_KEY = ""
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"Your name is Mehu, you act like my personal AI Assistant. Answer the provided question in very short, Question: {user_input}"
    response = model.generate_content(prompt)
    result = response.text

    return result


while True:
    query = takeCommand()
    if query is None:
        continue  # restart loop if nothing recognized
    query = query.lower()
    print(f"User said: {query}")

    #normal communication...
    if "your name" in query:
        speak("My name is Mehu")
        logging.info("User asked for assistant's name.")
    
    elif "how are you" in query or "are you" in query or "r u" in query:
        speak("I am fine, Thank you for asking me Sir!")
        logging.info("User asked for assistant's well-being.")
    
    elif "who are you" in query or "who r you" in query or "who r u" in query:
        speak("My name is Mehu, and I serve as the personal assistant to Mehadi Hassan Sir")
        logging.info("User asked about assistant's creator.")
    
    elif "made you" in query:
        speak("I was created by Mehadi Hassan Sir")
        logging.info("User asked about assistant's creator.")
     
    elif "who is mehadi?" in query or "mehadi" in query or "mehedi" in query or "hassan" in query:
        speak("Mehadi Hassan is an aspiring AI and Data Science learner, actively exploring Machine Learning, Deep Learning and Generative AI.")
        logging.info("User asked about assistant's creator.")
    
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
        subprocess.call(["taskkill", "/F", "/IM", "chrome.exe"])
        logging.info("Chrome browser closed.")
    
    elif "open facebook" in query:
        speak("ok sir, opening facebook.")
        webbrowser.open("https://www.facebook.com")
        logging.info("User requested to open facebook.")
    elif "close facebook" in query:
        speak("Closing Facebook browser.")
        subprocess.call(["taskkill", "/F", "/IM", "chrome.exe"])
        logging.info("Chrome browser closed.")

    elif "open github" in query:
        speak("ok sir, opening github.")
        webbrowser.open("https://github.com/Mehadii-Hassan")
        logging.info("User requested to open github.")
    elif "close github" in query:
        speak("Closing GitHub browser.")
        subprocess.call(["taskkill", "/F", "/IM", "chrome.exe"])
        logging.info("Chrome browser closed.")
    
    elif "open linkedin" in query:
        speak("ok sir, opening linkedin.")
        webbrowser.open("https://www.linkedin.com")
        logging.info("User requested to open linkedin.")
    elif "close linkedin" in query:
        speak("Closing LinkedIn browser.")
        subprocess.call(["taskkill", "/F", "/IM", "chrome.exe"])
        logging.info("Chrome browser closed.")

    elif "open calendar" in query:
        speak("ok sir, opening calendar.")
        webbrowser.open("https://calendar.google.com")
        logging.info("User requested to open calendar.")
    elif "close calendar" in query:
        speak("Closing Calendar browser.")
        subprocess.call(["taskkill", "/F", "/IM", "chrome.exe"])
        logging.info("Chrome browser closed.")

    #youtube search...
    elif "open youtube" in query:
        speak("ok sir, opening youtube.")
        query = query.replace("youtube", "")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        logging.info("User requested to search on youtube.")
    elif "close youtube" in query:
        speak("Closing YouTube browser.")
        subprocess.call(["taskkill", "/F", "/IM", "chrome.exe"])
        logging.info("Chrome browser closed.")

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
        # This will close any running media files opened via default player (like Groove Music or VLC if open)
        subprocess.call(["taskkill", "/F", "/IM", "wmplayer.exe"])
        logging.info("Music player closed.")
    elif "play music" in query or "music" in query or "song" in query:
        play_music()
    
    elif "exit" in query or "stop" in query or "bye" in query:
        speak("Thank you for you time Sir. Have a great day ahead!")
        logging.info("User exit the program.")
        exit() 

    else:
        response = gemini_model_response(query)
        speak(response)
        logging.info("User asked for others question.")