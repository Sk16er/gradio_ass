from gradio_client import Client
from gtts import gTTS
import os

def speak(text, lang='en'):
    # Create the Audio folder if it doesn't exist
    if not os.path.exists("Audio"):
        os.makedirs("Audio")
    
    # Generate a unique filename
    i = 0
    while True:
        filename = f"Audio/temp{i}.mp3"
        if not os.path.exists(filename):
            break
        i += 1
    
    # Save and play the audio file
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    os.system(f"start {filename}")

def main():
    client = Client("sk16er/nothing")
    
    # Ask user if they want to specify bot personality
    bot_act_ind = input("Do you want to specify how the bot should act? (y/n): ").lower()
    
    bot_act = "a friendly and helpful assistant"
    
    if bot_act_ind == 'y':
        bot_act = input("How should I act: ")
    
    while True:
        # que
        input_user = input("Write question (or 'quit' to exit): ")
        
        # quit option
        if input_user.lower() == 'quit':
            speak("Goodbye!", lang='en')
            break
        
        # response and the message 
        result = client.predict(
                message=input_user,
                system_message=f"You are a helpful assistant made by shushank kumar your name is byttsx3 and you have to act like {bot_act}",
                max_tokens=512,
                temperature=0.7,
                top_p=0.95,
                api_name="/chat"
        )
        
        # speak
        print("AI Response:", result)
        speak(result, lang='hi')  # Change 'hi' to 'en' for Hinglish

if __name__ == "__main__":
    main()