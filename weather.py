import pyttsx3,requests
import speech_recognition as sr
from datetime import datetime
def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source: #microphone k source hishebe use korbe,
        print("Listening...")
        r.pause_threshold = 1 #(amar kothar kono part jeno shuna bad na jay
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
def weather():
    speak("Enter the city: ")
    location = takeCommand().lower()
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=f32988a66a96c50bc58af095fdac7df5"
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    #create variables to store and display data
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']

    speak ("Current temperature is: {:.2f} degree Celsius".format(temp_city))
    speak ("weather description  :"+weather_desc)
    speak  ("Humidity      :"+str(hmdt)+ '%')
    speak  ("wind speed    :"+str(wind_spd) +'kilometers per hour')
