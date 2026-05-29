import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_mistral(prompt):
    payload = {
        "model": "mistral",
        "prompt": (
            "You are SPARK, a fast and smart AI assistant. "
            "Reply in short, clear sentences. "
            "Do not over-explain unless asked.\n\n"
            f"User: {prompt}\nAssistant:"
        ),
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=120)
        return response.json().get("response", "").strip()
    except:
        return "I am having trouble thinking right now."
