import speech_recognition as sr
import core.speaker as speaker

recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = True
recognizer.energy_threshold = 300

microphone = sr.Microphone()

def listen_wake():
    """Short listening only for wake word"""
    if speaker.is_speaking():
        return ""

    with microphone as source:
        try:
            recognizer.adjust_for_ambient_noise(source, duration=0.4)
            audio = recognizer.listen(
                source,
                timeout=3,
                phrase_time_limit=2
            )
            text = recognizer.recognize_google(audio)
            return text.lower()
        except:
            return ""

def listen_command():
    """Long listening for actual command"""
    if speaker.is_speaking():
        return ""

    with microphone as source:
        try:
            recognizer.adjust_for_ambient_noise(source, duration=0.6)
            audio = recognizer.listen(
                source,
                timeout=6,
                phrase_time_limit=8
            )
            text = recognizer.recognize_google(audio)
            return text.lower()
        except:
            return ""
