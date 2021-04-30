import speech_recognition as sr 
import time 
from time import ctime 
import webbrowser

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try: 
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            print('Lo siento, no te entedi :(')
        except sr.RequestError:
            print('Lo siento, error de conexión')
        return voice_data

def respond(voice_data):
    if 'nombre' in voice_data:
        print('Mi nombre es Alexis :3')
    if 'hora'in voice_data:
        print(ctime())
    if 'buscar' in voice_data:
        buscar = record_audio('¿Que quieres buscar uwu?')
        url = 'https://google.com/search?q=' + buscar
        webbrowser.get().open(url)
        print('Esto es lo que encontre para ti owo: ' + buscar)
    if 'place' in voice_data:
        buscar = record_audio('Que lugar')
        url = 'https://google.nl/maps/place/' + lugar + '/&amp;'
        webbrowser.get().open(url)
        print('Esto es lo que encontre para ti owo: ' + lugar)

time.sleep(1)
print('¿Como te puedo ayudar ewe?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
