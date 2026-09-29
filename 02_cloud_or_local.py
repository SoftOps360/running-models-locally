"""Local Model 2 — Same code, cloud OR local. Flip ONE flag; nothing else changes.
That's the whole point: it's the same OpenAI SDK, just a different base_url + model."""
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

USE_LOCAL = True          # ← flip this to False to use the cloud instead

if USE_LOCAL:
    client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
    MODEL, where = "llama3.1", "LOCAL (Ollama)"   # good default (8B); "llama3.2:1b" on a lighter CPU-only box
else:
    client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=os.environ["GROQ_API_KEY"])
    MODEL, where = "openai/gpt-oss-120b", "CLOUD (Groq)"

resp = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Give one tip to reduce nginx 502 errors."}],
)
print(f"[{where}]\n{resp.choices[0].message.content}")
