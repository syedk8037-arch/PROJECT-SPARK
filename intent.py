def detect_intent(command):
    command = command.lower()

    # Arduino keywords
    arduino_keywords = [
        "light", "led", "rgb", "relay", "socket",
        "arduino", "turn on", "turn off", "blink"
    ]

    # OS keywords
    system_keywords = [
        "open", "close", "start", "shutdown",
        "restart", "volume", "brightness",
        "wifi", "bluetooth"
    ]

    for word in arduino_keywords:
        if word in command:
            return "arduino"

    for word in system_keywords:
        if word in command:
            return "system"

    return "knowledge"
