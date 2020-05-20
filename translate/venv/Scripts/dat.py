import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

print('search youtube: ')
print('speak now ')

r1 = sr.Recognizer()
url = 'https://www.google.com/search?q='
with sr.Microphone() as source:
    print('Search your query')
    audio = r1.listen(source)

    try:
        get = r1.recognize_google(audio)
        print(get)
        wb.get().open_new(url+get)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError as e:
        print('failed'.format(e))
