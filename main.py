import pyttsx3
from pyttsx3 import engine
import speech_recognition as sr
import datetime as dt
import wikipedia as wp
import webbrowser as wb
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(dt.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("good Night")

    speak("I am Root sir")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Reconizing..")
        query = r.recognize_google(audio, language='en-Us')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say That again..")
        return "None"
    return query

def sendEmail(to,content):
    server  = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login#(Email,password )
    server.sendmail#(Email,to content)
    server.close()

#passwrd = #Keep any password thet will help to take command
if __name__ == "__main__" :
    wishMe()
    #while True:
    #pass_input = input("Enter Password : ")
    #if pass_input == passwrd:
    if 1:
            query = takeCommand().lower()
            #it searches on wikipiedia
            if 'wikipedia' in query:
                speak('Searching Wikipedia')
                query = query.replace("Wikipedia","")
                results = wp.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            #it opens youtube.com
            elif 'open youtube' in query:
                wb.open("https://www.youtube.com/")
            #it opens google.com
            elif 'open google' in query:
                wb.open("https://www.google.com/")
            #it opens facebook.com
            elif 'open facebook' in query:
                wb.open("https://www.facebook.com/")
            #it opens stackoverflow
            elif 'open stack overflow' in query:
                wb.open("https://www.stackoverflow.com")
            #it says the time
            elif 'the time' in query:
                strTime = dt.datetime.now().strftime("%H:%M:%S")
                print(strTime)
                speak(f"Sir , The time is {strTime}")
            #it opens Visual Studio Code
            elif 'open code' in query:
                codePath = "C:\\Users\\cc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            # elif 'email to root' in query:
            #     try:
            #         speak("What should i say?")
            #         content = takeCommand()
            #         #to = #whom you want to send Email 
            #         sendEmail(to,content)
            #         speak("Email has been sent!")

            #     except Exception as e:
            #         print(e)
            #         speak("Soory the Email was not sent")

            # elif 'email to jack' in query:
            #     try:
            #         speak("What should i say?")
            #         content = takeCommand()
            #         #to = #whom you want to send Email 
            #         sendEmail(to,content)
            #         speak("Email has been sent!")

            #     except Exception as e:
            #         print(e)
            #         speak("Soory the Email was not sent")

            
                
            elif 'make html' in query:
                sz_name = input("Enter File name : \n")
                try:
                    sz = open(sz_name,"w")
                    sz.write("<html>\n<head>\n<tittle>File</tittle>\n</head>\n<body>\n<h1>Hello World</h1>\n</body>\n</html>")
                    sz.close()
                    speak("file created")
                except Exception as e:
                    print(e)
                    speak("Sorry , can not make file")

            elif 'quit' in query:
                quit()


