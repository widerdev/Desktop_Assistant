import pyttsx3      # text to speech
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser


# Taking Voice from my system 
engine = pyttsx3.init('sapi5')  # if u want to access any kind of voice property in ur sysytem add parameter 'sapi5'
voices = engine.getProperty('voices')
# print(voices[0].id)
# print(type(voices))

engine.setProperty('voice', voices[0].id)   # Tell python interpretor to pick up male voice
engine.setProperty('rate', 150)   # Speech rate of jarvis


# Spek Function
def speak(text):
    """ This function takes text and return voices
    Args:
        text (_type_): -description_
    """
    engine.say(text)
    engine.runAndWait()  # To Close this speak property


# Speech recognition Function
def takecommand():
    """This function will recognize voice and returns text
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:   # to access ur microphone
        print("Listening....")
        r.pause_threshold = 1  # To recognize perfectly (pause for 1ms while listening)
        audio = r.listen(source)  # To listen 

        # hit the google API
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print("Say that again please!")
            return "None"
        return query

# This function is to wish me by using time
def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning Dev sir, How are you doing")
    elif hour>=12 and hour<18:
        speak("good afternoon Dev sir, How are you doing")
    else:
        speak("good evening Dev sir, How are you doing")

    speak("I am JARVIS. Tell me sir how can i help you?")



if __name__ == "__main__":    # (if u write it then the python interpreter will start reading code from here and then go forward)
    
    wish_me()

    while True:
        query = takecommand().lower()
    
        if "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif "youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")

        elif "google" in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif "github" in query:
            speak("Opening GitHub")
            webbrowser.open("github.com")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif "bye" in query:
            speak("goodbye sir")
            exit()