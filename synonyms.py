SYNONYMS = {
    # Vehicles
    "car": ["automobile", "vehicle", "auto", "sedan", "hatchback", "suv"],
    "bike": ["bicycle", "cycle"],
    "motorcycle": ["bike", "motorbike"],

    # Artificial Intelligence
    "ai": [
        "artificial intelligence",
        "machine intelligence",
        "artificial brain"
    ],

    # Machine Learning
    "ml": [
        "machine learning",
        "statistical learning"
    ],

    # Deep Learning
    "dl": [
        "deep learning",
        "neural networks",
        "neural network"
    ],

    # Hardware
    "cpu": [
        "processor",
        "central processing unit"
    ],
    "gpu": [
        "graphics card",
        "graphics processor",
        "video card",
        "nvidia",
        "amd gpu"
    ],
    "ram": [
        "memory",
        "random access memory"
    ],
    "storage": [
        "hard disk",
        "hard drive",
        "ssd",
        "hdd"
    ],

    # Phones & devices
    "phone": [
        "mobile",
        "smartphone",
        "cell phone"
    ],
    "laptop": [
        "notebook",
        "computer",
        "pc"
    ],
    "desktop": [
        "computer",
        "pc"
    ],

    # Software
    "os": [
        "operating system"
    ],
    "windows": [
        "microsoft windows"
    ],
    "linux": [
        "ubuntu",
        "debian",
        "fedora"
    ],

    # Internet & networking
    "internet": [
        "net",
        "online",
        "web"
    ],
    "wifi": [
        "wireless",
        "wireless internet"
    ],
    "bluetooth": [
        "bt"
    ],

    # Programming
    "python": [
        "python language"
    ],
    "java": [
        "java language"
    ],
    "javascript": [
        "js"
    ],
    "code": [
        "program",
        "programming",
        "coding"
    ],

    # Electronics
    "arduino": [
        "microcontroller",
        "embedded board"
    ],
    "sensor": [
        "detector",
        "input sensor"
    ],
    "relay": [
        "switch"
    ],

    # General concepts
    "temperature": [
        "heat"
    ],
    "speed": [
        "velocity"
    ],
    "power": [
        "energy"]
}

def apply_synonyms(words):
    normalized = []

    for word in words:
        replaced = False
        for key, values in SYNONYMS.items():
            if word == key or word in values:
                normalized.append(key)
                replaced = True
                break

        if not replaced:
            normalized.append(word)

    return normalized
