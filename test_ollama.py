import requests

def query_llm(prompt: str) -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )
    data = response.json()
    if "response" in data:
        return data["response"]
    else:
        print("Ollama API returned:", data)
        return "Sorry, I could not get a response."