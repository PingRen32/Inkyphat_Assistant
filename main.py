import speech_recognition as sr
import os
import message

r = sr.Recognizer()
os.system('python3 startup.py')

while True:
    with sr.Microphone() as source:
        print("Speech Recognition Running...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)
        if "logo" in text:
            import logo
        elif "calendar" in text:
            import cal
        elif "clean" in text:
            import clean
            message.printmessage('Done!')
        elif "weather" in text:
            import yahoo_weather
        else:
            continue
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
