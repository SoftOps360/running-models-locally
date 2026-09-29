"""Local Model 3 — Private data stays private. Parse a log that contains a SECRET,
entirely on your machine. Nothing is sent to any third-party API. This is why Ops needs local."""
import json
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
MODEL = "llama3.1"          # good default (8B). Lighter machine (CPU-only laptop)? use "llama3.2:1b".

# A log line you must NEVER paste into a public API — it carries a live token + internal IP.
log = ("2024/05/01 db-01 ERROR auth failed for user=svc_payments "
       "token=sk_live_9f83kZqR... while connecting to 10.0.2.14:5432")

resp = client.chat.completions.create(
    model=MODEL,
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": "Return only JSON."},
        {"role": "user", "content":
            f"Parse this internal log into JSON: {log}\n"
            'Return {"service": "", "problem": "", "host": "", "likely_cause": ""}. '
            "Do NOT copy any secret/token value into the output."},
    ],
)

print(json.loads(resp.choices[0].message.content))
print("\n(The secret in that log never left your machine.)")
