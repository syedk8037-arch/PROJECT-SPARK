import json
import os
from brain.normalizer import normalize_question

MEMORY_FILE = "memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2, ensure_ascii=False)

def recall(question):
    memory = load_memory()
    key = normalize_question(question)
    return memory.get(key)

def remember(question, answer):
    memory = load_memory()
    key = normalize_question(question)

    if key and key not in memory:
        memory[key] = answer
        save_memory(memory)

    if key and key not in memory:
        memory[key] = answer
        save_memory(memory)

    # Avoid overwriting good memory
    if key not in memory:
        memory[key] = answer
        save_memory(memory)
