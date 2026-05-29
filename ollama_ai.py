import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "vicuna:7b"   # MUST MATCH `ollama list`

def ollama_reply(prompt):
    try:
        payload = {
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(OLLAMA_URL, json=payload, timeout=120)

        if response.status_code != 200:
            return "I am having trouble thinking right now."

        data = response.json()
        return data.get("response", "").strip() or "I am having trouble thinking right now."

    except Exception as e:
        print("OLLAMA ERROR:", e)
        return "I am having trouble thinking right now."
