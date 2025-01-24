import warnings
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import datetime
import calendar
import random
import wikipedia
import webbrowser
import winshell
import subprocess
import pyjokes 
import requests
import json
import wolframalpha
import time


warnings.filterwarnings('ignore')

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()


def rec_audio():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        audio = recog.listen(source)

    data = " "
    
    try:
        data = recog.recogize_google(audio)
        print("You said:" + data)
    except sr.UnknownValueError:
        print("Assistant could not understand the audio")
    except sr.RequestError as ex:
        print("Request Error from Google Speech Recognition" + ex)

    return data

# rec_audio()

def response(text):
    print(text)

    tts = gTTS(text=text,lang='en')

    audio = "Audio.mp3"
    tts.save(audio)

    playsound.playsound(audio)

    os.remove(audio)


def call(text):
    action_call = "assistant"
    text = text.lower()

    if action_call in text:
        return True
    
    return False


def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = ['January','Febuary','March','April','May','June',
              'July','August','September','October','November','December'
    ]
    
    ordinals = ["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th","13th","14th",
                "15th","16th","17th","18th","19th","20th","21st","22nd","23rd","24th","25th","26th","27th","28th",
                "29th","30th","31th",
    ]

    return f'Today is {week_now},{months[month_now -1]} the {ordinals[day_now -1]}.'


def say_hello(text):
    greet = ['hi', 'hola', 'greetings', 'massup', 'hello', 'howdy', 'hey there']

    response = ['hi', 'hola', 'greetings', 'massup', 'hello', 'howdy', 'hey there']

    for word in text.split():
        if word.lower() in greet:
            return random.choice(response) + '.'
    return ""


def wiki_person(text):
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == 'who' and list_wiki[i+1].lower() == 'is':
           return list_wiki[i+2] + " " + list_wiki[i+3]


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":","-")+"-note.txt"
    with open(file_name,"w")  as f:
        f.write(text)
    
    subprocess.Popen(["notepad.exe", file_name])


