# app/memory/short_term.py

memory = []

def add(role, text):
    """Store a message in memory"""
    memory.append({"role": role, "text": text})

def get():
    """Return conversation memory"""
    return memory

def clear():
    memory.clear()