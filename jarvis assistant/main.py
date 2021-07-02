import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
jarvis=pyttsx3.init()
voices = jarvis.getProperty('voices')
jarvis.setProperty('voice',voices[0].id)

def talk(text):
    jarvis.say(text)
    jarvis.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'jarvis' in command:
                command = command.replace('jarvis','')
    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)
    elif 'play' in command:
        song = command.replace('play','')
        talk('yes boss')
        print('I am playing' + song)
        talk('I am playing' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for,2)
        talk('yes boss')
        print(info)
        talk(info)
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    elif 'your name' in command:
        talk('My name is Jarvis')
        print('My name is Jarvis')
    elif 'you' in command:
        talk('My name is Jarvis.Maruf islam have created me.He is my boss.I am a global assistant robot')
        print('My name is Jarvis.Maruf islam have created me.He is my boss.I am a global assistant robot')
    elif 'what is' in command:
        talk('yes boss')
        found = command.replace('what is','')
        pywhatkit.search(found)
    elif 'go to' in command:
        talk('yes boss')
        search = command.replace('go to',' ')
        pywhatkit.search(search)
    else:
        talk('sorry boss,i can not understand but i am going to search it for you')
        pywhatkit.search(command)

while True:
    run_jarvis()