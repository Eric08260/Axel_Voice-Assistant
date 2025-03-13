import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pyjokes
import os
import requests
import random
import subprocess

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        print("Could not request results, please check your internet connection.")
        return ""

def get_weather(city):
    api_key = "ce17d4720af67872f01b5e80451d8d21"  # Replace with a valid API key from OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response.get("main"):
        temp = response["main"]["temp"]
        weather = response["weather"][0]["description"]
        speak(f"The weather in {city} is {weather} with a temperature of {temp} degrees Celsius.")
    else:
        speak("Sorry, I couldn't fetch the weather information.")

def execute_command(command):
    if "axel" in command:
        speak("Hi, How can I help you?")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")
    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "tell me a joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)
    elif "search for" in command:
        query = command.replace("search for", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query} on Google")
    elif "play spotify music" in command:
        playlist_url = "https://open.spotify.com/playlist/78rB9Yy1ZfRxOWThORb7lk?autoplay=true"
        webbrowser.open(playlist_url)
        speak("Playing Spotify playlist")
    elif "close browser" in command or "close google" in command:
        os.system("taskkill /im chrome.exe /f")
        speak("Closing browser")
    elif "weather in" in command:
        city = command.replace("weather in", "").strip()
        get_weather(city)
    elif "news" in command:
        webbrowser.open("https://news.google.com")
        speak("Opening Google News")
    elif "calculate" in command:
        try:
            expression = command.replace("calculate", "").strip()
            result = eval(expression)
            speak(f"The result is {result}")
        except Exception:
            speak("Sorry, I couldn't calculate that.")
    elif "play music" in command:
        music_dir = "C:\\Users\\Public\\Music"  # Update with your music folder path
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, random.choice(songs)))
            speak("Playing music")
        else:
            speak("No music files found.")
    elif "shutdown" in command:
        speak("Shutting down the computer.")
        os.system("shutdown /s /t 5")
    elif "restart" in command:
        speak("Restarting the computer.")
        os.system("shutdown /r /t 5")
    elif "open calculator" in command:
        subprocess.Popen("calc.exe")
        speak("Opening Calculator")
    elif "exit" in command or "stop" in command:
        speak("Goodbye, have a great day!")
        exit()
    else:
        speak("Sorry, I can't do that yet.")

if __name__ == "__main__":
    speak("Hello, I am Axel. How can I help you?")
    while True:
        user_command = listen()
        if user_command:
            execute_command(user_command)
