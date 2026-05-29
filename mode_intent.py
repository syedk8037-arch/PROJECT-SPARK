import json
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def detect_mode(command: str):
    text = command.lower()

    # -------- FAST KEYWORD DETECTION (VERY IMPORTANT) --------
    if "arduino" in text:
        return "arduino"

    if "os" in text or "operating" in text:
        return "os"

    # -------- AI FALLBACK (ONLY IF NEEDED) --------
    prompt = f"""
You are an AI assistant.

Detect if the user wants to switch modes.

Modes:
- arduino
- os

Rules:
- Reply ONLY in JSON
- If unsure, return "none"

Examples:
Input: "arduino mode"
Output: {{ "mode": "arduino" }}

Input: "os mode"
Output: {{ "mode": "os" }}

Input: "hello"
Output: {{ "mode": "none" }}

User command: "{command}"
"""

    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }

    try:
        res = requests.post(OLLAMA_URL, json=payload, timeout=30)
        data = json.loads(res.json().get("response", "{}"))
        return data.get("mode", "none")
    except:
        return "none"
