import wikipediaapi
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to greet the user
def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Jarvis, how may I help you")

# Function to capture user's voice command
def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing.....")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please say again.")
        return "None"

    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "None"

    return query.lower()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            wiki_wiki = wikipediaapi.Wikipedia('en')
            
            try:
                page_py = wiki_wiki.page(query)
                results = page_py.text[:500]  # Limiting the output to 500 characters
                speak("According to Wikipedia")
                print(results)
                speak(results)

            except wikipediaapi.exceptions.DisambiguationError as e:
                print(f"Ambiguous term. Please be more specific: {e.options}")

            except wikipediaapi.exceptions.HTTPTimeoutError:
                print("Error: Wikipedia API request timed out. Please try again later.")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")

        elif 'play music' in query:
            music_dir = "E:\swatisweb\music"  # Update with your music directory
            if os.path.exists(music_dir):
                os.startfile(music_dir)
            else:
                print("Music directory not found.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\satyam singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  # Update with your VS Code path
            if os.path.exists(codePath):
                os.startfile(codePath)
            else:
                print("VS Code path not found.")
