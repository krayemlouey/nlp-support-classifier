import json
import os

FILE = "messages.json"

def load_messages():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_message(message):
    messages = load_messages()
    messages.append(message)

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2, ensure_ascii=False)