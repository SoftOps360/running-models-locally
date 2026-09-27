"""Local Model 1 — Hello, local LLM. No API key, no internet, no per-token cost.
The model runs on YOUR machine via Ollama — your data never leaves.

One-time setup:
  1. Install Ollama:  https://ollama.com
  2. Pull a model:    ollama pull llama3.1
  3. Ollama serves an OpenAI-compatible API at http://localhost:11434
"""
from openai import OpenAI

# Point the SAME OpenAI SDK at your local Ollama. api_key is required but ignored.
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
MODEL = "llama3.2:1b"       # fast on a CPU-only laptop. Stronger machine? "llama3.1" (8B) is smarter.

resp = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "In one line: what does a 502 Bad Gateway mean?"}],
)
print(resp.choices[0].message.content)
print("\n(This ran fully offline, on your machine.)")
