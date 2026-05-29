import pyttsx3
import time
import re

_speaking = False

def is_speaking():
    return _speaking

def split_text(text, max_length=180):
    sentences = re.split(r'(?<=[.!?]) +', text)
    chunks = []
    current = ""

    for s in sentences:
        if len(current) + len(s) <= max_length:
            current += " " + s
        else:
            chunks.append(current.strip())
            current = s

    if current.strip():
        chunks.append(current.strip())

    return chunks

def speak(text):
    global _speaking

    if not text or not text.strip():
        return

    _speaking = True
    print("🔊 SPARK speaking...")

    engine = pyttsx3.init()
    engine.setProperty("rate", 145)
    engine.setProperty("volume", 1.0)

    chunks = split_text(text)

    for chunk in chunks:
        engine.say(chunk)
        engine.runAndWait()
        time.sleep(0.2)  # important delay

    engine.stop()

    # IMPORTANT: do not reopen mic immediately
    time.sleep(1.2)
    _speaking = False
