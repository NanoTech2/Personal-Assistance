import pyttsx3 # pip install
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os



engine  = pyttsx3.init('sapi5')               # https://www.geeksforgeeks.org/python-text-to-speech-by-using-pyttsx3/#:~:text=init()%20factory%20function%20to,by%20%E2%80%9Csapi5%E2%80%9D%20for%20windows.
voices = engine.getProperty('voices')         # https://pyttsx.readthedocs.io/en/v1.0/engine.html
# print(voices)

engine.setProperty('voice', voices[1].id)
# print(voices[0].id) david and zeera voice choose beween 0 and 1 

def speak(audio):
    engine.say(audio)   #audio string speak  called by engine
    engine.runAndWait() 

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12: 
        speak("good morning ryzen wake up and brush")
    elif hour == 12:
        speak("good noon. ryzen")
    elif hour > 12 and hour <=18:
        speak("good evening ryzen")
    else:
        speak("good evening ryzen")

    speak("how are you. i m tyler . please tell me how may i help you")

def takecommand():  #it takes microphone input from use and return stirng outputs
    r = sr.Recognizer() # class recog from speechrecog help to recog audio
    with sr.Microphone() as source: # microphone as source
        print("listening.... ")
        r.adjust_for_ambient_noise(source,duration=1)
       # first word complete if get break for sec word then mic is wait for 1 sec to get second word
        audio = r.listen(source)  # listen form sppechreog listen from source  = microphone as source
        
    try:
        print("recognizing.... ") 
        query = r.recognize_google(audio, language = 'en-in')
        print(f"ryzen said: { query }\n")
    
    except Exception as e:
        #print(e)
        print("say it again ryzen i cant here you")
        return "none"
    return query


 

if __name__=="__main__":
    wishme() # wish funtion called
    #speak("hi ryzennn")   # only for test speak function called with paramet audio as stirg 
    while True:
        query  = takecommand().lower()#get voice save in query in lower case

        if 'wikipedia' in query:
            speak(f"searching{query} in google..")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(result)
            speak(result)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open_new_tab("google.com")

        elif 'play music' in query:
            try:
                print("playing sound")
                from playsound import playsound
                playsound('C:\songs-akhil\\hope lofi.mp3')
                print("done!")
            except Exception as e:
                print("i cant recognize please can u say it again.")
        
        elif ' time 'in query:
            strTime = (datetime.datetime.now().strftime("%H:%M:%S"))
            speak(f"the time is {strTime}")
        
        elif 'hello' in query:
            speak("hi ryzen. how may i help you")

        elif 'tell me' in query:
            speak(" hey. my name is tyler . i m personal assistant of ryzen. whats your name? ")

        elif 'bye'or'buy'or'bie'or'by' in query:
            speak("bye ryzen")
            exit()

        elif 'my name is 'in query:
            speak("good. i got new friend") 
        
        else:
            speak("i cant understand. can u repeat it again")

            


        
            






