#pip install pyttsx3
#pip install wikipedia
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

#for accepting voice input (windows provide an API for use of inbuilt voice )
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices) #Their are 2 inbuilt voices 0 =David and 1=zira 
#for setting engine voice 
engine.setProperty('voice', voices[1].id)#zira


def speak(audio):
    #This msg will be speaked by assistant
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    #till 12 --> Morning
    if hour>=0 and hour<12:
        speak("Good Morning")
    #after 12 till 6 --> afternoon
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    #after 6 --> Evening
    else:
        speak("Good Evening")   

    speak("I am your assistant Hemlata  ! Please tell me how may I help you?")

def takeCommand():
    
    #It takes input from user and returns strring output to user
    r = sr.Recognizer()
    #input will be given using microphone
    with sr.Microphone() as source:
        print("Listening...")
        #for waiting it user takes an pause
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        #For hearing the voice
        print("Recognizing.....")
        #set the query including parameter of language
        query = r.recognize_google(audio, language='en-in')#Using google for voice recognition.
        print(f"User said: {query}\n")

    except Exception as e:
        #If voice is not proper
        print("Say that again please...")#Say that again will be printed in case of improper voice
        return "None"#None string will be returned
    return query

if __name__ == "__main__": 
    #wishme() function will reflect the wish according to hour
    wishMe()
    while True:
        query = takeCommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            #If voice input is wikipedia it will direct to wikipedia
            query = query.replace("wikipedia", "")
            #the results will be fetched from wikipedia
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            #the results will be displayed
            print(results)
            #the results as an voice
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")        
            
        