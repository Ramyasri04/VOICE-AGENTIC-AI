import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_ai(prompt):

    try:

        payload = {
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(OLLAMA_URL, json=payload)

        response.raise_for_status()

        return response.json()["response"]

    except requests.exceptions.ConnectionError:
        return "Ollama server is not running."

    except Exception as e:
        return f"AI Error: {e}"