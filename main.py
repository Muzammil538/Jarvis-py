import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import PyAudio
import smtplib


print("Initializing Root...")

MASTER = "Almaaz"

engine=pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    #print(hour)

    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER)
    elif hour>=12 and hour <18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Night" + MASTER)
    speak("I am Root , How may I Help you" + MASTER)

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Can you repeat it please")
        speak("Can you repeat it please")

speak("Initializing Root...")
wishMe()
takeCommand()