import pyttsx3


def text_to_speech(text):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    for i, voice in enumerate(voices):
        print(i, voice.name)
 
    engine.setProperty('voice', voices[1].id)

    print("Selected Voice:", engine.getProperty('voice'))

    engine.say(text)
    engine.runAndWait()

#print(text_to_speech("hello srinithi"))


