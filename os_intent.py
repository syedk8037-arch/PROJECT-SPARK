import json
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def detect_os_action(command):
    prompt = f"""
You are an AI assistant.

Your task is to detect OS actions.
Allowed actions:
- open_chrome
- open_youtube
- youtube_search
- google_search
- open_app

Rules:
- Reply ONLY in JSON
- If action not found, return "none"
- Extract search query or app name if needed

Supported apps:
- notepad
- calculator
- file explorer
- vscode
- settings

Examples:
Input: "open notepad"
Output: {{ "action": "open_app", "app": "notepad" }}

Input: "open calculator"
Output: {{ "action": "open_app", "app": "calculator" }}

Input: "open file explorer"
Output: {{ "action": "open_app", "app": "file explorer" }}

Input: "open vscode"
Output: {{ "action": "open_app", "app": "vscode" }}

Input: "open settings"
Output: {{ "action": "open_app", "app": "settings" }}

Input: "search gold price on google"
Output: {{ "action": "google_search", "query": "gold price" }}

Input: "open youtube"
Output: {{ "action": "open_youtube" }}

Input: "hello"
Output: {{ "action": "none" }}

User command: "{command}"
"""

    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }

    try:
        res = requests.post(OLLAMA_URL, json=payload, timeout=60)
        text = res.json().get("response", "").strip()
        return json.loads(text)
    except Exception as e:
        print("OS intent error:", e)
        return {"action": "none"}