while True:

    try:
        text = rec_audio()
        speak = " "

        if call(text):
            speak = speak + say_hello(text)

            if 'date' in text or 'day' in text or 'month' in text:
                get_today = today_date()
                speak = speak + " " + get_today

            elif 'time' in text:
                now = datetime.datetime.now()
                meridien = ""
                if now.hour >= 12:
                    meridien = 'p.m'
                    hour = now.hour - 12
                else:
                    meridien = 'a.m'
                    hour = now.hour

                if now.minute < 10:
                    minute = '8' + str(now.minute)
                else:
                    minute = str(now.minute)
                speak = speak + " " + 'It is' + str(hour) + ":" + minute + " " + meridien + "."

            elif 'wikipedia' in text or 'wikipedia' in text:
                if 'who is' in text:
                    person = wiki_person(text)
                    wiki = wikipedia.summary(person, sentences = 2)
                    speak = speak + " " + wiki

            elif "who are you" in text or "define yourself" in text:
                speak = speak + """ Hello, I am an Assistant. Your Assistant.I am here to make your life easier. You can 
                command me to perform various tasks such as solving mathematical questions or opening applications
                etc."""

            elif "your name" in text:
                speak = speak + 'my name is assistant'

            elif "who am i" in text:
                speak = speak + 'you must probably be a human'

            elif "why do you exist" in text or "why did you come" in text:
                speak = speak + "It is a secret"

            elif "how are you" in text:
                speak = speak + "I am fine, thank you"
                speak = speak + "\nHow are you"

            elif "fine " in text or "good" in text:
                speak = speak + "It's good to know that you are fine"

            elif "open" in text.lower():
                if "chrome" in text.lower():
                    speak = speak + "Opening Google Chrome"
                    os.startfile(
                        r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                    )
                
                elif "office" in text.lower():
                    speak = speak + "Opening Microsoft Office"
                    os.startfile(
                        r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office.exe"
                    )

                elif "vs code" in text.lower():
                    speak = speak + "Opening Visual Studio Code"
                    os.startfile(
                        r"C:\Users\Shree\AppData\Local\Programs\Microsoft VS Code\Code.exe" 
                    )

                elif "youtube" in text.lower():
                    speak = speak + "Opening Youtube"
                    webbrowser.open("https://youtube.com")

                elif "google" in text.lower():
                    speak = speak + "Opening Google"
                    webbrowser.open("https://google.com")
                
                else:
                    speak = speak + "Application not available"

            elif "youtube" in text.lower():
                ind = text.lower().split().index("youtube")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.youtube.com/results?search_query=" + 
                    "+".join(search)
                )
                speak = speak +"Opening" + str(search) + "on youtube"

            elif "search" in text.lower():
                ind = text.lower().split().index("search")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q=" + "+".join(search)
                )
                speak = speak +"Searching" + str(search) + "on google"

            elif "google" in text.lower():
                ind = text.lower().split().index("google")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q=" + "+".join(search)
                )
                speak = speak +"Searching" + str(search) + "on google" 

            elif "empty recycle bin" in text:
                winshell.recycle_bin().empty(
                    confirm=True, show_progress=False, sound = True
                )
                speak = speak + "recycle bin emptied"

            elif "note" in text or "remember this" in text:
                talk("what would you like to write down?")
                note_text = rec_audio()
                note(note_text)
                speak = speak + "I have made a note of that"

            elif "joke" in text or "jokes" in text:
                speak = speak + pyjokes.get_joke()

            elif "where is" in text:
                ind = text.lower().split().index("is")
                location = text.split()[ind + 1:]
                url = "https://www.google.com/maps/place/" + "".join(location)
                speak = speak + "This is where" + str(location) + "is."
                webbrowser.open(url)  
            
            elif "weather" in text:
                key = "912f8207a5277cdba93b0ee5416b91f7"
                weather_url = "https://api.openweathermap.org/data/2.5/weather?"
                ind = text.split().index("in")
                location = text.split()[ind + 1:]
                location = "".join(location)
                url = weather_url + "appid=" + key + "&q=" + location
                js = requests.get(url).json()
                if js["cod"] != "484":
                    weather =js["main"]
                    temperature = weather["temp"]
                    temperature = temperature - 273.15
                    humidity = weather["humidity"]
                    desc = js["weather"][0]["description"]
                    weather_response = "The temperature in celcius is" + str(temperature) + "The humidity is"
                    + str(humidity) + "and weather description is " + str(desc)
                    speak = speak + weather_response
                else:
                    speak = speak + "city not found"

            elif "news" in text:
                url = ('https://newsapi.org/v2/top-headlines?'
                       'country=in&'
                       'apiKey=07c11f352cce45a895f6c14868e2822c')
                try:
                    response = requests.get(url)
                except:
                    talk("Please check your connection")
                
                news = json.loads(response.text)
                for new in news["articles"]:
                    print(str(new["title"]),"\n")
                    talk(str(new["title"]))
                    engine.runAndWait()

                    print(str(new["description"]),"\n")
                    talk(str(new["description"]))
                    engine.runAndWait()

     
            elif 'calculate' in text:
                app_id = 'VHA4HR-66QA47T9KQ'
                client = wolframalpha.Client(app_id)
                ind = text.lower().split().index('calculate')
                text = text.split()[ind + 1:]
                res = client.query(''.join(text))
                answer = next(res.results).text
                speak = speak + 'The answer is' + answer

            elif 'what is' in text or 'who is' in text:
                app_id = 'VHA4HR-66QA47T9KQ'
                client = wolframalpha.Client(app_id)
                ind = text.lower().split().index('is')
                text = text.split()[ind + 1:]
                res = client.query(''.join(text))
                answer = next(res.results).text
                speak = speak + 'The answer is' + answer

            elif "don't listen" in text or 'stop listening' in text or 'do not listen' in text:
                talk('for how many seconds do you want to sleep')
                a = int(rec_audio())
                time.sleep(a)
                speak = speak + str(a) + 'seconds completed. Now you can ask me anything'

            elif 'exit' in text or 'quit' in text:
                exit()
            
            response(speak) 
         
    except:
        talk("I don't know that")