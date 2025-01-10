import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

# converting voices male to female

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# starting speech

def talk(text):
    # engine.say('I am your Alexa')
    # engine.say('What can I do for you ? ')
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
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
    command1 = take_command()
    print(command1)

    if 'play' in command1:
        song = command1.replace('play', '')
        talk('playning' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command1:

        # time = datetime.datetime.now().strftime('%H:%M:%S')
        time = datetime.datetime.now().strftime('%I:%M %p')

        print(time)
        talk('Current time is ' + time)

    elif 'search' in command1:
        person = command1.replace('search', '')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)

    elif 'date' in command1:
        talk('sorry, I have a headache')
    elif 'are you single' in command1:
        talk('I am in a relationship with wifi')
    elif 'joke' in command1:
        joke = pyjokes.get_joke()
        talk(pyjokes.get_joke())
        print(joke)
    else:
        string = 'please say the command again...'
        talk(string)
        print(string)

while True:
    run_alexa()
