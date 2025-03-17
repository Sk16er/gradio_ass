from gradio_client import Client
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

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
            speak("Goodbye!")
            break
        
        # responce and the mesage 
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
        speak(result)

if __name__ == "__main__":
    main()    
