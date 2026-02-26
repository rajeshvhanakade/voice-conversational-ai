import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"

def query_llm(prompt: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "⚠️ No response from model.")
    except requests.exceptions.RequestException as e:
        return f"⚠️ Ollama error: {e}"