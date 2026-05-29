import requests

r = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "vicuna:7b",
        "prompt": "Explain artificial intelligence in simple words",
        "stream": False
    }
)

print(r.status_code)
print(r.text)
