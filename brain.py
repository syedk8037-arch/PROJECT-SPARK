from core.speaker import speak

def process(command):
    if "time" in command:
        from datetime import datetime
        speak(f"The time is {datetime.now().strftime('%I:%M %p')}")
    
    elif "hello" in command:
        speak("Hello Kabir. How can I help you?")

    else:
        speak("Sorry, I did not understand that.")
