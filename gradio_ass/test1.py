import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

while True:
    input_usr = input("Enter your input: ")
    if input_usr.lower() == "quit":
        break
    speak(input_usr)