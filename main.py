import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init()
voices = engine.getProperty('voices')
voices = engine.setProperty('voice', voices[0].id)
speed = engine.getProperty('rate')
engine.setProperty('rate', speed+(-50))


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 4 <= hour <= 12:
        speak('Hello sir, good morning...')
    elif 12 < hour <= 18:
        speak('Hello sir, good afternoon...')
    else:
        speak('Hello sir, good evening...')
        speak('I am Jarvis. Please tell me how can I help you...')


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listing....')
        r.pause_threshold = 1
        audio = r.listen(source)
        # audio = r.listen(source, timeout=1, phrase_time_limit=10)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}')
    except Exception as e:
        print('Say that again please')
        return 'None'

    return query


def send_email(to_email, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sadcat14@gmail.com', 'Fotikchand#6112')
    server.sendmail('sadcat14@gmail.com', to_email, content)
    server.close()


if __name__ == '__main__':
    wish_me()
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=1)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = "F:\\GUNS"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open chrome' in query:
            chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome_path)

        elif 'send email' in query:
            try:
                speak("What should I say ?")
                content = take_command()
                to_email = 'polsbca@gmail.com'
                send_email(to_email, content)
                speak("Email has been sent successfully")
            except Exception as e:
                print(e)
                speak("Sorry email not sent")

        elif 'quit' in query:
            speak("Quiting sir...")
            exit()
