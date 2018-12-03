import speech_recognition as sr
import os

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
            os.system('python3 logo.py')
        elif "calendar" in text:
            os.system('python3 cal.py')
        elif "clean" in text:
            os.system('python3 clean.py')
            os.system('python3 message.py Done!')
        else:
            continue
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
