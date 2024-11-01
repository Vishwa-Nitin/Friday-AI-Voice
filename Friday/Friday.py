import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import PySimpleGUI as sg

sg.theme('Dark Teal')
image1 = 'mic.png'
image2 = 'micmute.png'
layout = [[sg.Text("Friday")],[sg.ReadFormButton('Activate', button_color=sg.TRANSPARENT_BUTTON,
                                image_filename=image1, image_size=(50,50), image_subsample=2, border_width=0),
                                sg.Text(' ' * 2),sg.ReadFormButton('Exit', button_color=sg.TRANSPARENT_BUTTON,
                                image_filename=image2, image_size=(50,50), image_subsample=2, border_width=0,auto_size_button=True),
                                sg.Text(' ' * 2)]]

window = sg.Window('Friday',layout = layout,resizable=True,size=(225,100))

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Friday Sir. tell me how may i help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
while True:
    events,values = window.read()
    if events == sg.WIN_CLOSED or events == 'Exit':
        window.close()
        break
    elif events == "Activate":
         
        if __name__ == "__main__":
            wishMe()
            while True:
                # if 1:
                query = takeCommand().lower()

                # Logic for executing tasks based on query
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)


                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")
                    
                elif 'open gmail' in query:
                    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
                    
                elif 'open instagram' in query:
                    webbrowser.open("https://www.instagram.com/")

                elif 'play hindi song' in query:
                    webbrowser.open("https://www.youtube.com/watch?v=VOLKJJvfAbg")

                elif 'open google' in query:
                    webbrowser.open("google.com")

                elif 'open stackoverflow' in query:
                    webbrowser.open("stackoverflow.com")
   
                elif 'play music' in query:
                    music_dir = 'D:\\music\\English Mp3 Songs'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[1]))

                elif 'what is the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")

                elif 'open code' in query:
                    codePath = " "
                    os.startfile(codePath)
                


