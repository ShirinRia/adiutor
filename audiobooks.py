import PyPDF2 as pdf
import pyttsx3 #pip install pyttsx3

def back():
    from functions import begin_2
    begin_2()
def audiobk(bk,spage):
    global engine
    engine = pyttsx3.init()
    try:
        getbk=bk
        book=open(getbk,"rb")
        pdfreader=pdf.PdfFileReader(book)
        pages=pdfreader.numPages

        start_page=int(spage)
        for i in range(start_page,pages+1):
            pageget=pdfreader.getPage(i)
            text=pageget.extractText()
            engine.say(text)
            engine.runAndWait()

    except KeyboardInterrupt:
        engine.stop()
        back()
