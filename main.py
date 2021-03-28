import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 90)

text = input("What do you want to say: ")
engine.say(text)
engine.runAndWait()