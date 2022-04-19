import nltk
import pyttsx3
import random
from nltk.corpus import wordnet   #Import wordnet from the NLTK
syn = list()
ant = list()

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 175)
    engine.say(audio)
    engine.runAndWait()

def dictionary(w):
    meanng = wordnet.synsets(w)
    for synset in wordnet.synsets(w):
       for l in synset.lemmas():
           if w not in l.name():
            syn.append(l.name())    #add the synonyms
           if l.antonyms():    #When antonyms are available, add them into the list
            ant.append(l.antonyms()[0].name())
    s=random.choice(syn)
    a=random.choice(ant)

    if '_' in a:
        a=a.replace("_"," ")
    if '_' in s:
        s = s.replace("_", " ")
    print('The meaning of the word : ' + meanng[0].definition())
    speak('The meaning of'+w + meanng[0].definition())
    speak('Synonyms ' + str(s))
    print('Synonyms: ' + str(syn))
    print('Antonyms: ' + str(ant))
    speak('Antonyms ' + str(a))
