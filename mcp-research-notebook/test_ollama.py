import os
import requests
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Read the Ollama model name and base URL from the environment
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:8b")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# Ollama's local chat endpoint
url = f"{OLLAMA_BASE_URL}/api/chat"

# The request payload we send to Ollama
payload = {
    "model": OLLAMA_MODEL,
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant. Answer briefly."
        },
        {
            "role": "user",
            "content": "Explain what MCP is in one sentence."
        }
    ],
    "stream": False
}

# Send the request to Ollama
response = requests.post(url, json=payload, timeout=60)

# Raise an error if the request failed
response.raise_for_status()

# Convert the JSON response into a Python dictionary
data = response.json()

# Print only the assistant's answer
print(data["message"]["content"])