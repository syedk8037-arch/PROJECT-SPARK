from core.listener import listen_wake, listen_command
from core.speaker import speak
from brain.mode_intent import detect_mode
from brain.os_intent import detect_os_action
from brain.os_actions import execute_os_action

CURRENT_MODE = None  # "arduino" or "os"

speak("SPARK is online. Say spark to wake me up.")

while True:
    # -------- WAKE STATE --------
    wake_text = listen_wake()
    if not wake_text:
        continue

    print("Heard:", wake_text)

    if "spark" not in wake_text:
        continue

    # -------- COMMAND STATE --------
    speak("Yes Kabir. What can I do for you?")
    command = listen_command()

    if not command:
        continue

    command = command.lower()
    print("Command:", command)

    # -------- EXIT MODE (FAST PATH) --------
    if any(x in command for x in ["exit mode", "leave mode", "go back", "stop mode", "exit this mode"]):
        if CURRENT_MODE is not None:
            speak(f"Exiting {CURRENT_MODE} mode.")
            CURRENT_MODE = None
        else:
            speak("No mode is currently active.")
        continue

    # -------- MODE DETECTION --------
    mode = detect_mode(command)

    if mode == "arduino":
        CURRENT_MODE = "arduino"
        speak("Yes Kabir, Arduino mode activated.")
        print("MODE =", CURRENT_MODE)
        continue

    elif mode == "os":
        CURRENT_MODE = "os"
        speak("Yes Kabir, OS mode activated.")
        print("MODE =", CURRENT_MODE)
        continue

    # -------- OS MODE ACTIONS --------
    if CURRENT_MODE == "os":
        os_action = detect_os_action(command)

        if os_action.get("action") == "none":
            speak("OS mode is active. Please give an OS command or say exit mode.")
            continue

        result = execute_os_action(os_action)

        if result:
            speak(f"Yes Kabir, {result}")
        else:
            speak("I couldn't perform that action.")

        continue

    # -------- ARDUINO MODE (PLACEHOLDER) --------
    if CURRENT_MODE == "arduino":
        speak("Arduino mode is active. Please give an Arduino command or say exit mode.")
        continue

    # -------- NO MODE SELECTED --------
    speak("Please select a mode. Arduino or OS.")
