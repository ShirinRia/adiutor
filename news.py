import bs4
import pyttsx3
import requests


def news():
    main_url='https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey='
    main_page=requests.get(main_url).json()
    articles = main_page["articles"]
    head=[]
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        print(f"today's {day[i]} news is {head[i]}")
        speak(f"today's top {day[i]} news is {head[i]}")
def corona(country):
    countries=str(country).replace(" ","")
    url=f"https://www.worldometers.info/coronavirus/country/{countries}/"
    result=requests.get(url)
    soups=bs4.BeautifulSoup(result.text,'lxml')
    corona=soups.find_all('div',class_='maincounter-number')
    data=[]
    for case in corona:
        span=case.find('span')
        data.append(span.string)
    cases,death,recovered=data
    speak(f"Total cases: {cases}")
    speak(f"Total death: {death}")
    speak(f"Total recovered: {recovered}")

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 175)
    engine.say(audio)
    engine.runAndWait()