import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "3a6e780e6b3d47158d5f75b39f3e8473"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open insta" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles',[])
            for article in articles:
                speak(article['title'])
    
    
    
    
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
               
        r = sr.Recognizer()
        
        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=1)
          
            word = r.recognize_google(audio)
            print(word)
            
            if(word.lower() == "jarvis"):
                speak("Hello Sir")
                
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(command)
                    
                    processCommand(command)
                    
            elif(word.lower() == "hey jarvis"):
                speak("Hello Sir, how may I help you")
                
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(command)
                    
                    processCommand(command)
                
        except Exception as e:
            print("Error; {0}".format(e))
