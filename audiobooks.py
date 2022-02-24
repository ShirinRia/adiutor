import PyPDF2 as pdf
import pyttsx3 #pip install pyttsx3

def printi():
    from voice import start_game
    start_game()
def audiobk():
    global engine
    engine = pyttsx3.init()
    try:
        getbk=input("path: ")
        book=open(getbk,"rb")
        pdfreader=pdf.PdfFileReader(book)
        pages=pdfreader.numPages
        print(pages)

        engine.say("From which page should I start reading?")
        engine.runAndWait()
        start_page=int(input("enter:  "))
        for i in range(start_page,pages+1):

            pageget=pdfreader.getPage(i)
            text=pageget.extractText()
            engine.say(text)
            engine.runAndWait()

    except KeyboardInterrupt:
        engine.stop()
        printi()
