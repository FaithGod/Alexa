# speech recogonition is imported
#pyttsx3 text to speech converter
#pywhatkit yt access
#vpyjokes 1 line jokes

import speech_recognition as sr
import pyttsx3

audio = sr.Recognizer()
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()

# voice chage property
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('I am your alexa')

engine.say('what i can do for you')

# talking function nd text
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'give some information about mit adt ' in command:
        place = command.replace('give some information about mit adt', '')
        info = wikipedia.summary(place, 3)
        print(info)
        talk(info)


    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()