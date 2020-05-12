import webbrowser as wb
import speech_recognition as sr
import datetime

A = sr.Recognizer()
A1 = sr.Recognizer()

def VoiceRecognition(x):
    if 'YouTube' in x:
        A1 = sr.Recognizer()
        url="https://www.youtube.com/results?search_query="
        with sr.Microphone() as  source:
            print("speak video name you looking for:")
            audio2 = A1.listen(source)
            try:
                qurrie = A1.recognize_google(audio2)
                print(qurrie)
                wb.get().open_new(url+qurrie)

            except:
                print("Speak properly!!!!!")

    elif 'Wikipedia' in x:
        A1 = sr.Recognizer()
        url="https://en.wikipedia.org/wiki/"
        with sr.Microphone() as  source:
            print("speak your qurries:")
            audio2 = A1.listen(source)
            try:
                qurrie = A1.recognize_google(audio2)
                print(qurrie)
                wb.get().open_new(url+qurrie)

            except:
                print("Speak properly!!!!!")

    elif 'Python package' in x:
        A1 = sr.Recognizer()
        url="https://pypi.org/search/?q="
        with sr.Microphone() as  source:
            print("speak your module name:")
            audio2 = A1.listen(source)
            try:
                qurrie = A1.recognize_google(audio2)
                print(qurrie)
                wb.get().open_new(url+qurrie)

            except:
                print("Speak properly!!!!!")

    elif 'Google' in x:
        A1 = sr.Recognizer()
        url="https://www.google.com/search?q="
        with sr.Microphone() as  source:
            print("speak your qurries:")
            audio2 = A1.listen(source)
            try:
                qurrie = A1.recognize_google(audio2)
                print(qurrie)
                wb.get().open_new(url+qurrie)

            except:
                print("Speak properly!!!!!")

    else:
        A1 = sr.Recognizer()
        url = "https://www.google.com/search?q="
        try:
            wb.get().open_new(url+x)
        except:
            print("speak Correctly......")

try:
    with sr.Microphone() as source:
        print("speak searching plateform:")
        print("speak now:")
        print(datetime.datetime.now())
        audio = A.listen(source,timeout=2, phrase_time_limit=2)
        print(datetime.datetime.now())
        x = A.recognize_google(audio)
        print(x)
except (KeyboardInterrupt):
    print("Exiting...")
VoiceRecognition(x)